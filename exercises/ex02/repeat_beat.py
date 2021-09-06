"""Repeating a beat in a loop."""

__author__ = "730394749"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
times: int = int(input("How many times do you want to repeat it? "))
i: int = int(0)
beat_full: str = str(beat)
while times > i:
    beat_full: str = str(beat + " " + beat_full)
    i = i + 1
print(beat_full)