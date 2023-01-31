import time
import random


class Character:
    lastmove = time.time()

    def __init__(self, draw):
        self.draw = draw

    def move(self):
        if time.time() - self.lastmove < 1:
            return

        self.lastmove = time.time()
        d = random.randint(0, 3)
        x = 0
        y = 0
        if d == 0:
            x += 1
        elif d == 1:
            x -= 1
        elif d == 2:
            y += 1
        elif d == 3:
            y -= 1
        if self.draw.MoveAllowed(self.x + x, self.y + y):
            self.x += x
            self.y += y
