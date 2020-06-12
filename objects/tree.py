"""Module which implements the term tree."""
from . import term


class TermTree:
    """This will be the tree representation of a given expression."""

    def __init__(self, expression):
        """Define the base of a term tree."""
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
        """
        Parse the experssion to form the term tree.

        We consider:
        - each opened parantheses the creation of a new level in the tree
            (thus, going down);
        - each comma a new child of a term;
        - each closed parantheses a level upwards of the tree (thus, going up).
        Because of this, we are validating the expression while parsing it:
        - if the current term does not point to the parent's root when the
            parsing is done,
        then there were not enough parantheses closed in order to go upwards
            enough on the branches until the root is reached.
        - if when closing a parantheses the current term is already none, then
            the needed number of closed parantheses was already
        reached and there are no more branches to go upwards to.
        """
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
            print("Current", self.current)
            print("Root", self.root)

            # If parsing stops at a term which is not the root, then it did not
            # close all the parentheses / did not make its way back to the top.
            print("Invalid expression. Try closing all parentheses.")
            return False

    def handleNewTerm(self, content, i):
        """Handle new term case."""
        # PS. this also treats the case when there is only one item: s = x
        if len(content) == 0:
            print("Empty item found at position %d" % i)
            return

        new_term = term.Term(content, self.current)
        self.setRoot(new_term)

        return new_term

    def handleOpenBracket(self, content, i):
        """
        Handle open bracket case.

        We know there must be a child after an opened parantheses.
        """
        new_term = self.handleNewTerm(content, i)

        if self.current:
            self.current.adoptChild(new_term)

        self.current = new_term

    def handleComma(self, content, i):
        """
        Handle comma case.

        If we find a comma, we know that the content must be a child.
        """
        if content:
            new_term = term.Term(content, self.current)
            self.current.adoptChild(new_term)

    def handleClosedBracket(self, content, i):
        """
        Handle closed brackets.

        There are two cases here: either the content before is a term, either
        it is another closed parantheses.
        """
        if content:
            new_term = term.Term(content, self.current)
            self.current.adoptChild(new_term)

        if self.current:
            self.current = self.current.parent
        else:
            # If current becomes null after the parsing, then there were too
            # many parentheses opened.
            print("Too many parantheses closed at position %d" % i)
            return False

    def substitute(self, substitutionMap):
        """Substitute using the substitutin map provided."""
        self.substituteFromTerm(substitutionMap, self.root)

    def substituteFromTerm(self, substitutionMap, term):
        """Recursivelly substitute in the tree."""
        if term.content in substitutionMap.keys():
            foundSubstitution = substitutionMap[term.content]

            print("Replace ", term.content, term, " with ", foundSubstitution)

            substitutionTree = TermTree(foundSubstitution)
            substitutionTree.printTree()
            substitutionTree.printExpression()

            termPosition = term.parent.children.index(term)
            term.parent.children[termPosition] = substitutionTree.getRoot()
            term.parent.children[termPosition].parent = term.parent
        else:
            for child in term.children:
                self.substituteFromTerm(substitutionMap, child)

    def setRoot(self, term):
        """Set root, if there is none yet."""
        if self.root is None:
            self.root = term

    def printTree(self, activatePosition=True):
        """Print the expression in tree form."""
        if self.root:
            print(self.root.treeString(activatePosition))
        else:
            print("There is no root.")

    def printExpression(self, activatePosition=True):
        """Print the experssion in, well, expression form."""
        if self.root:
            print(self.root.expressionString(activatePosition))
        else:
            print("There is no root.")

    def validateTerm(self, term):
        """
        Check whether the term is valid.

        Based on whether it is formed only of letters or (not implemented yet)
        whether it appears in the arity map. Needs tweaking.
        """
        if term.isalpha():
            if term in self.arityMap.keys():
                print("This is a term.")
            else:
                print("This is a variable.")
        else:
            print("This is not a term because it is not a valid term name.")

    def getRoot(self) -> str:
        """Return the root of the tree."""
        if self.root:
            return self.root
        else:
            print("No root set.")


if __name__ == "__main__":
    # expression = "f(e,x,y)"
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
