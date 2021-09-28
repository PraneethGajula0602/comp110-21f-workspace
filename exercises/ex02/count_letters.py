"""Counting letters in a string."""

__author__ = "730394749"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for? "))
word: str = str(input("Enter a word: "))
long: int = len(word)
i: int = int(0)
count: int = int(0)
while i < long:
    if word[i] == letter:
        count = count + 1
    i = i + 1
print("Count: " + str(count))