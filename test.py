from Parser import *
from Lexer import *
from document import *

lexer = Lexer("7 + 5 - 8")
tokens = lexer.makeTokens()
parser = Parser(tokens)
AST = parser.parse()

print(AST)
