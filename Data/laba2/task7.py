import turtle
import random


def mountain(t, x1, y1, x2, y2, depth, rough):
    if depth == 0:
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
        return
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2 + random.uniform(-rough, rough)
    mountain(t, x1, y1, mx, my, depth - 1, rough / 2)
    mountain(t, mx, my, x2, y2, depth - 1, rough / 2)


def main():
    random.seed(1)
    t = turtle.Turtle()
    win = turtle.Screen()
    win.setup(900, 500)
    t.speed(0)
    t.color("dark green")

    pts = [(-400, -100), (-150, -100), (100, -100), (400, -100)]
    for i in range(len(pts) - 1):
        mountain(t, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], 7, 80)

    win.exitonclick()


main()