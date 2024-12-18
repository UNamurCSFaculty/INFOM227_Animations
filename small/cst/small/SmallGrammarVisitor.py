# Generated from small/SmallGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SmallGrammarParser import SmallGrammarParser
else:
    from SmallGrammarParser import SmallGrammarParser

# This class defines a complete generic visitor for a parse tree produced by SmallGrammarParser.

class SmallGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SmallGrammarParser#program.
    def visitProgram(self, ctx:SmallGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#function.
    def visitFunction(self, ctx:SmallGrammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#paramList.
    def visitParamList(self, ctx:SmallGrammarParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#param.
    def visitParam(self, ctx:SmallGrammarParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#stmt.
    def visitStmt(self, ctx:SmallGrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#assignStmt.
    def visitAssignStmt(self, ctx:SmallGrammarParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#ifStmt.
    def visitIfStmt(self, ctx:SmallGrammarParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#whileStmt.
    def visitWhileStmt(self, ctx:SmallGrammarParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#returnStmt.
    def visitReturnStmt(self, ctx:SmallGrammarParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#stmtList.
    def visitStmtList(self, ctx:SmallGrammarParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#sequence.
    def visitSequence(self, ctx:SmallGrammarParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#exprList.
    def visitExprList(self, ctx:SmallGrammarParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#funcCall.
    def visitFuncCall(self, ctx:SmallGrammarParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#expr.
    def visitExpr(self, ctx:SmallGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#arithExpr.
    def visitArithExpr(self, ctx:SmallGrammarParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#boolExpr.
    def visitBoolExpr(self, ctx:SmallGrammarParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#binMathOp.
    def visitBinMathOp(self, ctx:SmallGrammarParser.BinMathOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#binLogicOp.
    def visitBinLogicOp(self, ctx:SmallGrammarParser.BinLogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#relOp.
    def visitRelOp(self, ctx:SmallGrammarParser.RelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#noprnd.
    def visitNoprnd(self, ctx:SmallGrammarParser.NoprndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#boprnd.
    def visitBoprnd(self, ctx:SmallGrammarParser.BoprndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#mathOp.
    def visitMathOp(self, ctx:SmallGrammarParser.MathOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#logicOp.
    def visitLogicOp(self, ctx:SmallGrammarParser.LogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallGrammarParser#nop.
    def visitNop(self, ctx:SmallGrammarParser.NopContext):
        return self.visitChildren(ctx)



del SmallGrammarParser