# Generated from generated/Graphs.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .GraphsParser import GraphsParser
else:
    from GraphsParser import GraphsParser

# This class defines a complete generic visitor for a parse tree produced by GraphsParser.

class GraphsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphsParser#s.
    def visitS(self, ctx:GraphsParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#g.
    def visitG(self, ctx:GraphsParser.GContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#a.
    def visitA(self, ctx:GraphsParser.AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#aa.
    def visitAa(self, ctx:GraphsParser.AaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#w.
    def visitW(self, ctx:GraphsParser.WContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#k.
    def visitK(self, ctx:GraphsParser.KContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#m.
    def visitM(self, ctx:GraphsParser.MContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#e.
    def visitE(self, ctx:GraphsParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#graph.
    def visitGraph(self, ctx:GraphsParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#extend.
    def visitExtend(self, ctx:GraphsParser.ExtendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#node.
    def visitNode(self, ctx:GraphsParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#modify.
    def visitModify(self, ctx:GraphsParser.ModifyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#edge.
    def visitEdge(self, ctx:GraphsParser.EdgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#attributes.
    def visitAttributes(self, ctx:GraphsParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#value.
    def visitValue(self, ctx:GraphsParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#dest_node.
    def visitDest_node(self, ctx:GraphsParser.Dest_nodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#end_graph.
    def visitEnd_graph(self, ctx:GraphsParser.End_graphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#name.
    def visitName(self, ctx:GraphsParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphsParser#number.
    def visitNumber(self, ctx:GraphsParser.NumberContext):
        return self.visitChildren(ctx)



del GraphsParser