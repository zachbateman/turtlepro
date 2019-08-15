import sys
sys.path.insert(1, '..')
import turtle
import turtlepro

def test_func():
    tpro = turtlepro.TurtlePro()
    tpro.set_title('Test Title')
    tpro.draw_line((-70, -10), (70, -10))
    tpro.draw_lines([(-100, -40), (100, -40), (100, 40), (-100, 40), (-100, -40)])
    turtle.done()



if __name__ == '__main__':
    test_func()