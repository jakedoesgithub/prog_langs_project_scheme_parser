# Regular -- Parse tree node strategy for printing regular lists

from Special import Special
from Tree import Cons, Node
import sys
class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self, parent):
        self.parent = parent

    def print(self, t, n, p):
        # TODO: Implement this function.
        #Special forms store the parent, which is going to always be a Cons() object, so we can safely reach into the parent
        if not p:
            sys.stdout.write(n*' ')
            sys.stdout.write("(")
        if self.parent.getCdr().isNull():
            self.parent.getCar().print(0)
        else:
            self.parent.getCar().print(0)
            sys.stdout.write(' ')
            if not self.parent.getCdr().isPair():
                sys.stdout.write(". ")
                self.parent.getCdr().print(0, p=True)
            else:
                self.parent.getCdr().print(n, p=True)
        if not p:
            sys.stdout.write(")") #backspace to eliminate trailing space
        pass
