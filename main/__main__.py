import sys
print (sys.path)

import main.application
from utils import expression_parser, term


def test_parsing(expression, activatePosition):
    parser = expression_parser.ExpressionParser(expression)
    parser.parseExpression()

    # print("Root of the expression is: " + parser.getRoot().content)

    expressionRoot = parser.getRoot()
    termTree = term.TermTree(expressionRoot)
    expressionTree = term.TermExpression(expressionRoot)

    # termTree.printTree(activatePosition=False
    print("EXPRESSION:")
    print(expression)
    # expressionTree.printExpression(activatePosition=True)
    print("TREE: \n")
    termTree.printTree(activatePosition)

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

def test_different_expressions():
    valid_test_expressions = valid_test_expressions()
    invalid_test_expressions = invalid_test_expressions()

    print("Starting parsing of valid expressions...\n")

    for expression in valid_test_expressions:
        test_parsing(expression)
        print("\n\n****************************************************\n\n")

    print("Starting parsing of invalid expressions...")
    for expression in invalid_test_expressions:
        test_parsing(expression)
        print("\n\n****************************************************\n\n")


if __name__ == "__main__":

    expression = "f1(f2(x,f3(i(f4(x,f5(H,j))),e(i(x),Y))))"

    substitutionMap = {
    "x": "m(y)",
    "Y": "blabla"
    }

    test_parsing(expression, activatePosition=False)
