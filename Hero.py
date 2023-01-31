import random


class Hero:

    def __init__(self, draw):
        self.draw = draw

        self.image_down = draw.load_image("images/hero-down.png")
        self.image_up = draw.load_image("images/hero-up.png")
        self.image_left = draw.load_image("images/hero-left.png")
        self.image_right = draw.load_image("images/hero-right.png")
        self.image = self.image_down

        draw.bind("<Left>", self.leftKey)
        draw.bind("<Right>", self.rightKey)
        draw.bind("<Up>", self.upKey)
        draw.bind("<Down>", self.downKey)

        self.init_stats()

    def init_stats(self):
        self.x = 0
        self.y = 0
        d6 = random.randint(1, 6)
        self.HP = 20 + 3 * d6
        self.DP = 2 * d6
        self.SP = 5 + d6

    def leftKey(self, event):
        if self.draw.MoveAllowed(self.x-1, self.y):
            self.x -= 1
            self.image = self.image_left

    def rightKey(self, event):
        if self.draw.MoveAllowed(self.x+1, self.y):
            self.x += 1
            self.image = self.image_right

    def upKey(self, event):
        if self.draw.MoveAllowed(self.x, self.y-1):
            self.y -= 1
            self.image = self.image_up

    def downKey(self, event):
        if self.draw.MoveAllowed(self.x, self.y+1):
            self.y += 1
            self.image = self.image_down

    def fight(self, boss, skeleton1, skeleton2, skeleton3):
        if boss.x == self.x and boss.y == self.y and self.SP >= boss.DP:
            boss.HP -= self.SP
            # After a hero character performed a strike the defender should strike back the same way
            if boss.SP >= self.DP:
                self.HP -= boss.SP

        for skeleton in [skeleton1, skeleton2, skeleton3]:
            if skeleton.x == self.x and skeleton.y == self.y and self.SP >= skeleton.DP:
                skeleton.HP -= self.SP
                # After a hero character performed a strike the defender should strike back the same way
                if skeleton.SP >= self.DP:
                    self.HP -= skeleton.SP

    def update(self):
        self.draw.draw_character(self)
