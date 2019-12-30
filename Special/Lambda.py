# Lambda -- Parse tree node strategy for printing the special form lambda

from Special import Special
import sys
class Lambda(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self, parent):
        self.parent = parent
        pass

    def print(self, t, n, p):
         # TODO: Implement this function.
        if not p:
            sys.stdout.write(n*' ')
            sys.stdout.write("(")
        self.parent.getCar().print(0)
        if not self.parent.getCdr().isNull():
            sys.stdout.write(' ')
            c = self.parent.getCdr().getCar()
            c.print(0)
            c = self.parent.getCdr().getCdr()
            sys.stdout.write("\n")
            indent = n+4
            while not c.isNull():
                c.getCar().print(indent)
                sys.stdout.write('\n')
                c = c.getCdr()
        if not p:
            sys.stdout.write(n*' ')
            sys.stdout.write(")") #backspace to eliminate trailing space
        pass
