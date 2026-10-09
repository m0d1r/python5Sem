import turtle


def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
        return
    length /= 3
    koch(t, length, depth - 1)
    t.left(60)
    koch(t, length, depth - 1)
    t.right(120)
    koch(t, length, depth - 1)
    t.left(60)
    koch(t, length, depth - 1)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.speed(0)
    t.up()
    t.goto(-200, 0)
    t.down()
    koch(t, 400, 4)
    win.exitonclick()


main()