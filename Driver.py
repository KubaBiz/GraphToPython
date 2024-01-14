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
        self.output_file.write("import matplotlib.pyplot as plt\n")
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

        if node_name not in self.available_nodes:
            self.output_file.write(f'#ERROR There is no Node to modify named \'{node_name}\'\n')
            self.visitChildren(ctx)
            return 
        attributes = [child.getText() for child in ctx.getChild(1).getChildren()][1:-1]
        attributes = list(filter(lambda x: x != ':', attributes))
        for i in range(0,len(attributes), 2):
            name, value = attributes[i], attributes[i+1]
            self.output_file.write(f'{self.current_graph}.nodes["{node_name}"]["{name}"] = "{value}"\n')

        self.visitChildren(ctx)

    def visitE(self, ctx:GraphsParser.EContext):
        node1 = ctx.getChild(0).getChild(1).getText()
        node2 = ctx.getChild(0).getChild(2).getText()
        attributes = [child.getText() for child in ctx.getChild(1).getChildren()][1:-1]
        attributes = list(filter(lambda x: x != ':', attributes))
        dictionary = {}
        for i in range(0,len(attributes), 2):
            name, value = attributes[i], attributes[i+1]
            dictionary[name] = value
        print(dictionary)
        if node1 == "*" and node2 == "*":
            for v in range(len(self.available_nodes)):
                for k in range(v+1, len(self.available_nodes)):
                    self.output_file.write(f'{self.current_graph}.add_edge("{self.available_nodes[v]}", "{self.available_nodes[k]}", **{dictionary})\n')
        elif node1 == "*" or node2 == "*":
            node = node1 if node2 == "*" else node2
            if node not in self.available_nodes:
                self.output_file.write(f'#ERROR There is no Node to add edge named \'{node}\'\n')
            else:
                for v in range(len(self.available_nodes)):
                    self.output_file.write(f'{self.current_graph}.add_edge("{node}", "{self.available_nodes[v]}", **{dictionary})\n')
        else:
            if node1 in self.available_nodes and node2 in self.available_nodes:
                self.output_file.write(f'{self.current_graph}.add_edge("{node1}", "{node2}", **{dictionary})\n')
            else:
                self.output_file.write(f'#ERROR There is no Node to add edge named \'{node1}\' or \'{node2}\'\n')
        
        self.visitChildren(ctx)

    def visitEnd_graph(self, ctx:GraphsParser.End_graphContext):
        self.output_file.write(f'nx.drawing.nx_pydot.write_dot({self.current_graph},"{self.output_path.split(".")[0]}{len(self.available_graphs)}.dot")\n')
        self.output_file.write(f'nx.draw_networkx({self.current_graph})\n')
        self.output_file.write(f'plt.show()\n\n')
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