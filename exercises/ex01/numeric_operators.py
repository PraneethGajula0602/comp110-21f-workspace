"""This is a program to demonstrate common python operators!"""

__author__ = "730394749"

LHS: str = input("Left-hand side: ")
RHS: str = input("Right-hand side: ")
left: int = int(LHS)
right: int = int(RHS)
print(LHS + " ** " + RHS + " is " + str(left**right))
print(LHS + " / " + RHS + " is " + str(left / right))
print(LHS + " // " + RHS + " is " + str(left // right))
print(LHS + " % " + RHS + " is " + str(left % right))