from tkinter import *
from Hero import Hero
from Skeletons import *
from Boss import Boss
from Draw import Draw


draw = Draw()
hero = Hero(draw)
boss = Boss(draw)


s1 = SkeletonKey(draw)
s2 = Skeleton(draw)
s3 = Skeleton(draw)


draw.bind('<space>', lambda x: hero.fight(boss, s1, s2, s3))


def level_up():
    if boss.HP <= 0 and s1.HP <= 0:
        draw.Level += 1
        s1.init_stats()
        s2.init_stats()
        s3.init_stats()
        boss.init_stats()
        hero.init_stats()


label_string = StringVar()
label = Label(draw.root, textvariable=label_string)
label.pack()


def display_stats():
    str = f"Hero (Level {draw.Level}) HP: {hero.HP} | DP: {hero.DP} | SP: {hero.SP}\n"
    str += f"Boss HP: {boss.HP} | DP: {boss.DP} | SP: {boss.SP}\n"
    str += f"Skeleton HP: {s1.HP} | DP: {s1.DP} | SP: {s1.SP}\n"
    label_string.set(str)


while True:
    draw.update()
    boss.update()
    hero.update()

    level_up()

    s1.update()
    s2.update()
    s3.update()

    display_stats()

    draw.root.update_idletasks()
    draw.root.update()
