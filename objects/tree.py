import node


class TermTree:
    """
    This will be the tree representation of a given expression.
    """
    def __init__(self):
        self.expression = "f1(f2(x,f3(i(f4(x,f5(H,j))),e(i(x),Y))))"
        self.arityMap = {'f': 2, 'i': 1, 'e': 2, 'j': 0}
        self.delimitators = {
        '(': self.handleOpenBracket,
        ',': self.handleComma,
        ')': self.handleClosedBracket
        }

        self.root = None
        self.current = None

    def parseExpression(self):
        content = ""

        for character in self.expression:
            if character in self.delimitators.keys():
                self.delimitators[character](content)
                content = ""
                print("Root: \n" + self.root.treeString())
            else:
                content = content + character


    def handleOpenBracket(self, content):
        # print(self.handleOpenBracket)
        new_node = node.Node(content, self.current)

        if self.current:
            self.current.adoptChild(new_node)

        self.current = new_node
        self.setRoot(new_node)

    def handleComma(self, content):
        # print(self.handleComma)
        if content:
            new_node = node.Node(content, self.current)
            self.current.adoptChild(new_node)

    def handleClosedBracket(self, content):
        # print(self.handleClosedBracket)
        if content:
            new_node = node.Node(content, self.current)
            self.current.adoptChild(new_node)

        self.current = self.current.parent

    def setRoot(self, node):
        if self.root is None:
            self.root = node
        # try:
        #     self.root = self.expression[0]
        #
        #     if self.validateTerm(self.root):
        #         self.root = self.ex
        # except IndexError as e:
        #     print("The expression is empty. There is not root")

    def validateTerm(self, term):
        """
        Function which checks whether a string is a term based on whether it appears in the arity map or if it is formed of only letters.
        """
        if term.isalpha() :
            if term in self.arityMap.keys():
                print("This is a term.")
            else:
                print("This is not a term because it does not appear in the arity map.")
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
    # test.validateTerm('f')
    # test.validateTerm('g')
    # test.validateTerm('0')
    # test.validateTerm('/')

    # test.parseExpression()
    # test.setRoot('f')
    # test.parseExpression()
    # print(test.getRoot())
