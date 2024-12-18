from small.cst.small.SmallGrammarVisitor import SmallGrammarVisitor
from small.cst.small.SmallGrammarParser import SmallGrammarParser
from small.ast.symbol_table import RootSymbolTable, FunctionSymbolTable
from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl
import small.ast as ast
from typing import Self, cast, Any, Generator
from contextlib import contextmanager


def term(node: Any) -> TerminalNodeImpl | None:
    return cast(TerminalNodeImpl | None, node)


class CannotBuildAstException(Exception):
    def __init__(
        self,
        message: str,
        line: int | None = None,
    ):
        super().__init__(f"Line {line} - {message}" if line is not None else message)
        self.message = message
        self.line = line

    @classmethod
    def from_ctx(cls, message: str, ctx: ParserRuleContext | None = None) -> Self:
        return cls(message, ctx.start.line if ctx is not None else None)


class UnsupportedRuleException(CannotBuildAstException):
    def __init__(self, message: str, line: int | None = None):
        super().__init__(message, line)


class MissingScopeException(CannotBuildAstException):
    def __init__(self, message: str):
        super().__init__(message, None)


class SmallAstBuilder(SmallGrammarVisitor):
    def __init__(
        self,
        root_symbol_table: RootSymbolTable | None = None,
        function_symbol_table: FunctionSymbolTable | None = None,
        program: str | None = None,
    ):
        super().__init__()

        self._root_symbol_table = root_symbol_table or RootSymbolTable()
        self._function_symbol_table = function_symbol_table
        self._program = program

    @contextmanager
    def _scope(self) -> Generator[FunctionSymbolTable, None, None]:
        if self._function_symbol_table is None:
            raise MissingScopeException("No function scope defined")

        yield self._function_symbol_table

    @contextmanager
    def _new_scope(
        self, function_symbol_table: FunctionSymbolTable
    ) -> Generator[FunctionSymbolTable, None, None]:
        old_function_symbol_table = self._function_symbol_table

        self._function_symbol_table = function_symbol_table

        try:
            yield function_symbol_table
        finally:
            self._function_symbol_table = old_function_symbol_table

    # Programs

    def visitProgram(
        self, ctx: SmallGrammarParser.ProgramContext
    ) -> tuple[ast.Function]:
        return tuple(
            self.visitFunction(function)
            for function in cast(
                list[SmallGrammarParser.FunctionContext], ctx.function()
            )
        )

    def visitFunction(self, ctx: SmallGrammarParser.FunctionContext) -> ast.Function:
        name = cast(str, term(ctx.IDENTIFIER()).getText())

        if (
            param_list := cast(SmallGrammarParser.ParamListContext, ctx.paramList())
        ) is not None:
            params = self.visitParamList(param_list)
        else:
            params: tuple[str, ...] = tuple()

        with self._new_scope(
            self._root_symbol_table.declare_function(name, params)
        ) as symbol_table:
            statements = self.visitStmtList(
                cast(SmallGrammarParser.SequenceContext, ctx.stmtList())
            )

        if self._program is not None:
            function_code = "\n".join(
                self._program.splitlines()[ctx.start.line - 1 : ctx.stop.line]
            )
        else:
            function_code = None

        return ast.Function(
            ctx.start.line,
            name,
            params,
            symbol_table.variables().difference(params),
            statements,
            function_code,
        )

    def visitParamList(
        self, ctx: SmallGrammarParser.ParamListContext
    ) -> tuple[str, ...]:
        return tuple(
            cast(str, param.getText())
            for param in cast(list[TerminalNodeImpl], ctx.IDENTIFIER())
        )

    # Statements

    def visitSequence(
        self, ctx: SmallGrammarParser.SequenceContext
    ) -> tuple[ast.Statement, ...]:
        if (stmt := cast(SmallGrammarParser.StmtContext, ctx.stmt())) is not None:
            return (self.visitStmt(stmt),)
        elif (
            stmts := cast(SmallGrammarParser.StmtListContext, ctx.stmtList())
        ) is not None:
            return self.visitStmtList(stmts)
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported sequence: {ctx.getText()}", ctx
            )

    def visitStmtList(
        self, ctx: SmallGrammarParser.StmtListContext
    ) -> tuple[ast.Statement, ...]:
        return tuple(
            self.visitStmt(stmt)
            for stmt in cast(list[SmallGrammarParser.StmtContext], ctx.stmt())
        )

    def visitStmt(self, ctx: SmallGrammarParser.StmtContext) -> ast.Statement:
        if (
            assign_stmt := cast(SmallGrammarParser.AssignStmtContext, ctx.assignStmt())
        ) is not None:
            return self.visitAssignStmt(assign_stmt)
        elif (
            if_stmt := cast(SmallGrammarParser.IfStmtContext, ctx.ifStmt())
        ) is not None:
            return self.visitIfStmt(if_stmt)
        elif (
            while_stmt := cast(SmallGrammarParser.WhileStmtContext, ctx.whileStmt())
        ) is not None:
            return self.visitWhileStmt(while_stmt)
        elif (
            return_stmt := cast(SmallGrammarParser.ReturnStmtContext, ctx.returnStmt())
        ) is not None:
            return self.visitReturnStmt(return_stmt)
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported stmt: {ctx.getText()}", ctx
            )

    def visitAssignStmt(
        self, ctx: SmallGrammarParser.AssignStmtContext
    ) -> ast.Assignment:
        variable = cast(str, term(ctx.IDENTIFIER()).getText())

        if (expr := term(ctx.expr())) is not None:
            assignment_expr = self.visitExpr(cast(SmallGrammarParser.ExprContext, expr))
        elif (func_call := term(ctx.funcCall())) is not None:
            assignment_expr = self.visitFuncCall(
                cast(SmallGrammarParser.FuncCallContext, func_call)
            )
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported assignStmt: {ctx.getText()}", ctx
            )

        with self._scope() as symbol_table:
            try:
                symbol_table.use(variable, assignment_expr.type(symbol_table))
            except ValueError as e:
                raise UnsupportedRuleException.from_ctx(str(e), ctx)

        return ast.Assignment(ctx.start.line, variable, assignment_expr)

    def visitIfStmt(self, ctx: SmallGrammarParser.IfStmtContext) -> ast.IfElse:
        condition = self.visitBoolExpr(
            cast(SmallGrammarParser.BoolExprContext, ctx.boolExpr())
        )
        then_statements = self.visitSequence(
            cast(SmallGrammarParser.SequenceContext, ctx.ifBody)
        )
        else_statements = self.visitSequence(
            cast(SmallGrammarParser.SequenceContext, ctx.elseBody)
        )

        return ast.IfElse(ctx.start.line, condition, then_statements, else_statements)

    def visitWhileStmt(self, ctx: SmallGrammarParser.WhileStmtContext) -> ast.While:
        condition = self.visitBoolExpr(
            cast(SmallGrammarParser.BoolExprContext, ctx.boolExpr())
        )
        statements = self.visitSequence(
            cast(SmallGrammarParser.SequenceContext, ctx.sequence())
        )

        return ast.While(ctx.start.line, condition, statements)

    def visitReturnStmt(self, ctx: SmallGrammarParser.ReturnStmtContext) -> ast.Return:
        expr = self.visitExpr(cast(SmallGrammarParser.ExprContext, ctx.expr()))

        with self._scope() as symbol_table:
            try:
                symbol_table.return_(expr.type(symbol_table))
            except ValueError as e:
                raise UnsupportedRuleException.from_ctx(str(e), ctx)

        return ast.Return(ctx.start.line, expr)

    # Expressions

    def visitFuncCall(
        self, ctx: SmallGrammarParser.FuncCallContext
    ) -> ast.FunctionCall:
        name = cast(str, term(ctx.IDENTIFIER()).getText())
        expr_list = cast(SmallGrammarParser.ExprListContext | None, ctx.exprList())

        if expr_list is None:
            arguments = []
        else:
            arguments = self.visitExprList(expr_list)

        with self._scope() as symbol_table:
            try:
                self._root_symbol_table.call(
                    expression.type(symbol_table) for expression in arguments
                )
            except ValueError as e:
                raise UnsupportedRuleException.from_ctx(str(e), ctx)

        return ast.FunctionCall(name, arguments)

    def visitExprList(
        self, ctx: SmallGrammarParser.ExprListContext
    ) -> list[ast.Expression]:
        return [
            self.visitExpr(expr)
            for expr in cast(list[SmallGrammarParser.ExprContext], ctx.expr())
        ]

    def visitExpr(self, ctx: SmallGrammarParser.ExprContext) -> ast.Expression:
        if (
            arithExpr := cast(SmallGrammarParser.ArithExprContext, ctx.arithExpr())
        ) is not None:
            return self.visitArithExpr(arithExpr)
        elif (
            boolExpr := cast(SmallGrammarParser.BoolExprContext, ctx.boolExpr())
        ) is not None:
            return self.visitBoolExpr(boolExpr)
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported expr: {ctx.getText()}", ctx
            )

    def visitArithExpr(
        self, ctx: SmallGrammarParser.ArithExprContext
    ) -> ast.IntExpression:
        if (noprnd := cast(SmallGrammarParser.NoprndContext, ctx.noprnd())) is not None:
            return self.visitNoprnd(noprnd)
        elif (
            binMathOp := cast(SmallGrammarParser.BinMathOpContext, ctx.binMathOp())
        ) is not None:
            return self.visitBinMathOp(binMathOp)
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported arithExpr: {ctx.getText()}", ctx
            )

    def visitBoolExpr(
        self, ctx: SmallGrammarParser.BoolExprContext
    ) -> ast.BoolExpression:
        if (boprnd := cast(SmallGrammarParser.BoprndContext, ctx.boprnd())) is not None:
            return self.visitBoprnd(boprnd)
        elif (relOp := cast(SmallGrammarParser.RelOpContext, ctx.relOp())) is not None:
            return self.visitRelOp(relOp)
        elif (
            binLogicOp := cast(SmallGrammarParser.BinLogicOpContext, ctx.binLogicOp())
        ) is not None:
            return self.visitBinLogicOp(binLogicOp)
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported boolExpr: {ctx.getText()}", ctx
            )

    def visitBinMathOp(
        self, ctx: SmallGrammarParser.BinMathOpContext
    ) -> ast.IntExpression:
        left = self.visitNoprnd(cast(SmallGrammarParser.NoprndContext, ctx.left))
        right = self.visitNoprnd(cast(SmallGrammarParser.NoprndContext, ctx.right))
        operator = self.visitMathOp(
            cast(SmallGrammarParser.MathOpContext, ctx.mathOp())
        )

        return ast.IntBinaryExpression(left, operator, right)

    def visitBinLogicOp(
        self, ctx: SmallGrammarParser.BinLogicOpContext
    ) -> ast.BoolExpression:
        left = self.visitNoprnd(cast(SmallGrammarParser.NoprndContext, ctx.left))
        right = self.visitNoprnd(cast(SmallGrammarParser.NoprndContext, ctx.right))
        operator = self.visitLogicOp(
            cast(SmallGrammarParser.LogicOpContext, ctx.logicOp())
        )

        match operator:
            case (
                ast.IntComparisonOperator.LT
                | ast.IntComparisonOperator.GT
                | ast.IntComparisonOperator.LTE
                | ast.IntComparisonOperator.GTE
            ):
                return ast.IntComparisonExpression(left, operator, right)
            case ast.EqualityOperator.EQ | ast.EqualityOperator.NEQ:
                return ast.IntEqualComparisonExpression(left, operator, right)

    def visitRelOp(self, ctx: SmallGrammarParser.RelOpContext) -> ast.BoolExpression:
        left = self.visitBoprnd(cast(SmallGrammarParser.BoprndContext, ctx.left))
        right = self.visitBoprnd(cast(SmallGrammarParser.BoprndContext, ctx.right))
        operator = self.visitNop(cast(SmallGrammarParser.NopContext, ctx.nop()))

        match operator:
            case ast.EqualityOperator.EQ | ast.EqualityOperator.NEQ:
                return ast.BoolEqualComparisonExpression(left, operator, right)
            case ast.BoolComparisonOperator.AND | ast.BoolComparisonOperator.OR:
                return ast.BoolComparisonExpression(left, operator, right)

    def visitNoprnd(self, ctx: SmallGrammarParser.NoprndContext) -> ast.IntExpression:
        if (identifier := term(ctx.IDENTIFIER())) is not None:
            variable = cast(str, identifier.getText())

            with self._scope() as symbol_table:
                try:
                    symbol_table.use(variable, ast.SmallType.INT)
                except ValueError as e:
                    raise UnsupportedRuleException.from_ctx(str(e), ctx)

            return ast.Variable(variable)
        elif (number := term(ctx.NUM())) is not None:
            return ast.IntConstant(int(cast(str, number.getText())))
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported noprnd: {ctx.getText()}", ctx
            )

    def visitBoprnd(self, ctx: SmallGrammarParser.BoprndContext) -> ast.BoolExpression:
        if (identifier := term(ctx.IDENTIFIER())) is not None:
            variable = cast(str, identifier.getText())

            with self._scope() as symbol_table:
                try:
                    symbol_table.use(variable, ast.SmallType.BOOL)
                except ValueError as e:
                    raise UnsupportedRuleException.from_ctx(str(e), ctx)

            return ast.Variable(variable)
        elif term(ctx.TRUE()) is not None:
            return ast.BoolConstant(True)
        elif term(ctx.FALSE()) is not None:
            return ast.BoolConstant(False)
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported boprnd: {ctx.getText()}", ctx
            )

    # Operators

    def visitMathOp(
        self, ctx: SmallGrammarParser.MathOpContext
    ) -> ast.IntBinaryOperator:
        if term(ctx.ADD()) is not None:
            return ast.IntBinaryOperator.ADD
        elif term(ctx.SUBSTRACT()) is not None:
            return ast.IntBinaryOperator.SUB
        elif term(ctx.MULTIPLY()) is not None:
            return ast.IntBinaryOperator.MUL
        elif term(ctx.DIVIDE()) is not None:
            return ast.IntBinaryOperator.DIV
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported mathOp: {ctx.getText()}", ctx
            )

    def visitLogicOp(
        self, ctx: SmallGrammarParser.LogicOpContext
    ) -> ast.BoolComparisonOperator:
        if term(ctx.LESS()) is not None:
            return ast.IntComparisonOperator.LT
        elif term(ctx.GREATER()) is not None:
            return ast.IntComparisonOperator.GT
        elif term(ctx.EQUAL()) is not None:
            return ast.EqualityOperator.EQ
        elif term(ctx.DIFFERENT()) is not None:
            return ast.EqualityOperator.NEQ
        elif term(ctx.LESS_EQUAL()) is not None:
            return ast.IntComparisonOperator.LTE
        elif term(ctx.GREATER_EQUAL()) is not None:
            return ast.IntComparisonOperator.GTE
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported logicOp: {ctx.getText()}", ctx
            )

    def visitNop(
        self, ctx: SmallGrammarParser.NopContext
    ) -> ast.EqualityOperator | ast.BoolComparisonOperator:
        if term(ctx.EQUAL()) is not None:
            return ast.EqualityOperator.EQ
        elif term(ctx.DIFFERENT()) is not None:
            return ast.EqualityOperator.NEQ
        elif term(ctx.AND()) is not None:
            return ast.BoolComparisonOperator.AND
        elif term(ctx.OR()) is not None:
            return ast.BoolComparisonOperator.OR
        else:
            raise UnsupportedRuleException.from_ctx(
                f"Unsupported nop: {ctx.getText()}", ctx
            )


def build(
    program_cst: SmallGrammarParser.ProgramContext,
    root_symbol_table: RootSymbolTable | None = None,
    program: str | None = None,
) -> tuple[ast.Function]:
    builder = SmallAstBuilder(root_symbol_table=root_symbol_table, program=program)
    return builder.visitProgram(program_cst)
