from tkinter import *
import random


class Draw:
    exit = False
    Level = 1

    def __init__(self):
        self.root = Tk()
        self.root.title('Wanderer Game')
        self.canvas = Canvas(self.root, width=360, height=360)
        self.canvas.pack()

        file = open("map.txt", "r")
        self.board = file.readlines()
        file.close()

        self.wall = self.load_image("images/wall.png")
        self.floor = self.load_image("images/floor.png")

    def update(self):
        self.canvas.delete("all")
        for x in range(10):
            for y in range(10):
                if self.board[y][x] == "F":
                    self.canvas.create_image(
                        x * 36, y * 36, image=self.floor, anchor=NW)
                else:
                    self.canvas.create_image(
                        x * 36, y * 36, image=self.wall, anchor=NW)

    def MoveAllowed(self, x, y):
        if x > 9 or x < 0 or y > 9 or y < 0:
            return False
        if self.board[y][x] == "W":
            return False
        return True

    def draw_character(self, person):
        x = person.x * 36
        y = person.y * 36
        self.canvas.create_image(x, y, image=person.image, anchor=NW)

    def bind(self, key, func):
        self.root.bind(key, func)

    def load_image(self, path):
        return PhotoImage(file=path).subsample(2)

    def generate_random(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.MoveAllowed(x, y):
                return [x, y]
