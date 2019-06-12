'''
Python module implementing turtle-controlling classes.
'''
import turtle
import math



class TurtlePro():

    def __init__(self, linesize=3, color=(0.2, 0.3, 0.5)) -> None:
        self.default_linesize = linesize
        turtle.pensize(linesize)
        turtle.title('TurtlePro')
        turtle.pencolor(*color)
        turtle.hideturtle()
        turtle.speed(0)

        self.max_dist_from_center = 0


    def delay_refresh_until_end(self) -> None:
        print('Delaying screen refresh until turtle is done drawing... Please wait.')
        turtle.tracer(0, 0)

    def write_text(self, text, x=0, y=0, font='Arial', size=16) -> None:
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(text, font=(font, size, 'normal'), align='center')

    def set_title(self, text) -> None:
        '''
        Put a title at the top of the drawing.  Do this AT THE END
        OF DRAWING so that TurtlePro knows how far to go!
        '''
        self.write_text(text, 0, self.max_dist_from_center + 5, size=16)
