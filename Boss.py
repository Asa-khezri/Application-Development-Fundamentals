import random
import time
from tkinter import *
from Character import *


class Boss(Character):

    lastmove = time.time()

    def __init__(self, draw):
        self.draw = draw
        self.image = draw.load_image("images/Boss.png")
        self.init_stats()

    def init_stats(self):
        self.x, self.y = self.draw.generate_random()
        d6 = random.randint(1, 6)
        self.HP = 2 * self.draw.Level * d6 + d6 #X=draw.Level
        self.DP = self.draw.Level/2 * d6 + d6 / 2
        self.SP = self.draw.Level * d6 + self.draw.Level

    def update(self):
        if self.HP <= 0:
            return

        self.move()

        self.draw.draw_character(self)
