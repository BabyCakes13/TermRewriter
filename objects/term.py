"""Module which implements the Term class."""


class Term:
    """This will represent a term of an expression."""

    # When enabled, the tree also displays the position of the terms.
    POSITION = False

    def __init__(self, content, parent):
        """
        Initialise the term related objects.

        Each term has a content, as well as remembering their parent and
        children.
        """
        self.content = content
        self.parent = parent
        self.children = []

    def adoptChild(self, child):
        """Adopt the child whenever we find a new node with this parent."""
        self.children.append(child)

    @property
    def position(self):
        """
        Get the position of the term.

        By recusrivelly searching up in the tree.
        """
        if self.parent:
            parent_p = str(self.parent.position)
            children_p = str(self.parent.children.index(self) + 1)
            return str(parent_p + children_p)
        else:
            # If the term does not have a parent, the term is the root which
            #  has empty string as position.
            return ""

    def expressionString(self, activatePosition):
        """Pretty print the expression."""
        string = self.content

        if len(self.children) > 0:
            string = string + "("
            delimitator = ""
            for child in self.children:
                string = string + delimitator + \
                    child.expressionString(activatePosition)
                delimitator = ","
            string = string + ")"

        return string

    def treeStringRecursive(self, prefix, activatePosition):
        """Construct the term tree."""
        string = ""
        for child in self.children:
            if activatePosition:
                p = " (" + child.position + ")"
            else:
                p = ""
            if child == self.children[-1]:
                string = string + (prefix + "└── " + child.content) + p + "\n"
                string = string + child.treeStringRecursive(prefix + "    ", activatePosition)
            else:
                string = string + (prefix + "├── " + child.content) + p + "\n"
                string = string + child.treeStringRecursive(prefix + "│   ", activatePosition)

        return string

    def treeString(self, activatePosition=False):
        """Pretty print the expression as tree."""
        if activatePosition:
            return self.content + " (" + self.position + ") " + "\n" + \
                self.treeStringRecursive("", activatePosition)
        else:
            return self.content + self.position + "\n" + \
                self.treeStringRecursive("", activatePosition)

    def getArity(self):
        """
        Return the arity.

        The arity of the function is given by the number of its children.
        """
        return len(self.children)
