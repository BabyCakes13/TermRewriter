class Node:
    """
    This will be a term of an expression.
    """
    def __init__(self, content, parent):
        self.content = content
        self.parent = parent
        self.children = []

    def adoptChild(self, child):
        self.children.append(child)

    def getArity(self):
        """
        The arity of the function is actually given by the number of its children.
        """
        return len(self.children)

    def expressionString(self):
        """
        Function which pretty prints the expression.
        """
        string = self.content

        if len(self.children) > 0:
            string = string + " ("
            delimitator = ""
            for child in self.children:
                string = string + delimitator + str(child)
                delimitator = ", "
            string = string + ")"

        return string

    def treeStringRecursive(self, prefix):
        """
        Functi
        """
        string = ""
        for child in self.children:
            if child == self.children[-1]:
                string = string + (prefix + "└── " + child.content) + "\n"
                string = string + child.treeStringRecursive( prefix + "    " )
            else:
                string = string + (prefix + "├── " + child.content) + "\n"
                string = string + child.treeStringRecursive( prefix + "│   " )

        return string

    def treeString(self):
        """
        Function which pretty prints the expression as tree.
        """
        return self.content + "\n" + self.treeStringRecursive("")
