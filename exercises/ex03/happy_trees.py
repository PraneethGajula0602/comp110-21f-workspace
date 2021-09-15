"""Drawing forests in a loop."""

__author__ = "730394749"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
forest: str = ""
depth: int = int(input("Depth: "))
while depth > 0:
    forest = forest + TREE
    depth = depth - 1
    print(forest)
