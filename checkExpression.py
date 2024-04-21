from sympy import *
from sympy.abc import *
import re

symbols = []

def InputExpression():
    exp = input("Enter an expression: Y = ")
    # if exp.find('~(') != -1:
    #     return exp
    simplified_expression = simplify_logic(exp)
    return simplified_expression

def countVariables(expression):
    symbols = expression.free_symbols
    num_variables = len(symbols)
    return num_variables

def separate_variables(expression):
    exp = str(expression)
    variables = set(re.findall(r'\b\w\b', exp))
    negated_variables = set(re.findall(r'~\b\w\b', exp))
    variables -= {var[1:] for var in negated_variables}
    return variables, negated_variables

def reExpression(expression):
    num_variables = countVariables(expression)
    exp = str(expression)
    variables, negated_variables = separate_variables(expression)
    if num_variables > 1:
        if exp.find('~(') != -1:
            return exp
        if exp.find('&') != -1 or exp.find('|') != -1:
            for item in variables:
                exp = re.sub(item, "~" + item, exp)
            for item in negated_variables:
                exp = re.sub(item, "~" + item, exp)
        if exp.find('&') != -1:
            exp = exp.replace('&', '|')
        elif exp.find('|') != -1:
            exp = exp.replace('|', '&')
        exp = '~(' + str(simplify_logic(exp)) + ")"
        return exp
    return exp

def determine_operation(expression):
    exp = str(expression)
    if exp.find('~(') != -1 and exp.find('&') != -1:
        return 'NAND'
    elif exp.find('~(') != -1 and exp.find('|') != -1:
        return 'NOR'
    elif exp.find('~') != -1:
        return 'NOT'
    else:
        return 'None'

def main():
    exp = [A, ~A, A & B, ~A & B, A & ~B, ~(A & B), A | B, ~A | B, A | ~B, ~(A | B)]
    for item in exp:
        print(item)
        a = reExpression(item)
        print(countVariables(item))
        print(determine_operation(a))
        x,y = separate_variables(a)
        print(x.union(y))
        print('------------------')

if __name__ == "__main__":
    main()