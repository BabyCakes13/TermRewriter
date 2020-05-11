import sys

from utils import expression_parser, term


def valid_test_expressions():
    valid_test_expressions = [
    "f(f(x,f(i(f(x,f(H,j))),e(i(x),Y))))",
    "x",
    "f(e,i)",
    ]

    return valid_test_expressions

def invalid_test_expressions():
    invalid_test_expressions = {
    "f(x",
    "f(x,)",
    "f(x,y))",
    }

    # TODO Cover the case when there is nothing after comma. :f(x,)

    return invalid_test_expressions

def test_different_expressions(activatePosition=False):
    valid_test_expressions_result = valid_test_expressions()
    invalid_test_expressions_result = invalid_test_expressions()

    print("Starting parsing of valid expressions...\n")

    for expression in valid_test_expressions_result:
        test_parsing(expression, activatePosition)
        print("\n\n****************************************************\n\n")

    print("Starting parsing of invalid expressions...")
    for expression in invalid_test_expressions_result:
        test_parsing(expression, activatePosition)
        print("\n\n****************************************************\n\n")


if __name__ == "__main__":

    expression = "f(f(x,f(i(f(x,f(H,j))),e(i(x),y))))"

    substitutionMap = {
    "x": "m(y)",
    "y": "noty"
    }

    parser = expression_parser.ExpressionParser(expression)
    parser.parseExpression()

    # print("Root of the expression is: " + parser.getRoot().content)

    expressionRoot = parser.getRoot()
    termTree = term.TermTree(expressionRoot)
    expressionTree = term.TermExpression(expressionRoot)

    # termTree.printTree(activatePosition=False
    print("\nINPUT EXPRESSION:")
    print(expression)

    print("\nPARSING OUTPUT EXPRESSION:")
    expressionTree.printExpression(activatePosition=True)
    print("\nPARSING OUTPUT TREE: \n")
    termTree.printTree(activatePosition=True)

    termTree.substitute(substitutionMap)

    termTree.printTree(activatePosition=True)
    # test_different_expressions()
