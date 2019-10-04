import sys
sys.path.insert(1, '..')
import turtle
import turtlepro
import random
import math


def test_func():
    tpro = turtlepro.PolarTurtle()
    tpro.delay_refresh_until_end()

    tpro.set_title('Test Title')
    tpro.draw_line((-70, -10), (70, -10))
    tpro.draw_lines([(-100, -40), (100, -40), (100, 40), (-100, 40), (-100, -40)])

    tpro.draw_ark(0, 0.1, 150)
    tpro.draw_ark(3, 4.5, 150)
    tpro.draw_ark(0.1, 0.25, 160)
    tpro.draw_ark(2, 6, 160)
    tpro.draw_ark(0.25, 2, 170)
    tpro.draw_ark(2, 5, 180)
    tpro.draw_ark(5, 6.2, 190)

    tpro.draw_circle(200)
    tpro.draw_circle(220)
    tpro.draw_polarline(0, 220, 250)

    for i in range(150):
        tpro.draw_polarline(2*math.pi * i / 150, 200, 220)

    for _ in range(30):
        angle = random.uniform(0, 2*math.pi)
        tpro.draw_polarline(angle, 220, 300)

    turtle.done()



if __name__ == '__main__':
    test_func()