class TermTree:
    """
    This will be the tree representation of a given expression.
    """
    def __init__(self):
        self.expression = "f(f(x,f(i(f(x,f(H,j))),e(i(x),Y)))"
        self.arityMap = {'f': 2, 'i': 1, 'e': 2, 'j': 0}
        # self.expression = ""
        self.root = None

    def parseExpression(self):
        for character in self.expression:
            print(character)

    def setRoot(self, term):
        try:
            self.root = self.expression[0]
        except IndexError as e:
            print("The expression is empty. There is not root")

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

    test.validateTerm('f')
    test.validateTerm('g')
    test.validateTerm('0')
    test.validateTerm('/')

    # test.parseExpression()
    # test.setRoot('f')
    # test.parseExpression()
    # print(test.getRoot())
