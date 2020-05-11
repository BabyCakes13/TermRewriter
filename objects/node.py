class Node:
    """
    This will be a term of an expression.
    """

    POSITION = False # When enabled, the tree also displays the position of the terms.

    def __init__(self, content, parent):
        self.content = content
        self.parent = parent
        self.children = []

    def adoptChild(self, child):
        self.children.append(child)

    @property
    def position(self):
        """
        Get the position on the spot by recusrivelly searching up in the tree.
        """
        if self.parent:
            return str(self.parent.position + str(self.parent.children.index(self) + 1))
        else:
            # If the node does not have a parent, the node is the root which has empty string as position.
            return ""

    def getArity(self):
        """
        The arity of the function is actually given by the number of its children.
        """
        return len(self.children)

    def expressionString(self, activatePosition):
        """
        Function which pretty prints the expression.
        """
        string = self.content

        if len(self.children) > 0:
            string = string + "("
            delimitator = ""
            for child in self.children:
                string = string + delimitator + child.expressionString(activatePosition)
                delimitator = ","
            string = string + ")"

        return string

    def treeStringRecursive(self, prefix, activatePosition):
        """
        Function which constructs the tree.
        """
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
        """
        Function which pretty prints the expression as tree.
        """
        if activatePosition:
            return self.content + " (" + self.position + ") " + "\n" + self.treeStringRecursive("", activatePosition)
        else:
            return self.content + self.position + "\n" + self.treeStringRecursive("", activatePosition)
