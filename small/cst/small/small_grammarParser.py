# Generated from small/small_grammar.g4 by ANTLR 4.13.2
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
        4,1,31,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,3,3,57,8,3,1,4,1,4,3,4,61,8,4,1,5,1,5,1,5,3,5,66,8,5,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,
        1,11,5,11,87,8,11,10,11,12,11,90,9,11,1,12,1,12,1,12,3,12,95,8,12,
        1,12,1,12,1,13,1,13,1,13,1,13,3,13,103,8,13,1,14,1,14,1,14,1,14,
        3,14,109,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,5,18,132,
        8,18,10,18,12,18,135,9,18,1,19,1,19,1,19,1,19,1,19,3,19,142,8,19,
        1,20,5,20,145,8,20,10,20,12,20,148,9,20,1,21,1,21,1,21,1,21,3,21,
        154,8,21,1,21,1,21,1,21,1,22,1,22,1,22,5,22,162,8,22,10,22,12,22,
        165,9,22,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,0,5,1,0,15,18,1,0,19,24,2,0,13,
        14,23,24,1,0,27,28,2,0,25,26,28,28,159,0,48,1,0,0,0,2,50,1,0,0,0,
        4,52,1,0,0,0,6,56,1,0,0,0,8,60,1,0,0,0,10,65,1,0,0,0,12,67,1,0,0,
        0,14,71,1,0,0,0,16,75,1,0,0,0,18,79,1,0,0,0,20,81,1,0,0,0,22,83,
        1,0,0,0,24,91,1,0,0,0,26,102,1,0,0,0,28,104,1,0,0,0,30,112,1,0,0,
        0,32,120,1,0,0,0,34,126,1,0,0,0,36,133,1,0,0,0,38,141,1,0,0,0,40,
        146,1,0,0,0,42,149,1,0,0,0,44,158,1,0,0,0,46,166,1,0,0,0,48,49,7,
        0,0,0,49,1,1,0,0,0,50,51,7,1,0,0,51,3,1,0,0,0,52,53,7,2,0,0,53,5,
        1,0,0,0,54,57,3,8,4,0,55,57,3,10,5,0,56,54,1,0,0,0,56,55,1,0,0,0,
        57,7,1,0,0,0,58,61,3,18,9,0,59,61,3,12,6,0,60,58,1,0,0,0,60,59,1,
        0,0,0,61,9,1,0,0,0,62,66,3,20,10,0,63,66,3,16,8,0,64,66,3,14,7,0,
        65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,11,1,0,0,0,67,68,3,
        18,9,0,68,69,3,0,0,0,69,70,3,18,9,0,70,13,1,0,0,0,71,72,3,18,9,0,
        72,73,3,2,1,0,73,74,3,18,9,0,74,15,1,0,0,0,75,76,3,20,10,0,76,77,
        3,4,2,0,77,78,3,20,10,0,78,17,1,0,0,0,79,80,7,3,0,0,80,19,1,0,0,
        0,81,82,7,4,0,0,82,21,1,0,0,0,83,88,3,6,3,0,84,85,5,10,0,0,85,87,
        3,6,3,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,23,1,0,0,0,90,88,1,0,0,0,91,92,5,28,0,0,92,94,5,8,0,0,93,95,3,
        22,11,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,5,9,0,0,
        97,25,1,0,0,0,98,103,3,28,14,0,99,103,3,30,15,0,100,103,3,32,16,
        0,101,103,3,34,17,0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,
        0,102,101,1,0,0,0,103,27,1,0,0,0,104,105,5,28,0,0,105,108,5,23,0,
        0,106,109,3,6,3,0,107,109,3,24,12,0,108,106,1,0,0,0,108,107,1,0,
        0,0,109,110,1,0,0,0,110,111,5,11,0,0,111,29,1,0,0,0,112,113,5,1,
        0,0,113,114,5,8,0,0,114,115,3,10,5,0,115,116,5,9,0,0,116,117,3,38,
        19,0,117,118,5,2,0,0,118,119,3,38,19,0,119,31,1,0,0,0,120,121,5,
        3,0,0,121,122,5,8,0,0,122,123,3,10,5,0,123,124,5,9,0,0,124,125,3,
        38,19,0,125,33,1,0,0,0,126,127,5,5,0,0,127,128,3,6,3,0,128,129,5,
        11,0,0,129,35,1,0,0,0,130,132,3,26,13,0,131,130,1,0,0,0,132,135,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,37,1,0,0,0,135,133,1,
        0,0,0,136,142,3,26,13,0,137,138,5,6,0,0,138,139,3,36,18,0,139,140,
        5,7,0,0,140,142,1,0,0,0,141,136,1,0,0,0,141,137,1,0,0,0,142,39,1,
        0,0,0,143,145,3,42,21,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,41,1,0,0,0,148,146,1,0,0,0,149,150,5,
        4,0,0,150,151,5,28,0,0,151,153,5,8,0,0,152,154,3,44,22,0,153,152,
        1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,156,5,9,0,0,156,157,
        3,36,18,0,157,43,1,0,0,0,158,163,3,46,23,0,159,160,5,10,0,0,160,
        162,3,46,23,0,161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,
        164,1,0,0,0,164,45,1,0,0,0,165,163,1,0,0,0,166,167,5,28,0,0,167,
        47,1,0,0,0,12,56,60,65,88,94,102,108,133,141,146,153,163
    ]

