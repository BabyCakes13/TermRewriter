import sys
print(sys.path)

from utils import expression_parser, term


if __name__ == "__main__":
    expression = "f1(f2(x,f3(i(f4(x,f5(H,j))),e(i(x),Y))))"

    substitutionMap = {
    "x": "m(y)",
    "Y": "blabla"
    }

    parser = expression_parser.ExpressionParser(expression)
    parser.parseExpression()
