# Quote -- Parse tree node strategy for printing the special form quote

from Special import Special
import sys
class Quote(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self, parent):
        self.parent = parent

    def print(self, t, n, p):
        # TODO: Implement this function.
        sys.stdout.write(n*" ")
        sys.stdout.write("'")
        #self.parent.getCar().print(n)
        if self.parent.getCdr().getCdr().isNull():
            self.parent.getCdr().print(n, p=True)
        else:
            self.parent.getCdr().print(n)
        pass
