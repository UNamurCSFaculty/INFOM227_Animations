# Generated from small/SmallGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,1,1,1,
        1,1,1,1,3,1,57,8,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,67,8,2,10,
        2,12,2,70,9,2,1,3,1,3,1,3,1,3,1,3,3,3,77,8,3,1,4,5,4,80,8,4,10,4,
        12,4,83,9,4,1,5,1,5,1,5,1,5,3,5,89,8,5,1,6,1,6,1,6,1,6,3,6,95,8,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,120,8,10,1,10,1,10,1,11,1,
        11,1,11,5,11,127,8,11,10,11,12,11,130,9,11,1,12,1,12,3,12,134,8,
        12,1,13,1,13,3,13,138,8,13,1,14,1,14,1,14,3,14,143,8,14,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,19,
        1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,0,23,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,5,1,0,27,28,2,0,25,
        26,28,28,1,0,15,18,1,0,19,24,2,0,13,14,23,24,158,0,49,1,0,0,0,2,
        52,1,0,0,0,4,63,1,0,0,0,6,76,1,0,0,0,8,81,1,0,0,0,10,88,1,0,0,0,
        12,90,1,0,0,0,14,98,1,0,0,0,16,106,1,0,0,0,18,112,1,0,0,0,20,116,
        1,0,0,0,22,123,1,0,0,0,24,133,1,0,0,0,26,137,1,0,0,0,28,142,1,0,
        0,0,30,144,1,0,0,0,32,148,1,0,0,0,34,152,1,0,0,0,36,156,1,0,0,0,
        38,158,1,0,0,0,40,160,1,0,0,0,42,162,1,0,0,0,44,164,1,0,0,0,46,48,
        3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,
        50,1,1,0,0,0,51,49,1,0,0,0,52,53,5,4,0,0,53,54,5,28,0,0,54,56,5,
        8,0,0,55,57,3,4,2,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,
        59,5,9,0,0,59,60,5,6,0,0,60,61,3,8,4,0,61,62,5,7,0,0,62,3,1,0,0,
        0,63,68,5,28,0,0,64,65,5,10,0,0,65,67,5,28,0,0,66,64,1,0,0,0,67,
        70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,5,1,0,0,0,70,68,1,0,0,
        0,71,77,3,10,5,0,72,73,5,6,0,0,73,74,3,8,4,0,74,75,5,7,0,0,75,77,
        1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,77,7,1,0,0,0,78,80,3,10,5,0,
        79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,9,1,0,
        0,0,83,81,1,0,0,0,84,89,3,12,6,0,85,89,3,14,7,0,86,89,3,16,8,0,87,
        89,3,18,9,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,88,87,1,0,
        0,0,89,11,1,0,0,0,90,91,5,28,0,0,91,94,5,12,0,0,92,95,3,24,12,0,
        93,95,3,20,10,0,94,92,1,0,0,0,94,93,1,0,0,0,95,96,1,0,0,0,96,97,
        5,11,0,0,97,13,1,0,0,0,98,99,5,1,0,0,99,100,5,8,0,0,100,101,3,28,
        14,0,101,102,5,9,0,0,102,103,3,6,3,0,103,104,5,2,0,0,104,105,3,6,
        3,0,105,15,1,0,0,0,106,107,5,3,0,0,107,108,5,8,0,0,108,109,3,28,
        14,0,109,110,5,9,0,0,110,111,3,6,3,0,111,17,1,0,0,0,112,113,5,5,
        0,0,113,114,3,24,12,0,114,115,5,11,0,0,115,19,1,0,0,0,116,117,5,
        28,0,0,117,119,5,8,0,0,118,120,3,22,11,0,119,118,1,0,0,0,119,120,
        1,0,0,0,120,121,1,0,0,0,121,122,5,9,0,0,122,21,1,0,0,0,123,128,3,
        24,12,0,124,125,5,10,0,0,125,127,3,24,12,0,126,124,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,23,1,0,0,0,130,128,1,
        0,0,0,131,134,3,26,13,0,132,134,3,28,14,0,133,131,1,0,0,0,133,132,
        1,0,0,0,134,25,1,0,0,0,135,138,3,36,18,0,136,138,3,30,15,0,137,135,
        1,0,0,0,137,136,1,0,0,0,138,27,1,0,0,0,139,143,3,38,19,0,140,143,
        3,34,17,0,141,143,3,32,16,0,142,139,1,0,0,0,142,140,1,0,0,0,142,
        141,1,0,0,0,143,29,1,0,0,0,144,145,3,36,18,0,145,146,3,40,20,0,146,
        147,3,36,18,0,147,31,1,0,0,0,148,149,3,36,18,0,149,150,3,42,21,0,
        150,151,3,36,18,0,151,33,1,0,0,0,152,153,3,38,19,0,153,154,3,44,
        22,0,154,155,3,38,19,0,155,35,1,0,0,0,156,157,7,0,0,0,157,37,1,0,
        0,0,158,159,7,1,0,0,159,39,1,0,0,0,160,161,7,2,0,0,161,41,1,0,0,
        0,162,163,7,3,0,0,163,43,1,0,0,0,164,165,7,4,0,0,165,45,1,0,0,0,
        12,49,56,68,76,81,88,94,119,128,133,137,142
    ]

