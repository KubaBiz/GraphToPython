import sys
from antlr4 import *
from GraphsLexer import GraphsLexer
from GraphsParser import GraphsParser
from antlr4.tree.Trees import Trees
#from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GraphsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphsParser(stream)
    tree = parser.s()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        pass
    print(Trees.toStringTree(tree, None, parser))
    
    # code_generator = CodeGenerator()
    # result = code_generator.visit(tree)
    # print(f"Generated Python code: {result}")

if __name__ == '__main__':
    main(sys.argv)

# antlr4-parse Expr.g4 _start -tree# antlr4 -v 4.13.0 -Dlanguage=Python3 Expr.g4# python Driver.py input.txt