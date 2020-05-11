from objects import node
from utils import expression_parser

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

    def substitute(self, substitutionMap):
        print("\nSTARTING TO SUBSTITUTE...\n")
        self.substituteFromNode(substitutionMap, self.root)

    def substituteFromNode(self, substitutionMap, node):
        if node.content in substitutionMap.keys():
            foundSubstitution = substitutionMap[node.content]

            print ("Subsituting: {} at {} with {}\n".format(node.content, node.position, foundSubstitution))
            #print ("Found substitution: ", node.content + " at " + node.position, " with ", foundSubstitution + "\n")

            parser = expression_parser.ExpressionParser(foundSubstitution)
            parser.parseExpression()

            substitutionTree = TermTree(parser.getRoot())
            # substitutionTree.printTree()
            # substitutionTree.printExpression()

            nodePosition = node.parent.children.index(node)
            node.parent.children[nodePosition] = substitutionTree.root
            node.parent.children[nodePosition].parent = node.parent
        else:
            for child in node.children:
                self.substituteFromNode(substitutionMap, child)


class TermExpression(Term):
    def __init__(self, root):
        super().__init__(root)

    def printExpression(self, activatePosition=False):
        if self.root:
            print(self.root.expressionString(activatePosition))
        else:
            print("No root set.")
