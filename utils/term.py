class Term:
    def __init__(self, root):
        self.root = root

class TermTree(Term):
    def __init__(self, root):
        super().__init__(root)

    def printTree(self, activatePosition=False):
        if self.root:
            print(self.root.treeString(activatePosition))
        else:
            print("No root set.")


class TermExpression(Term):
    def __init__(self, root):
        super().__init__(root)

    def printExpression(self, activatePosition=False):
        if self.root:
            print(self.root.expressionString(activatePosition))
        else:
            print("No root set.")
