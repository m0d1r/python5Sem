import turtle
import random


def tree(branch_len, t, thickness):
    if branch_len > 5:
        # толщина ветви пропорциональна её длине
        t.pensize(max(1, thickness * branch_len / 75))

        # короткие ветви — «листья», длинные — ствол
        if branch_len < 25:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branch_len)

        # случайный угол поворота 15..45
        a = random.randint(15, 45)

        # случайный шаг уменьшения длины
        t.right(a)
        tree(branch_len - random.randint(10, 20), t, thickness)
        t.left(2 * a)
        tree(branch_len - random.randint(10, 20), t, thickness)
        t.right(a)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    win.setup(800, 600)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.speed(0)
    tree(100, t, 10)
    win.exitonclick()


main()