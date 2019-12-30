# Scanner -- The lexical analyzer for the Scheme printer and interpreter

import sys
import io
from Tokens import *

class Scanner:
    extended_chars = ['!', '$', '%', '&', '*', '+', '-', '.', '/', ':', '<', '=', '>', '?', '@', '^', '_', '~']

    def __init__(self, i):
        self.In = i
        self.buf = []
        self.ch_buf = None

    def read(self):
        if self.ch_buf == None:
            return self.In.read(1)
        else:
            ch = self.ch_buf
            self.ch_buf = None
            return ch
    
    def peek(self):
        if self.ch_buf == None:
            self.ch_buf = self.In.read(1)
            return self.ch_buf
        else:
            return self.ch_buf

    @staticmethod
    def isDigit(ch):
        return ch >= '0' and ch <= '9'

    whitespace = [" ", "\t", "\n", "\r"]
    def getNextToken(self):
        try:
            # It would be more efficient if we'd maintain our own
            # input buffer for a line and read characters out of that
            # buffer, but reading individual characters from the
            # input stream is easier.

            #skip the whitespace and comments
            ch = self.read()

            while ch in self.whitespace or ch == ';':
                if ch in self.whitespace:
                    ch = self.read()
                else: 
                    ch = self.read()
                    while ch != "\n":
                        ch = self.read()
                    ch = self.read() #this gets character after end of line
             # Return None on EOFch.
            #if this doesn't work, change it to if not self.buf: return none
            if ch == "":
                return None


    
            # Special characters
            elif ch == '\'':
                return Token(TokenType.QUOTE)
            elif ch == '(':
                return Token(TokenType.LPAREN)
            elif ch == ')':
                return Token(TokenType.RPAREN)
            elif ch == '.':
                #  We ignore the special identifier `...'.
                return Token(TokenType.DOT)

            # Boolean constants
            elif ch == '#':
                ch = self.read()

                if ch == 't':
                    return Token(TokenType.TRUE)
                elif ch == 'f':
                    return Token(TokenType.FALSE)
                elif ch == "":
                    sys.stderr.write("Unexpected EOF following #\n")
                    return None
                else:
                    sys.stderr.write("Illegal character '" +
                                     chr(ch) + "' following #\n")
                    return self.getNextToken()

            # String constants
            elif ch == '"':
                self.buf = []
                # TODO: scan a string into the buffer variable buf(complete)
                nextCh = self.peek()
                while nextCh != '"':
                    self.buf += nextCh
                    nextCh = self.read()
                    nextCh = self.peek()
                nextCh = self.read() #discard last "
                return StrToken("".join(self.buf).lower())

            # Integer constants
            elif self.isDigit(ch):
                buf = ch
                nextCh = self.peek()
                while self.isDigit(nextCh):
                    buf += nextCh
                    nextCh = self.read()
                    nextCh = self.peek()
                i = int(buf)


                #i = ord(ch) - ord('0')

                # make sure that the character following the integer
                # is not removed from the input stream
                return IntToken(i)
    
            # Identifiers
            elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or ch in self.extended_chars:
                # or ch is some other vaid first character
                # for an identifier
                self.buf = []
                # TODO: scan an identifier into the buffer variable buf
                self.buf.append(ch)
                ch = self.peek()
                while ch not in self.whitespace and ch != ")" and ch != ";":
                    self.buf.append(ch)
                    self.read()
                    ch = self.peek()

                # make sure that the character following the identifier
                # is not removed from the input stream
                return IdentToken("".join(self.buf).lower())

            # Illegal character
            else:
                sys.stderr.write("Illegal input character '" + ch + "'\n")
                return self.getNextToken()

        except IOError:
            sys.stderr.write("IOError: error reading input file\n")
            return None


if __name__ == "__main__":
    scanner = Scanner(sys.stdin)
    tok = scanner.getNextToken()
    tt = tok.getType()
    print(tt)
    if tt == TokenType.INT:
        print(tok.getIntVal())
