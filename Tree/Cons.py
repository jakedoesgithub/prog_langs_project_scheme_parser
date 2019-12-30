# Cons -- Parse tree node class for representing a Cons node

from Tree import Node
from Tree import Ident
from Special import *
import sys
class Cons(Node):
    def __init__(self, a, d, specialForm = None):
        self.car = a
        self.cdr = d
        #These are to trigger code in setCar() and setCdr() if a and d were actual values
        if not a is None:
            self.setCar(a)
        if not a is None:
            self.setCdr(d)
        if specialForm is None:
            self.form = Regular(self)
        else:
            if specialForm == "quote":
                self.form = Quote(self)
            elif specialForm == "begin":
                self.form = Begin(self)
        # self.parseList() TODO: is this method needed?

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.
    def parseList(self):
        # TODO: implement this function and any helper functions
        # you might need
        if self.car.isSymbol():
            if self.car.getName() == "quote":
                self.form = Quote(self)
            elif self.car.getName() == "begin":
                self.form = Begin(self)
            elif self.car.getName() == "if":
                self.form = If(self)
            elif self.car.getName() == "lambda":
                self.form = Lambda(self)
            elif self.car.getName() == "let":
                self.form = Let(self)
            elif self.car.getName() == "cond":
                self.form = Cond(self)
            elif self.car.getName() == "define":
                self.form = Define(self) #TODO: write code for Define

    def print(self, n, p=False):
        if self.form is None:
            self.car.print(n)
            self.cdr.print(n)
        else:
            self.form.print(self, n, p)

    def isPair(self):
        return True
    def getCar(self):
        return self.car
    def getCdr(self):
        return self.cdr

    #TODO: parseList() needs to be called in setcar
    def setCar(self, node):
        self.car = node
        self.parseList()
    def setCdr(self, node):
        self.cdr = node 
    def setParent(self, node):
        self.parent = node
    def getParent(self):
        return self.parent


if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
