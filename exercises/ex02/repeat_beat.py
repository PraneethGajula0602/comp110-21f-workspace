"""Repeating a beat in a loop."""

__author__ = "730394749"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
times: int = int(input("How many times do you want to repeat it? "))
i: int = int(1)
full: str = str(beat)
if times > 1:
    while times > i:
        full = beat + " " + full
        i = i + 1
    print(full)
else:
    print("No beat...")