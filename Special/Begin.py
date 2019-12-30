# Begin -- Parse tree node strategy for printing the special form begin

from Special import Special
import sys

class Begin(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self, parent):
        self.parent = parent
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        #nopte, subsequent lines in begin indented by 4 spaces each
        if not p:
            sys.stdout.write(n*' ')
            sys.stdout.write("(")
        if self.parent.getCdr().isNull():
            self.parent.getCar().print(0)
        else :
            self.parent.getCar().print(0)
            sys.stdout.write('\n')
            c = self.parent.getCdr()
            indent = n+4
            while not c.isNull():
                #sys.stdout.write(n*' ')
                c.getCar().print(indent)
                sys.stdout.write('\n')
                c = c.getCdr()
        if not p:
            sys.stdout.write(n*' ')
            sys.stdout.write(")") #backspace to eliminate trailing space
        pass
