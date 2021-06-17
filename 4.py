from turtle import *

speed(100)
bok = 90
gracz = "o"
plansza_markery = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def kwadrat():
    for i in range(4):
        fd(bok)
        left(90)


def wygrana():
    pass


def plansza():
    for j in range(3):
        for i in range(3):
            pd()
            kwadrat()
            pu()
            fd(bok)

        left(90)
        fd(bok)
        left(90)
        fd(3 * bok)
        right(180)


def krzyzyk(k_x, k_y):
    plansza_markery[int(k_x) + int(k_y) * 3] = "x"
    pu()
    setx(k_x * bok + bok / 6)
    sety(k_y * bok + bok / 6)

    pd()
    left(45)
    fd(bok)
    right(135)
    pu()
    fd(bok / 1.41)
    right(135)
    pd()
    fd(bok)
    right(135)


def kolko(ko_x, ko_y):
    plansza_markery[int(ko_x) + int(ko_y) * 3] = "o"
    pu()
    setx(ko_x * bok + bok / 2)
    sety(ko_y * bok + 5)
    pd()
    circle((bok - 10) / 2)


def fxn(x, y):

    tu_x = x // bok
    tu_y = y // bok
    index = tu_x + tu_y * 3
    index_curr = plansza_markery[int(index)]
    global gracz

    if 0 <= tu_x < 3 and 0 <= tu_y < 3:
        index = tu_x + tu_y * 3
        index_curr = plansza_markery[int(index)]
        if index_curr == 0:
            if gracz == "o":
                kolko(tu_x, tu_y)
                gracz = "x"
            else:
                krzyzyk(tu_x, tu_y)
                gracz = "o"


onscreenclick(fxn)
plansza()

done()
