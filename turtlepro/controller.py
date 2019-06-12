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



def PolarTurtle(TurtlePro):

    def __init__(self) -> None:
        super().__init__()
        self.max_radius = 0


    def circle_xy(self, radians, radius) -> tuple:
        '''Calc coords of edge of circle at given angle'''
        return (math.cos(radians) * radius, math.sin(radians) * radius)

    def _check_radius(self, radius):
        '''Used to capture maximum radius used for drawing'''
        if radius > self.max_radius:
            self.max_radius = radius

    def set_title(self, text) -> None:
        '''Put a title at the top of the drawing.  Do this AT THE END
        OF DRAWING so that TurtlePro knows how far to go!
        '''
        self.write_text(text, 0, self.max_radius + 5, size=16)

    def draw_ark(self, init_radian, end_radian, radius, fast=False) -> None:
        '''Draw an ark (part of a circle'''
        self._check_radius(radius)
        turtle.penup()
        turtle.goto(*self.circle_xy, init_radian, end_radian, radius)
        turtle.pendown()
        num_segments=40 if not fast else 3
        for angle in range(1, num_segments + 1):
            turtle.goto(*self.circle_xy(init_radian + (end_radian - init_radian) * (angle / num_segments), radius))

    def draw_circle(self, radius) -> None:
        '''Draw a circle of given radius'''
        self.draw_ark(0, 2 * math.pi, radius)

    def draw_polarline(self, angle, radius_1, radius_2) -> None:
        '''Draw a line directly out from center with endpoints specified by radii'''
        turtle.penup()
        turtle.goto(*self.circle_xy(angle, radius_1))
        turtle.pendown()
        turtle.goto(*self.circle_xy(angle, radius_2))
