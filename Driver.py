import sys
from antlr4 import *
from generated.GraphsLexer import GraphsLexer
from generated.GraphsParser import GraphsParser
from generated.GraphsVisitor import GraphsVisitor
from antlr4.tree.Trees import Trees
#from VisitorInterp import VisitorInterp

class CodeGenerator(GraphsVisitor):
    def __init__(self, output_path):
        # init code generator
        self.output_path = output_path
        self.output_file = open(output_path, "w")
        self.output_file.write("import networkx as nx\n")
        # self.output_file.write("\n\ndef main():\n")
        self.graph_name = None

    def visitGraph(self, ctx:GraphsParser.GraphContext):
        self.graph_name = ctx.getChild(1).getText()
        self.output_file.write(f"{self.graph_name} = nx.Graph()\n")
        self.visitChildren(ctx)

    def visitVertex(self, ctx:GraphsParser.VertexContext):
        name = ctx.getChild(1).getText()
        self.output_file.write(f'{self.graph_name}.add_node("{name}")\n')
        self.visitChildren(ctx)

    def visitM(self, ctx:GraphsParser.MContext):
        node_name = ctx.getChild(0).getChild(1).getText()
        attributes = [child.getText() for child in ctx.getChild(1).getChildren()][1:-1]
        attributes = list(filter(lambda x: x != ':', attributes))
        for i in range(0,len(attributes), 2):
            pass
        print(node_name, attributes)
        self.output_file.write(f'{self.graph_name}.add_node("")\n')
        self.visitChildren(ctx)

    def visitEnd(self, ctx:GraphsParser.EndContext):
        self.graph_name = None
def main(argv):
    input_stream = FileStream(argv[1])
    print(argv[1])
    lexer = GraphsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphsParser(stream)
    tree = parser.s()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        pass
    print(Trees.toStringTree(tree, None, parser))
    
    outputPath = argv[1].split(".")[0] + ".py"
    print(outputPath)
    visitor = CodeGenerator(outputPath)
    visitor.visit(tree)
    # code_generator = CodeGenerator()
    # result = code_generator.visit(tree)
    # print(f"Generated Python code: {result}")

if __name__ == '__main__':
    main(sys.argv)

# antlr4-parse Expr.g4 _start -tree# antlr4 -v 4.13.0 -Dlanguage=Python3 Expr.g4# python Driver.py input.txt