from pathlib import Path

zero_counter = 0

class Dial:
    def __init__(self):
        self.val = 50
    def inc(self, x):
        self.val = (self.val + x) % 100
    def dec(self, x):
        self.val = (self.val - x) % 100

dial = Dial()

for line in Path("input.txt").open():
    line = line.strip()
    a = int(line[1:])

    if line.startswith("L"):
        dial.dec(a)
    elif line.startswith("R"):
        dial.inc(a)

    if dial.val == 0:
        zero_counter += 1

print(zero_counter)
