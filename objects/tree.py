class TermTree:
    """
    This will be the tree representation of a given expression.
    """
    def __init__(self):
        print("Started parsing")
        self.expression = "f(f(x,f(i(f(x,f(H,j))),e(i(x),Y)))"

    def parseExpression(self):
        print("Started parsing")
        for character in self.expression:
            print(character)


if __name__=="__main__":
    test = TermTree()
    test.parseExpression()

print("here")
