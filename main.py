from drawStick import *
from checkExpression import *

def main():
    exp = InputExpression()
    temp = countVariables(exp)
    print(temp)
    StickDefault(temp)
    exp = reExpression(exp)
    x,y = separate_variables(exp)
    print("Bieu thuc bien thuc:", exp)
    print(determine_operation(exp))
    StickPoly(temp, determine_operation(exp), x, y)
    turtle.done()

if __name__ == "__main__":
    main()