# Define -- Parse tree node strategy for printing the special form define

from Special import Special
import sys
class Define(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self, parent):
        self.parent = parent
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        if self.parent.getCdr() is not None and self.parent.getCdr().getCar() is not None:
            if not self.parent.getCdr().getCar().isPair():
                #use regular form
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
            else:
                #use if/lambda form
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
                    sys.stdout.write(")")
        pass
