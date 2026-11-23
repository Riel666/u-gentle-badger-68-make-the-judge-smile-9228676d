"""Write one line to /output/entry.txt.

One small good thing that happened today: a neighbour, a still-warm
loaf, a note that says "you looked tired", and half of it eaten
standing in the hallway. At most 200 characters, and the program
writes exactly that line and nothing else.
"""

import os

ENTRY = "My neighbour left a still-warm loaf on my doorstep with a note that just said 'you looked tired' — I ate half of it standing in the hallway."


def main():
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY == ENTRY.strip()

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
