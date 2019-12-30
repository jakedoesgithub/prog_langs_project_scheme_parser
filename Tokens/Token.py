# Token -- Base class for Token objects

from Tokens import TokenType

class Token:
    def __init__(self, t):
        self.tt = t

    def getType(self):
        return self.tt

    def print(self, x):
        if (self.tt == TokenType.QUOTE):
            print("'")
        elif self.tt == TokenType.LPAREN:
            print("(")
        elif self.tt == TokenType.RPAREN:
            print(")")
        elif self.tt == TokenType.DOT:
            print(".")
        elif self.tt == TokenType.TRUE:
            print("#t")
        elif self.tt == TokenType.FALSE:
            print("#f")


if __name__ == "__main__":
    tok = Token(TokenType.DOT)
    print(tok.getType())
