# Generated from Graphs.g4 by ANTLR 4.13.1
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
        4,1,11,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,1,0,
        3,0,43,8,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,3,1,
        3,3,3,58,8,3,1,4,1,4,1,4,1,4,3,4,64,8,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,76,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,
        8,1,9,1,9,3,9,90,8,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,110,8,14,10,14,
        12,14,113,9,14,1,14,1,14,1,15,1,15,3,15,119,8,15,1,16,1,16,1,17,
        1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        0,0,116,0,42,1,0,0,0,2,50,1,0,0,0,4,52,1,0,0,0,6,57,1,0,0,0,8,63,
        1,0,0,0,10,75,1,0,0,0,12,77,1,0,0,0,14,81,1,0,0,0,16,85,1,0,0,0,
        18,89,1,0,0,0,20,91,1,0,0,0,22,94,1,0,0,0,24,97,1,0,0,0,26,100,1,
        0,0,0,28,104,1,0,0,0,30,118,1,0,0,0,32,120,1,0,0,0,34,122,1,0,0,
        0,36,37,3,20,10,0,37,38,3,4,2,0,38,39,5,1,0,0,39,40,3,2,1,0,40,43,
        1,0,0,0,41,43,1,0,0,0,42,36,1,0,0,0,42,41,1,0,0,0,43,1,1,0,0,0,44,
        45,3,20,10,0,45,46,3,4,2,0,46,47,5,1,0,0,47,48,3,2,1,0,48,51,1,0,
        0,0,49,51,1,0,0,0,50,44,1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,53,
        3,8,4,0,53,54,3,6,3,0,54,5,1,0,0,0,55,58,3,10,5,0,56,58,1,0,0,0,
        57,55,1,0,0,0,57,56,1,0,0,0,58,7,1,0,0,0,59,60,3,22,11,0,60,61,3,
        8,4,0,61,64,1,0,0,0,62,64,1,0,0,0,63,59,1,0,0,0,63,62,1,0,0,0,64,
        9,1,0,0,0,65,66,3,22,11,0,66,67,3,10,5,0,67,76,1,0,0,0,68,69,3,12,
        6,0,69,70,3,10,5,0,70,76,1,0,0,0,71,72,3,14,7,0,72,73,3,10,5,0,73,
        76,1,0,0,0,74,76,1,0,0,0,75,65,1,0,0,0,75,68,1,0,0,0,75,71,1,0,0,
        0,75,74,1,0,0,0,76,11,1,0,0,0,77,78,3,24,12,0,78,79,3,28,14,0,79,
        80,5,1,0,0,80,13,1,0,0,0,81,82,3,26,13,0,82,83,3,28,14,0,83,84,5,
        1,0,0,84,15,1,0,0,0,85,86,5,9,0,0,86,17,1,0,0,0,87,90,3,34,17,0,
        88,90,3,16,8,0,89,87,1,0,0,0,89,88,1,0,0,0,90,19,1,0,0,0,91,92,5,
        2,0,0,92,93,3,16,8,0,93,21,1,0,0,0,94,95,5,3,0,0,95,96,3,16,8,0,
        96,23,1,0,0,0,97,98,5,4,0,0,98,99,3,16,8,0,99,25,1,0,0,0,100,101,
        5,5,0,0,101,102,3,16,8,0,102,103,3,16,8,0,103,27,1,0,0,0,104,111,
        5,6,0,0,105,106,3,16,8,0,106,107,5,7,0,0,107,108,3,30,15,0,108,110,
        1,0,0,0,109,105,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,
        1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,115,5,8,0,0,115,29,1,
        0,0,0,116,119,3,34,17,0,117,119,3,16,8,0,118,116,1,0,0,0,118,117,
        1,0,0,0,119,31,1,0,0,0,120,121,5,1,0,0,121,33,1,0,0,0,122,123,5,
        10,0,0,123,35,1,0,0,0,8,42,50,57,63,75,89,111,118
    ]

