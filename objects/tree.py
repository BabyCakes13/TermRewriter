import node


class TermTree:
    """
    This will be the tree representation of a given expression.
    """

    def __init__(self):
        # self.expression = "f1(f2(x,f3(i(f4(x,f5(H,j))),e(i(x),Y))))"
        # self.arityMap = {'f': 2, 'i': 1, 'e': 2, 'j': 0}
        # self.expression = "f(g(h(j("
        # self.expression = "x"

        self.expression = "f(e,x)"

        self.substitutionMap = {
        "x": "i(y)"
        }

        self.delimitators = {
        '(': self.handleOpenBracket,
        ',': self.handleComma,
        ')': self.handleClosedBracket
        }

        self.root = None
        self.current = None

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
            self.handleOpenBracket(content)

        if self.current != self.root:
            # If parsing stops at a node which is not the root, then it did not close all the parentheses / did not make its way back to the top.
            print("Invalid expression. Try closing all parentheses.")
            return False

    def handleOpenBracket(self, content, i):
        if len(content) == 0:
            print("Empty item found at position %d" % i)
            return

        new_node = node.Node(content, self.current)

        if self.current:
            self.current.adoptChild(new_node)

        self.current = new_node
        self.setRoot(new_node)

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

    def setRoot(self, node):
        if self.root is None:
            self.root = node

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
    test = TermTree()
    test.parseExpression()
    root = test.getRoot()
    # print(root.content)
    if root:
        print(root.treeString(True))
    else:
        print("No root.")

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
