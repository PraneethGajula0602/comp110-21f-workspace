"""Counting letters in a string."""

__author__ = "730394749"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for? "))
word: str = str(input("Enter a word: "))
long: int = len(word)
i: int = int(0)
k: int = int(0)
while i < long:
    if word[i] == letter:
        k = k + 1
    i = i + 1
print(k)