class small_grammarParser ( Parser ):

    grammarFileName = "small_grammar.g4"

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

    RULE_math_op = 0
    RULE_logic_op = 1
    RULE_nop = 2
    RULE_expr = 3
    RULE_arith_expr = 4
    RULE_bool_expr = 5
    RULE_bin_math_op = 6
    RULE_bin_logic_op = 7
    RULE_rel_op = 8
    RULE_noprnd = 9
    RULE_boprnd = 10
    RULE_expr_list = 11
    RULE_func_call = 12
    RULE_stmt = 13
    RULE_assign_stmt = 14
    RULE_if_stmt = 15
    RULE_while_stmt = 16
    RULE_return_stmt = 17
    RULE_stmt_list = 18
    RULE_sequence = 19
    RULE_program = 20
    RULE_function = 21
    RULE_param_list = 22
    RULE_param = 23

    ruleNames =  [ "math_op", "logic_op", "nop", "expr", "arith_expr", "bool_expr", 
                   "bin_math_op", "bin_logic_op", "rel_op", "noprnd", "boprnd", 
                   "expr_list", "func_call", "stmt", "assign_stmt", "if_stmt", 
                   "while_stmt", "return_stmt", "stmt_list", "sequence", 
                   "program", "function", "param_list", "param" ]

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




    class Math_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(small_grammarParser.ADD, 0)

        def SUBSTRACT(self):
            return self.getToken(small_grammarParser.SUBSTRACT, 0)

        def MULTIPLY(self):
            return self.getToken(small_grammarParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(small_grammarParser.DIVIDE, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_math_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_op" ):
                return visitor.visitMath_op(self)
            else:
                return visitor.visitChildren(self)




    def math_op(self):

        localctx = small_grammarParser.Math_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_math_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
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


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(small_grammarParser.LESS, 0)

        def GREATER(self):
            return self.getToken(small_grammarParser.GREATER, 0)

        def EQUAL(self):
            return self.getToken(small_grammarParser.EQUAL, 0)

        def DIFFERENT(self):
            return self.getToken(small_grammarParser.DIFFERENT, 0)

        def GREATER_EQUAL(self):
            return self.getToken(small_grammarParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(small_grammarParser.LESS_EQUAL, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_logic_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_op" ):
                return visitor.visitLogic_op(self)
            else:
                return visitor.visitChildren(self)




    def logic_op(self):

        localctx = small_grammarParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
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
            return self.getToken(small_grammarParser.EQUAL, 0)

        def DIFFERENT(self):
            return self.getToken(small_grammarParser.DIFFERENT, 0)

        def AND(self):
            return self.getToken(small_grammarParser.AND, 0)

        def OR(self):
            return self.getToken(small_grammarParser.OR, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_nop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNop" ):
                return visitor.visitNop(self)
            else:
                return visitor.visitChildren(self)




    def nop(self):

        localctx = small_grammarParser.NopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_expr(self):
            return self.getTypedRuleContext(small_grammarParser.Arith_exprContext,0)


        def bool_expr(self):
            return self.getTypedRuleContext(small_grammarParser.Bool_exprContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = small_grammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.arith_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.bool_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noprnd(self):
            return self.getTypedRuleContext(small_grammarParser.NoprndContext,0)


        def bin_math_op(self):
            return self.getTypedRuleContext(small_grammarParser.Bin_math_opContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_arith_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_expr" ):
                return visitor.visitArith_expr(self)
            else:
                return visitor.visitChildren(self)




    def arith_expr(self):

        localctx = small_grammarParser.Arith_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arith_expr)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.noprnd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.bin_math_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boprnd(self):
            return self.getTypedRuleContext(small_grammarParser.BoprndContext,0)


        def rel_op(self):
            return self.getTypedRuleContext(small_grammarParser.Rel_opContext,0)


        def bin_logic_op(self):
            return self.getTypedRuleContext(small_grammarParser.Bin_logic_opContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_bool_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr" ):
                return visitor.visitBool_expr(self)
            else:
                return visitor.visitChildren(self)




    def bool_expr(self):

        localctx = small_grammarParser.Bool_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bool_expr)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.boprnd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.rel_op()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.bin_logic_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_math_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # NoprndContext
            self.right = None # NoprndContext

        def math_op(self):
            return self.getTypedRuleContext(small_grammarParser.Math_opContext,0)


        def noprnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.NoprndContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.NoprndContext,i)


        def getRuleIndex(self):
            return small_grammarParser.RULE_bin_math_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_math_op" ):
                return visitor.visitBin_math_op(self)
            else:
                return visitor.visitChildren(self)




    def bin_math_op(self):

        localctx = small_grammarParser.Bin_math_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bin_math_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            localctx.left = self.noprnd()
            self.state = 68
            self.math_op()
            self.state = 69
            localctx.right = self.noprnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # NoprndContext
            self.right = None # NoprndContext

        def logic_op(self):
            return self.getTypedRuleContext(small_grammarParser.Logic_opContext,0)


        def noprnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.NoprndContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.NoprndContext,i)


        def getRuleIndex(self):
            return small_grammarParser.RULE_bin_logic_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_logic_op" ):
                return visitor.visitBin_logic_op(self)
            else:
                return visitor.visitChildren(self)




    def bin_logic_op(self):

        localctx = small_grammarParser.Bin_logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bin_logic_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            localctx.left = self.noprnd()
            self.state = 72
            self.logic_op()
            self.state = 73
            localctx.right = self.noprnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # BoprndContext
            self.right = None # BoprndContext

        def nop(self):
            return self.getTypedRuleContext(small_grammarParser.NopContext,0)


        def boprnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.BoprndContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.BoprndContext,i)


        def getRuleIndex(self):
            return small_grammarParser.RULE_rel_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = small_grammarParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rel_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            localctx.left = self.boprnd()
            self.state = 76
            self.nop()
            self.state = 77
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
            return self.getToken(small_grammarParser.IDENTIFIER, 0)

        def NUM(self):
            return self.getToken(small_grammarParser.NUM, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_noprnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoprnd" ):
                return visitor.visitNoprnd(self)
            else:
                return visitor.visitChildren(self)




    def noprnd(self):

        localctx = small_grammarParser.NoprndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_noprnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
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
            return self.getToken(small_grammarParser.IDENTIFIER, 0)

        def TRUE(self):
            return self.getToken(small_grammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(small_grammarParser.FALSE, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_boprnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoprnd" ):
                return visitor.visitBoprnd(self)
            else:
                return visitor.visitChildren(self)




    def boprnd(self):

        localctx = small_grammarParser.BoprndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_boprnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(small_grammarParser.COMMA)
            else:
                return self.getToken(small_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return small_grammarParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = small_grammarParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.expr()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 84
                self.match(small_grammarParser.COMMA)
                self.state = 85
                self.expr()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(small_grammarParser.IDENTIFIER, 0)

        def LPAR(self):
            return self.getToken(small_grammarParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(small_grammarParser.RPAR, 0)

        def expr_list(self):
            return self.getTypedRuleContext(small_grammarParser.Expr_listContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = small_grammarParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(small_grammarParser.IDENTIFIER)
            self.state = 92
            self.match(small_grammarParser.LPAR)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0):
                self.state = 93
                self.expr_list()


            self.state = 96
            self.match(small_grammarParser.RPAR)
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

        def assign_stmt(self):
            return self.getTypedRuleContext(small_grammarParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(small_grammarParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(small_grammarParser.While_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(small_grammarParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = small_grammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.assign_stmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.if_stmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.while_stmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.return_stmt()
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


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(small_grammarParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(small_grammarParser.EQUAL, 0)

        def SEMICOLON(self):
            return self.getToken(small_grammarParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(small_grammarParser.ExprContext,0)


        def func_call(self):
            return self.getTypedRuleContext(small_grammarParser.Func_callContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = small_grammarParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(small_grammarParser.IDENTIFIER)
            self.state = 105
            self.match(small_grammarParser.EQUAL)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 106
                self.expr()
                pass

            elif la_ == 2:
                self.state = 107
                self.func_call()
                pass


            self.state = 110
            self.match(small_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.if_body = None # SequenceContext
            self.else_body = None # SequenceContext

        def IF(self):
            return self.getToken(small_grammarParser.IF, 0)

        def LPAR(self):
            return self.getToken(small_grammarParser.LPAR, 0)

        def bool_expr(self):
            return self.getTypedRuleContext(small_grammarParser.Bool_exprContext,0)


        def RPAR(self):
            return self.getToken(small_grammarParser.RPAR, 0)

        def ELSE(self):
            return self.getToken(small_grammarParser.ELSE, 0)

        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.SequenceContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.SequenceContext,i)


        def getRuleIndex(self):
            return small_grammarParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = small_grammarParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(small_grammarParser.IF)
            self.state = 113
            self.match(small_grammarParser.LPAR)
            self.state = 114
            self.bool_expr()
            self.state = 115
            self.match(small_grammarParser.RPAR)
            self.state = 116
            localctx.if_body = self.sequence()
            self.state = 117
            self.match(small_grammarParser.ELSE)
            self.state = 118
            localctx.else_body = self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.while_body = None # SequenceContext

        def WHILE(self):
            return self.getToken(small_grammarParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(small_grammarParser.LPAR, 0)

        def bool_expr(self):
            return self.getTypedRuleContext(small_grammarParser.Bool_exprContext,0)


        def RPAR(self):
            return self.getToken(small_grammarParser.RPAR, 0)

        def sequence(self):
            return self.getTypedRuleContext(small_grammarParser.SequenceContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = small_grammarParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(small_grammarParser.WHILE)
            self.state = 121
            self.match(small_grammarParser.LPAR)
            self.state = 122
            self.bool_expr()
            self.state = 123
            self.match(small_grammarParser.RPAR)
            self.state = 124
            localctx.while_body = self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(small_grammarParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(small_grammarParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(small_grammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = small_grammarParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(small_grammarParser.RETURN)
            self.state = 127
            self.expr()
            self.state = 128
            self.match(small_grammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.StmtContext,i)


        def getRuleIndex(self):
            return small_grammarParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = small_grammarParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435498) != 0):
                self.state = 130
                self.stmt()
                self.state = 135
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
            return self.getTypedRuleContext(small_grammarParser.StmtContext,0)


        def LBRACE(self):
            return self.getToken(small_grammarParser.LBRACE, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(small_grammarParser.Stmt_listContext,0)


        def RBRACE(self):
            return self.getToken(small_grammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_sequence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = small_grammarParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sequence)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(small_grammarParser.LBRACE)
                self.state = 138
                self.stmt_list()
                self.state = 139
                self.match(small_grammarParser.RBRACE)
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


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.FunctionContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.FunctionContext,i)


        def getRuleIndex(self):
            return small_grammarParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = small_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 143
                self.function()
                self.state = 148
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
            return self.getToken(small_grammarParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(small_grammarParser.IDENTIFIER, 0)

        def LPAR(self):
            return self.getToken(small_grammarParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(small_grammarParser.RPAR, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(small_grammarParser.Stmt_listContext,0)


        def param_list(self):
            return self.getTypedRuleContext(small_grammarParser.Param_listContext,0)


        def getRuleIndex(self):
            return small_grammarParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = small_grammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(small_grammarParser.FUNCTION)
            self.state = 150
            self.match(small_grammarParser.IDENTIFIER)
            self.state = 151
            self.match(small_grammarParser.LPAR)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 152
                self.param_list()


            self.state = 155
            self.match(small_grammarParser.RPAR)
            self.state = 156
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(small_grammarParser.ParamContext)
            else:
                return self.getTypedRuleContext(small_grammarParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(small_grammarParser.COMMA)
            else:
                return self.getToken(small_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return small_grammarParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = small_grammarParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.param()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 159
                self.match(small_grammarParser.COMMA)
                self.state = 160
                self.param()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(small_grammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return small_grammarParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = small_grammarParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(small_grammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





