# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys
from Tokens import TokenType, IdentToken, Token
from Tree import *
from Special import *

class Parser:
    def __init__(self, s, treeBuilder):
        self.scanner = s
        self.treeBuilder = treeBuilder
    def clearTree(self):
        self.treeBuilder.clearTree()
    def parseExp(self, token = None, tree=None):
        # TODO: write code for parsing an exp
        if tree is None:
            tree = self.treeBuilder
        if token is None:
            token = self.scanner.getNextToken()
        if token is None:
            return tree.getTree()
        if token.getType() is TokenType.LPAREN:
            return self.parseRest(tree)
        elif token.getType() is TokenType.QUOTE:
            subTree = TreeBuilder()
            tree.addNode(Cons(None, None))
            tree.addNode(Ident("quote"))
            tree.addNode(Cons(None,None))
            tree.addNode(self.parseExp(tree=subTree))
            tree.addNode(Nil.getInstance())
            return tree.getTree()
        elif token.getType() is TokenType.TRUE:
            return BoolLit.getInstance(True)
        elif token.getType() is TokenType.FALSE:
            return BoolLit.getInstance(False)
        elif token.getType() == TokenType.INT:
            return IntLit(token.intVal)
        elif token.getType() == TokenType.STR:
            return StrLit(token.strVal)
        else:
            return Ident(token.getName())
    


    def parseRest(self, tree,token = None):
        if token is None:
            token = self.scanner.getNextToken()
        if token is None:
            return tree.getTree()
        if token.getType() is TokenType.RPAREN:
            return Nil.getInstance()
        else:
            tree.addNode(Cons(None,None))
            subTree = TreeBuilder()
            tree.addNode(self.parseExp(token=token, tree=subTree))
            nextTok = self.scanner.getNextToken()
            if nextTok.getType() is TokenType.DOT:
                subTreeTwo = TreeBuilder()
                tree.addNode(self.parseExp(tree=subTreeTwo))
                throwaway = self.scanner.getNextToken() #toss out trailing )
                return tree.getTree()
            else:
                tree.addNode(self.parseRest(token=nextTok, tree=tree))
                return tree.getTree()
        # TODO: write code for parsing a rest
    # TODO: Add any additional methods you might need

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