class SmallGrammarParser ( Parser ):

    grammarFileName = "SmallGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'function'", 
                     "'return'", "'{'", "'}'", "'('", "')'", "','", "';'", 
                     "'='", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
                     "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'True'", 
                     "'False'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FUNCTION", "RETURN", 
                      "LBRACE", "RBRACE", "LPAR", "RPAR", "COMMA", "SEMICOLON", 
                      "ASSIGN", "AND", "OR", "ADD", "SUBSTRACT", "MULTIPLY", 
                      "DIVIDE", "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL", 
                      "EQUAL", "DIFFERENT", "TRUE", "FALSE", "NUM", "IDENTIFIER", 
                      "COMMENT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_function = 1
    RULE_paramList = 2
    RULE_sequence = 3
    RULE_stmtList = 4
    RULE_stmt = 5
    RULE_assignStmt = 6
    RULE_ifStmt = 7
    RULE_whileStmt = 8
    RULE_returnStmt = 9
    RULE_funcCall = 10
    RULE_exprList = 11
    RULE_expr = 12
    RULE_arithExpr = 13
    RULE_boolExpr = 14
    RULE_binMathOp = 15
    RULE_binLogicOp = 16
    RULE_relOp = 17
    RULE_noprnd = 18
    RULE_boprnd = 19
    RULE_mathOp = 20
    RULE_logicOp = 21
    RULE_nop = 22

    ruleNames =  [ "program", "function", "paramList", "sequence", "stmtList", 
                   "stmt", "assignStmt", "ifStmt", "whileStmt", "returnStmt", 
                   "funcCall", "exprList", "expr", "arithExpr", "boolExpr", 
                   "binMathOp", "binLogicOp", "relOp", "noprnd", "boprnd", 
                   "mathOp", "logicOp", "nop" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FUNCTION=4
    RETURN=5
    LBRACE=6
    RBRACE=7
    LPAR=8
    RPAR=9
    COMMA=10
    SEMICOLON=11
    ASSIGN=12
    AND=13
    OR=14
    ADD=15
    SUBSTRACT=16
    MULTIPLY=17
    DIVIDE=18
    GREATER=19
    GREATER_EQUAL=20
    LESS=21
    LESS_EQUAL=22
    EQUAL=23
    DIFFERENT=24
    TRUE=25
    FALSE=26
    NUM=27
    IDENTIFIER=28
    COMMENT=29
    NEWLINE=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallGrammarParser.FunctionContext)
            else:
                return self.getTypedRuleContext(SmallGrammarParser.FunctionContext,i)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SmallGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 46
                self.function()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(SmallGrammarParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(SmallGrammarParser.IDENTIFIER, 0)

        def LPAR(self):
            return self.getToken(SmallGrammarParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SmallGrammarParser.RPAR, 0)

        def LBRACE(self):
            return self.getToken(SmallGrammarParser.LBRACE, 0)

        def stmtList(self):
            return self.getTypedRuleContext(SmallGrammarParser.StmtListContext,0)


        def RBRACE(self):
            return self.getToken(SmallGrammarParser.RBRACE, 0)

        def paramList(self):
            return self.getTypedRuleContext(SmallGrammarParser.ParamListContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = SmallGrammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SmallGrammarParser.FUNCTION)
            self.state = 53
            self.match(SmallGrammarParser.IDENTIFIER)
            self.state = 54
            self.match(SmallGrammarParser.LPAR)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 55
                self.paramList()


            self.state = 58
            self.match(SmallGrammarParser.RPAR)
            self.state = 59
            self.match(SmallGrammarParser.LBRACE)
            self.state = 60
            self.stmtList()
            self.state = 61
            self.match(SmallGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(SmallGrammarParser.IDENTIFIER)
            else:
                return self.getToken(SmallGrammarParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SmallGrammarParser.COMMA)
            else:
                return self.getToken(SmallGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = SmallGrammarParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SmallGrammarParser.IDENTIFIER)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 64
                self.match(SmallGrammarParser.COMMA)
                self.state = 65
                self.match(SmallGrammarParser.IDENTIFIER)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(SmallGrammarParser.StmtContext,0)


        def LBRACE(self):
            return self.getToken(SmallGrammarParser.LBRACE, 0)

        def stmtList(self):
            return self.getTypedRuleContext(SmallGrammarParser.StmtListContext,0)


        def RBRACE(self):
            return self.getToken(SmallGrammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_sequence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = SmallGrammarParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sequence)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(SmallGrammarParser.LBRACE)
                self.state = 73
                self.stmtList()
                self.state = 74
                self.match(SmallGrammarParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallGrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(SmallGrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_stmtList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = SmallGrammarParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435498) != 0):
                self.state = 78
                self.stmt()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(SmallGrammarParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(SmallGrammarParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(SmallGrammarParser.WhileStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(SmallGrammarParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = SmallGrammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.assignStmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.ifStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.whileStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.returnStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SmallGrammarParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(SmallGrammarParser.ASSIGN, 0)

        def SEMICOLON(self):
            return self.getToken(SmallGrammarParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(SmallGrammarParser.ExprContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(SmallGrammarParser.FuncCallContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = SmallGrammarParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SmallGrammarParser.IDENTIFIER)
            self.state = 91
            self.match(SmallGrammarParser.ASSIGN)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 92
                self.expr()
                pass

            elif la_ == 2:
                self.state = 93
                self.funcCall()
                pass


            self.state = 96
            self.match(SmallGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ifBody = None # SequenceContext
            self.elseBody = None # SequenceContext

        def IF(self):
            return self.getToken(SmallGrammarParser.IF, 0)

        def LPAR(self):
            return self.getToken(SmallGrammarParser.LPAR, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(SmallGrammarParser.BoolExprContext,0)


        def RPAR(self):
            return self.getToken(SmallGrammarParser.RPAR, 0)

        def ELSE(self):
            return self.getToken(SmallGrammarParser.ELSE, 0)

        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallGrammarParser.SequenceContext)
            else:
                return self.getTypedRuleContext(SmallGrammarParser.SequenceContext,i)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = SmallGrammarParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(SmallGrammarParser.IF)
            self.state = 99
            self.match(SmallGrammarParser.LPAR)
            self.state = 100
            self.boolExpr()
            self.state = 101
            self.match(SmallGrammarParser.RPAR)
            self.state = 102
            localctx.ifBody = self.sequence()
            self.state = 103
            self.match(SmallGrammarParser.ELSE)
            self.state = 104
            localctx.elseBody = self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SmallGrammarParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(SmallGrammarParser.LPAR, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(SmallGrammarParser.BoolExprContext,0)


        def RPAR(self):
            return self.getToken(SmallGrammarParser.RPAR, 0)

        def sequence(self):
            return self.getTypedRuleContext(SmallGrammarParser.SequenceContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = SmallGrammarParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SmallGrammarParser.WHILE)
            self.state = 107
            self.match(SmallGrammarParser.LPAR)
            self.state = 108
            self.boolExpr()
            self.state = 109
            self.match(SmallGrammarParser.RPAR)
            self.state = 110
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SmallGrammarParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(SmallGrammarParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(SmallGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = SmallGrammarParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(SmallGrammarParser.RETURN)
            self.state = 113
            self.expr()
            self.state = 114
            self.match(SmallGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SmallGrammarParser.IDENTIFIER, 0)

        def LPAR(self):
            return self.getToken(SmallGrammarParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SmallGrammarParser.RPAR, 0)

        def exprList(self):
            return self.getTypedRuleContext(SmallGrammarParser.ExprListContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = SmallGrammarParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(SmallGrammarParser.IDENTIFIER)
            self.state = 117
            self.match(SmallGrammarParser.LPAR)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0):
                self.state = 118
                self.exprList()


            self.state = 121
            self.match(SmallGrammarParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(SmallGrammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SmallGrammarParser.COMMA)
            else:
                return self.getToken(SmallGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = SmallGrammarParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.expr()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 124
                self.match(SmallGrammarParser.COMMA)
                self.state = 125
                self.expr()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr(self):
            return self.getTypedRuleContext(SmallGrammarParser.ArithExprContext,0)


        def boolExpr(self):
            return self.getTypedRuleContext(SmallGrammarParser.BoolExprContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SmallGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.arithExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.boolExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noprnd(self):
            return self.getTypedRuleContext(SmallGrammarParser.NoprndContext,0)


        def binMathOp(self):
            return self.getTypedRuleContext(SmallGrammarParser.BinMathOpContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_arithExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr" ):
                return visitor.visitArithExpr(self)
            else:
                return visitor.visitChildren(self)




    def arithExpr(self):

        localctx = SmallGrammarParser.ArithExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arithExpr)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.noprnd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.binMathOp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boprnd(self):
            return self.getTypedRuleContext(SmallGrammarParser.BoprndContext,0)


        def relOp(self):
            return self.getTypedRuleContext(SmallGrammarParser.RelOpContext,0)


        def binLogicOp(self):
            return self.getTypedRuleContext(SmallGrammarParser.BinLogicOpContext,0)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_boolExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)




    def boolExpr(self):

        localctx = SmallGrammarParser.BoolExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boolExpr)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.boprnd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.relOp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.binLogicOp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinMathOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # NoprndContext
            self.right = None # NoprndContext

        def mathOp(self):
            return self.getTypedRuleContext(SmallGrammarParser.MathOpContext,0)


        def noprnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallGrammarParser.NoprndContext)
            else:
                return self.getTypedRuleContext(SmallGrammarParser.NoprndContext,i)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_binMathOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinMathOp" ):
                return visitor.visitBinMathOp(self)
            else:
                return visitor.visitChildren(self)




    def binMathOp(self):

        localctx = SmallGrammarParser.BinMathOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_binMathOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            localctx.left = self.noprnd()
            self.state = 145
            self.mathOp()
            self.state = 146
            localctx.right = self.noprnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinLogicOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # NoprndContext
            self.right = None # NoprndContext

        def logicOp(self):
            return self.getTypedRuleContext(SmallGrammarParser.LogicOpContext,0)


        def noprnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallGrammarParser.NoprndContext)
            else:
                return self.getTypedRuleContext(SmallGrammarParser.NoprndContext,i)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_binLogicOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinLogicOp" ):
                return visitor.visitBinLogicOp(self)
            else:
                return visitor.visitChildren(self)




    def binLogicOp(self):

        localctx = SmallGrammarParser.BinLogicOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_binLogicOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            localctx.left = self.noprnd()
            self.state = 149
            self.logicOp()
            self.state = 150
            localctx.right = self.noprnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # BoprndContext
            self.right = None # BoprndContext

        def nop(self):
            return self.getTypedRuleContext(SmallGrammarParser.NopContext,0)


        def boprnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallGrammarParser.BoprndContext)
            else:
                return self.getTypedRuleContext(SmallGrammarParser.BoprndContext,i)


        def getRuleIndex(self):
            return SmallGrammarParser.RULE_relOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelOp" ):
                return visitor.visitRelOp(self)
            else:
                return visitor.visitChildren(self)




    def relOp(self):

        localctx = SmallGrammarParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            localctx.left = self.boprnd()
            self.state = 153
            self.nop()
            self.state = 154
            localctx.right = self.boprnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoprndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SmallGrammarParser.IDENTIFIER, 0)

        def NUM(self):
            return self.getToken(SmallGrammarParser.NUM, 0)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_noprnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoprnd" ):
                return visitor.visitNoprnd(self)
            else:
                return visitor.visitChildren(self)




    def noprnd(self):

        localctx = SmallGrammarParser.NoprndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_noprnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoprndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SmallGrammarParser.IDENTIFIER, 0)

        def TRUE(self):
            return self.getToken(SmallGrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SmallGrammarParser.FALSE, 0)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_boprnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoprnd" ):
                return visitor.visitBoprnd(self)
            else:
                return visitor.visitChildren(self)




    def boprnd(self):

        localctx = SmallGrammarParser.BoprndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_boprnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 369098752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(SmallGrammarParser.ADD, 0)

        def SUBSTRACT(self):
            return self.getToken(SmallGrammarParser.SUBSTRACT, 0)

        def MULTIPLY(self):
            return self.getToken(SmallGrammarParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(SmallGrammarParser.DIVIDE, 0)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_mathOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOp" ):
                return visitor.visitMathOp(self)
            else:
                return visitor.visitChildren(self)




    def mathOp(self):

        localctx = SmallGrammarParser.MathOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mathOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(SmallGrammarParser.LESS, 0)

        def GREATER(self):
            return self.getToken(SmallGrammarParser.GREATER, 0)

        def EQUAL(self):
            return self.getToken(SmallGrammarParser.EQUAL, 0)

        def DIFFERENT(self):
            return self.getToken(SmallGrammarParser.DIFFERENT, 0)

        def GREATER_EQUAL(self):
            return self.getToken(SmallGrammarParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(SmallGrammarParser.LESS_EQUAL, 0)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_logicOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOp" ):
                return visitor.visitLogicOp(self)
            else:
                return visitor.visitChildren(self)




    def logicOp(self):

        localctx = SmallGrammarParser.LogicOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(SmallGrammarParser.EQUAL, 0)

        def DIFFERENT(self):
            return self.getToken(SmallGrammarParser.DIFFERENT, 0)

        def AND(self):
            return self.getToken(SmallGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(SmallGrammarParser.OR, 0)

        def getRuleIndex(self):
            return SmallGrammarParser.RULE_nop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNop" ):
                return visitor.visitNop(self)
            else:
                return visitor.visitChildren(self)




    def nop(self):

        localctx = SmallGrammarParser.NopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_nop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 25190400) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





