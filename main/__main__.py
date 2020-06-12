"""Module which represents the entrypoint of the application."""

from objects import tree


valid_test_expressions = [
    "f(f(x,f(i(f(x,f(H,j))),e(i(x),Y))))",
    "x",
    "f(e,i)",
]


invalid_test_expressions = {
    "f(x",
    "f(x,)",
    "f(x,y))",
}


if __name__ == "__main__":

    expression = "f(f(x,f(i(f(x,f(H,j))),e(i(x),y))))"

    substitutionMap = {
        "x": "m(y)",
        "y": "noty"
    }

    termTree = tree.TermTree(expression)
    termTree.parseExpression()

    print("Root of the expression is: " + termTree.getRoot().content)

    expressionRoot = termTree.getRoot()

    # termTree = term.TermTree(expressionRoot)
    # expressionTree = term.TermExpression(expressionRoot)

    # termTree.printTree(activatePosition=False)
    print("\nINPUT EXPRESSION:")
    print(expression)

    print("\nPARSING OUTPUT EXPRESSION:")
    termTree.printExpression(activatePosition=True)
    print("\nPARSING OUTPUT TREE: \n")
    termTree.printTree(activatePosition=True)

    termTree.substitute(substitutionMap)

    termTree.printTree(activatePosition=True)
    # test_different_expressions()
