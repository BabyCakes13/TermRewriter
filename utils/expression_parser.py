from objects import node


class ExpressionParser:
    def __init__(self, expression):
        self.expression = expression

        self.delimitators = {
        '(': self.handleOpenBracket,
        ',': self.handleComma,
        ')': self.handleClosedBracket
        }

        self.root = None
        self.current = None

    def parseExpression(self):
        """
        Function which parses an expression and creates the expression tree.
        We consider:
        - each opened parantheses the creation of a new level in the tree (thus, going down);
        - each comma a new child of a node;
        - each closed parantheses a level upwards of the tree (thus, going up).
        Because of this, we are validating the expression while parsing it:
        - if the current node does not point to the parent's root when the parsing is done,
        then there were not enough parantheses closed in order to go upwards enough on the branches until the root is reached.
        - if when closing a parantheses the current node is already none, then the needed number of closed parantheses was already
        reached and there are no more branches to go upwards to.
        """
        content = ""

        for position, character in enumerate(self.expression):
            if character in self.delimitators.keys():
                self.delimitators[character](content, position)
                content = ""
            else:
                content = content + character

        if len(content) > 0 and self.root is None:
            # For expressions as: s = x (with no delimitators).
            self.handleNewTerm(content, position)

        if self.current is not None:
            # If the current focused node is not the root, then there were not enough parentheses closed so the expression is invalid.
            # Since we are going one level up the tree by a closed parantheses, not arriving to the root semnalates this.
            print("Invalid expression. Try closing all parentheses.")
            return False

    def handleNewTerm(self, content, position):
        if len(content) == 0:
            print("Empty item found at position %d" % position)
            return

        new_node = node.Node(content, self.current)
        self.setRoot(new_node)

        return new_node

    def handleOpenBracket(self, content, position):
        new_node = self.handleNewTerm(content, position)

        if self.current:
            self.current.adoptChild(new_node)

        self.current = new_node

    def handleComma(self, content, position):
        if content:
            new_node = node.Node(content, self.current)
            self.current.adoptChild(new_node)

    def handleClosedBracket(self, content, position):
        if content:
            new_node = node.Node(content, self.current)
            self.current.adoptChild(new_node)

        if self.current:
            self.current = self.current.parent
        else:
            # If current becomes null after the parsing, then there were too many parentheses opened.
            # It tried to go past the root and became null.
            print("Too many parantheses closed at position %d" % position)
            return False

    def setRoot(self, node):
        if self.root is None:
            self.root = node

    def getRoot(self):
        if self.root:
            return self.root
        else:
            print("No root set.")
