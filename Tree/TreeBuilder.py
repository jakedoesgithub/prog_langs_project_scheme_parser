from Tree import BoolLit, Cons, Ident, IntLit, Nil, Node, StrLit
class TreeBuilder:
    
    def __init__(self):
        self.root = None
        self.subroot = self.root

    #TODO: implement currentNode
    def addNode(self, node):
        if self.subroot is None:
            if self.root is None:
                self.root = node
                if node.isPair():
                    self.root.setParent(None)
                    self.subroot = node
        else:
            if self.subroot.isPair():
                if self.subroot.getCar() is None:
                    self.subroot.setCar(node)
                    if node.isPair():
                        node.setParent(self.subroot)
                        self.subroot = node
                elif self.subroot.getCdr() is None:
                    self.subroot.setCdr(node)
                    if node.isPair():
                        node.setParent(self.subroot)
                        self.subroot = node 
                    while self.subroot is not None and self.subroot.getCar() is not None and self.subroot.getCdr() is not None:
                        self.subroot = self.subroot.getParent()
        while self.subroot is not None and self.subroot.getCar() is not None and self.subroot.getCdr() is not None:
            self.subroot = self.subroot.getParent()

    def getTree(self):
        return self.root
    def getSubTree(self):
        return self.subroot
    def clearTree(self):
        self.root = None
        self.subroot = None
    