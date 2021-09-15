"""An exercise in remainders and boolean logic."""

__author__ = "730394749"


# Begin your solution here...
value: int = int(input("Enter an int: "))
even: int = value % 2
seven: int = value % 7
if even == 0 and seven == 0:
    print("TAR HEELS")
if even == 0 and not seven == 0:
    print("TAR")
if not even == 0 and seven == 0:
    print("HEELS")
if not even == 0 and not seven == 0:
    print("CAROLINA")