class GraphsParser ( Parser ):

    grammarFileName = "Graphs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'end'", "'graph'", "'add vertex'", "'modify'", 
                     "'set edge'", "'['", "':'", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "White_spaces" ]

    RULE_s = 0
    RULE_g = 1
    RULE_a = 2
    RULE_aa = 3
    RULE_w = 4
    RULE_k = 5
    RULE_m = 6
    RULE_e = 7
    RULE_name = 8
    RULE_value = 9
    RULE_graph = 10
    RULE_vertex = 11
    RULE_modify = 12
    RULE_edge = 13
    RULE_attributes = 14
    RULE_choose = 15
    RULE_end = 16
    RULE_liczba = 17

    ruleNames =  [ "s", "g", "a", "aa", "w", "k", "m", "e", "name", "value", 
                   "graph", "vertex", "modify", "edge", "attributes", "choose", 
                   "end", "liczba" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    INT=10
    White_spaces=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graph(self):
            return self.getTypedRuleContext(GraphsParser.GraphContext,0)


        def a(self):
            return self.getTypedRuleContext(GraphsParser.AContext,0)


        def g(self):
            return self.getTypedRuleContext(GraphsParser.GContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = GraphsParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.graph()
                self.state = 37
                self.a()
                self.state = 38
                self.match(GraphsParser.T__0)
                self.state = 39
                self.g()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

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


    class GContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graph(self):
            return self.getTypedRuleContext(GraphsParser.GraphContext,0)


        def a(self):
            return self.getTypedRuleContext(GraphsParser.AContext,0)


        def g(self):
            return self.getTypedRuleContext(GraphsParser.GContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_g

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterG" ):
                listener.enterG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitG" ):
                listener.exitG(self)




    def g(self):

        localctx = GraphsParser.GContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_g)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.graph()
                self.state = 45
                self.a()
                self.state = 46
                self.match(GraphsParser.T__0)
                self.state = 47
                self.g()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

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


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def w(self):
            return self.getTypedRuleContext(GraphsParser.WContext,0)


        def aa(self):
            return self.getTypedRuleContext(GraphsParser.AaContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)




    def a(self):

        localctx = GraphsParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_a)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.w()
            self.state = 53
            self.aa()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def k(self):
            return self.getTypedRuleContext(GraphsParser.KContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_aa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAa" ):
                listener.enterAa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAa" ):
                listener.exitAa(self)




    def aa(self):

        localctx = GraphsParser.AaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_aa)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.k()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex(self):
            return self.getTypedRuleContext(GraphsParser.VertexContext,0)


        def w(self):
            return self.getTypedRuleContext(GraphsParser.WContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_w

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterW" ):
                listener.enterW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitW" ):
                listener.exitW(self)




    def w(self):

        localctx = GraphsParser.WContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_w)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.vertex()
                self.state = 60
                self.w()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex(self):
            return self.getTypedRuleContext(GraphsParser.VertexContext,0)


        def k(self):
            return self.getTypedRuleContext(GraphsParser.KContext,0)


        def m(self):
            return self.getTypedRuleContext(GraphsParser.MContext,0)


        def e(self):
            return self.getTypedRuleContext(GraphsParser.EContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterK" ):
                listener.enterK(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitK" ):
                listener.exitK(self)




    def k(self):

        localctx = GraphsParser.KContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_k)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.vertex()
                self.state = 66
                self.k()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.m()
                self.state = 69
                self.k()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.e()
                self.state = 72
                self.k()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)

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


    class MContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modify(self):
            return self.getTypedRuleContext(GraphsParser.ModifyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(GraphsParser.AttributesContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_m

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterM" ):
                listener.enterM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitM" ):
                listener.exitM(self)




    def m(self):

        localctx = GraphsParser.MContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_m)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.modify()
            self.state = 78
            self.attributes()
            self.state = 79
            self.match(GraphsParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edge(self):
            return self.getTypedRuleContext(GraphsParser.EdgeContext,0)


        def attributes(self):
            return self.getTypedRuleContext(GraphsParser.AttributesContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)




    def e(self):

        localctx = GraphsParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_e)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.edge()
            self.state = 82
            self.attributes()
            self.state = 83
            self.match(GraphsParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphsParser.ID, 0)

        def getRuleIndex(self):
            return GraphsParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = GraphsParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(GraphsParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def liczba(self):
            return self.getTypedRuleContext(GraphsParser.LiczbaContext,0)


        def name(self):
            return self.getTypedRuleContext(GraphsParser.NameContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = GraphsParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.liczba()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.name()
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


    class GraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(GraphsParser.NameContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_graph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph" ):
                listener.enterGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph" ):
                listener.exitGraph(self)




    def graph(self):

        localctx = GraphsParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_graph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(GraphsParser.T__1)
            self.state = 92
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VertexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(GraphsParser.NameContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_vertex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertex" ):
                listener.enterVertex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertex" ):
                listener.exitVertex(self)




    def vertex(self):

        localctx = GraphsParser.VertexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vertex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GraphsParser.T__2)
            self.state = 95
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(GraphsParser.NameContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_modify

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModify" ):
                listener.enterModify(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModify" ):
                listener.exitModify(self)




    def modify(self):

        localctx = GraphsParser.ModifyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_modify)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(GraphsParser.T__3)
            self.state = 98
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphsParser.NameContext)
            else:
                return self.getTypedRuleContext(GraphsParser.NameContext,i)


        def getRuleIndex(self):
            return GraphsParser.RULE_edge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge" ):
                listener.enterEdge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge" ):
                listener.exitEdge(self)




    def edge(self):

        localctx = GraphsParser.EdgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_edge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(GraphsParser.T__4)
            self.state = 101
            self.name()
            self.state = 102
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphsParser.NameContext)
            else:
                return self.getTypedRuleContext(GraphsParser.NameContext,i)


        def choose(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphsParser.ChooseContext)
            else:
                return self.getTypedRuleContext(GraphsParser.ChooseContext,i)


        def getRuleIndex(self):
            return GraphsParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)




    def attributes(self):

        localctx = GraphsParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GraphsParser.T__5)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 105
                self.name()
                self.state = 106
                self.match(GraphsParser.T__6)
                self.state = 107
                self.choose()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(GraphsParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChooseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def liczba(self):
            return self.getTypedRuleContext(GraphsParser.LiczbaContext,0)


        def name(self):
            return self.getTypedRuleContext(GraphsParser.NameContext,0)


        def getRuleIndex(self):
            return GraphsParser.RULE_choose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChoose" ):
                listener.enterChoose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChoose" ):
                listener.exitChoose(self)




    def choose(self):

        localctx = GraphsParser.ChooseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_choose)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.liczba()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.name()
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


    class EndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GraphsParser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)




    def end(self):

        localctx = GraphsParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(GraphsParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiczbaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GraphsParser.INT, 0)

        def getRuleIndex(self):
            return GraphsParser.RULE_liczba

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiczba" ):
                listener.enterLiczba(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiczba" ):
                listener.exitLiczba(self)




    def liczba(self):

        localctx = GraphsParser.LiczbaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_liczba)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(GraphsParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





