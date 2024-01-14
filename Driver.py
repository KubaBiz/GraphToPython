import sys
from antlr4 import *
from generated.GraphsLexer import GraphsLexer
from generated.GraphsParser import GraphsParser
from generated.GraphsVisitor import GraphsVisitor
from antlr4.tree.Trees import Trees


class CodeGenerator(GraphsVisitor):
    def __init__(self, output_path):
        self.output_path = output_path
        self.output_file = open(output_path, "w")
        self.output_file.write("import networkx as nx\n")
        self.output_file.write("import copy as cp\n\n\n")
        # self.output_file.write("\n\ndef main():\n")
        self.current_graph = None
        self.available_graphs = [] # potrzebne do extends
        self.available_nodes = [] # potrzebne do tworzenia krawędzi

    def visitGraph(self, ctx:GraphsParser.GraphContext):
        self.current_graph = ctx.getChild(1).getText()
        if ctx.getChild(2).getText() != "":
            extend_graph = ctx.getChild(2).getChild(1).getText()
        else:
            extend_graph = None
        if extend_graph in self.available_graphs:
            self.output_file.write(f"{self.current_graph} = cp.deepcopy({extend_graph})\n")
        elif extend_graph != None:
            self.output_file.write(f"#ERROR No Graph to copy named \'{extend_graph}\'\n")
            self.output_file.write(f"{self.current_graph} = nx.Graph()\n")
        else:
            self.output_file.write(f"{self.current_graph} = nx.Graph()\n")
        self.available_graphs.append(self.current_graph)
        print(self.available_graphs)
        self.visitChildren(ctx)

    def visitNode(self, ctx:GraphsParser.NodeContext):
        name = ctx.getChild(1).getText()
        if name in self.available_nodes:
            self.output_file.write(f'#ERROR There is already Node named \'{name}\'\n')
        else:
            self.output_file.write(f'{self.current_graph}.add_node("{name}")\n')
            self.available_nodes.append(name)
        print(self.available_nodes)
        self.visitChildren(ctx)

    def visitM(self, ctx:GraphsParser.MContext):
        node_name = ctx.getChild(0).getChild(1).getText()
        attributes = [child.getText() for child in ctx.getChild(1).getChildren()][1:-1]
        attributes = list(filter(lambda x: x != ':', attributes))
        for i in range(0,len(attributes), 2):
            pass
        print(node_name, attributes)
        self.output_file.write(f'{self.current_graph}.add_node("")\n')
        self.visitChildren(ctx)

    def visitEnd_graph(self, ctx:GraphsParser.End_graphContext):
        self.current_graph = None
        self.available_nodes = []

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GraphsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphsParser(stream)
    tree = parser.s()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors in file " + argv[1])
    else:
        pass
    print(Trees.toStringTree(tree, None, parser)) # do usunięcia po skończeniu
    
    outputPath = argv[1].split(".")[0] + ".py"
    visitor = CodeGenerator(outputPath)
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)

# antlr4-parse Expr.g4 _start -tree# antlr4 -v 4.13.0 -Dlanguage=Python3 Expr.g4# python Driver.py input.txt