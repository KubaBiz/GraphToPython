import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
#from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.start_()
    print(input_stream)
    print(lexer)
    for token in stream.tokens:
        print(token, end=" ")
    print(parser)

if __name__ == '__main__':
    main(sys.argv)