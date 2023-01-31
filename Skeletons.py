import random
import time
from tkinter import *
from Character import *


class Skeleton(Character):

    lastmove = time.time()

    def __init__(self, draw):
        self.draw = draw
        self.image = self.draw.load_image("images/skeleton.png")
        self.init_stats()

    def init_stats(self):
        self.x, self.y = self.draw.generate_random()
        d6 = random.randint(1, 6)
        self.HP = 2 * self.draw.Level * d6
        self.DP = self.draw.Level/2 * d6
        self.SP = self.draw.Level * d6

    def update(self):
        if self.HP <= 0:
            return

        self.move()
        self.draw.draw_character(self)


class SkeletonKey(Skeleton):
    def __init__(self, draw):
        super().__init__(draw)
        self.key = True
        self.draw = draw
        self.image = self.draw.load_image("images/skeletonK.png")
