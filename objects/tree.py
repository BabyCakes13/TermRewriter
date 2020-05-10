import node


class TermTree:
    """
    This will be the tree representation of a given expression.
    """

    def __init__(self, expression):
        self.expression = expression

        self.delimitators = {
        '(': self.handleOpenBracket,
        ',': self.handleComma,
        ')': self.handleClosedBracket
        }

        self.root = None
        self.current = None

        self.parseExpression()

    def parseExpression(self):
        content = ""

        for i, character in enumerate(self.expression):
            if character in self.delimitators.keys():
                self.delimitators[character](content, i)
                content = ""
            else:
                content = content + character

        if len(content) > 0 and self.root is None:
            # for the case when the expression has no delimitators
            self.handleNewTerm(content, i)

        if self.current is not None:
            print ("Current", self.current)
            print ("Root", self.root)

            # If parsing stops at a node which is not the root, then it did not close all the parentheses / did not make its way back to the top.
            print("Invalid expression. Try closing all parentheses.")
            return False

    def handleNewTerm(self, content, i):
        # PS. this also treats the case when there is only one item: s = x
        if len(content) == 0:
            print("Empty item found at position %d" % i)
            return

        new_node = node.Node(content, self.current)
        self.setRoot(new_node)

        return new_node

    def handleOpenBracket(self, content, i):
        new_node = self.handleNewTerm(content, i)

        if self.current:
            self.current.adoptChild(new_node)

        self.current = new_node

    def handleComma(self, content, i):
        if content:
            new_node = node.Node(content, self.current)
            self.current.adoptChild(new_node)

    def handleClosedBracket(self, content, i):
        if content:
            new_node = node.Node(content, self.current)
            self.current.adoptChild(new_node)

        if self.current:
            self.current = self.current.parent
        else:
            # If current becomes null after the parsing, then there were too many parentheses opened.
            print("Too many parantheses closed at position %d" % i)
            return False

    def substitute(self, substitutionMap):
        self.substituteFromNode(substitutionMap, self.root)

    def substituteFromNode(self, substitutionMap, node):
        if node.content in substitutionMap.keys():
            foundSubstitution = substitutionMap[node.content]

            print ("replacing ", node.content, node, " with ", foundSubstitution)

            substitutionTree = TermTree(foundSubstitution)
            substitutionTree.printTree()
            substitutionTree.printExpression()

            nodePosition = node.parent.children.index(node)
            node.parent.children[nodePosition] = substitutionTree.getRoot()
            node.parent.children[nodePosition].parent = node.parent
        else:
            for child in node.children:
                self.substituteFromNode(substitutionMap, child)

    def setRoot(self, node):
        if self.root is None:
            self.root = node

    def printTree(self):
        if self.root:
            print(self.root.treeString(True))
        else:
            print("There is no root.")

    def printExpression(self):
        if self.root:
            print(self.root.expressionString())
        else:
            print("There is no root.")

    def validateTerm(self, term):
        """
        Function which checks whether a string is a term based on whether it appears in the arity map or if it is formed of only letters.
        """
        if term.isalpha():
            if term in self.arityMap.keys():
                print("This is a term.")
            else:
                print("This is a variable.")
        else:
            print("This is not a term because it is not a valid term name.")

    def getRoot(self) -> str:
        if self.root:
            return self.root
        else:
            print("No root set.")


if __name__=="__main__":
    #expression = "f(e,x,y)"
    expression = "f1(f2(x,f3(i(f4(x,f5(H,j))),e(i(x),Y))))"

    substitutionMap = {
    "x": "m(y)",
    "Y": "blabla"
    }

    expressionTree = TermTree(expression)
    print("BREFORE...\n")
    expressionTree.printTree()

    expressionTree.substitute(substitutionMap)

    print("AFTER...\n")
    expressionTree.printTree()

    # first_child = root.children[0]
    # print(first_child.treeString(True))

    # print("------------------------------")
    # print(test.root.children[0].position)
    # print("------------------------------")

    # test.validateTerm('f')
    # test.validateTerm('g')
    # test.validateTerm('0')
    # test.validateTerm('/')

    # test.parseExpression()
    # test.setRoot('f')
    # test.parseExpression()
    # print(test.getRoot())

    # self.expression = "f1(f2(x,f3(i(f4(x,f5(H,j))),e(i(x),Y))))"
    # self.arityMap = {'f': 2, 'i': 1, 'e': 2, 'j': 0}
    # self.expression = "f(g(h(j("
    # self.expression = "x"
