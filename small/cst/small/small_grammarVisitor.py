# Generated from small/small_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .small_grammarParser import small_grammarParser
else:
    from small_grammarParser import small_grammarParser

# This class defines a complete generic visitor for a parse tree produced by small_grammarParser.

class small_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by small_grammarParser#math_op.
    def visitMath_op(self, ctx:small_grammarParser.Math_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#logic_op.
    def visitLogic_op(self, ctx:small_grammarParser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#nop.
    def visitNop(self, ctx:small_grammarParser.NopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#expr.
    def visitExpr(self, ctx:small_grammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#arith_expr.
    def visitArith_expr(self, ctx:small_grammarParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#bool_expr.
    def visitBool_expr(self, ctx:small_grammarParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#bin_math_op.
    def visitBin_math_op(self, ctx:small_grammarParser.Bin_math_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#bin_logic_op.
    def visitBin_logic_op(self, ctx:small_grammarParser.Bin_logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#rel_op.
    def visitRel_op(self, ctx:small_grammarParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#noprnd.
    def visitNoprnd(self, ctx:small_grammarParser.NoprndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#boprnd.
    def visitBoprnd(self, ctx:small_grammarParser.BoprndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#expr_list.
    def visitExpr_list(self, ctx:small_grammarParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#func_call.
    def visitFunc_call(self, ctx:small_grammarParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#stmt.
    def visitStmt(self, ctx:small_grammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#assign_stmt.
    def visitAssign_stmt(self, ctx:small_grammarParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#if_stmt.
    def visitIf_stmt(self, ctx:small_grammarParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#while_stmt.
    def visitWhile_stmt(self, ctx:small_grammarParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#return_stmt.
    def visitReturn_stmt(self, ctx:small_grammarParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#stmt_list.
    def visitStmt_list(self, ctx:small_grammarParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#sequence.
    def visitSequence(self, ctx:small_grammarParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#program.
    def visitProgram(self, ctx:small_grammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#function.
    def visitFunction(self, ctx:small_grammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#param_list.
    def visitParam_list(self, ctx:small_grammarParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by small_grammarParser#param.
    def visitParam(self, ctx:small_grammarParser.ParamContext):
        return self.visitChildren(ctx)



del small_grammarParser