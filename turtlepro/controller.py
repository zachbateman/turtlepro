'''
Python module implementing turtle-controlling classes.
'''
import turtle
import math



class TurtlePro():

    def __init__(self, linesize=3, color=(0.2, 0.3, 0.5), canvas=None) -> None:
        self.default_linesize = linesize

        if canvas:  # if an existing tkinter canvas is provided, use it
            turtle.RawTurtle(canvas)

        turtle.pensize(linesize)
        turtle.pencolor(*color)
        turtle.title('TurtlePro')
        turtle.hideturtle()
        turtle.speed(0)  # fastest speed
        turtle.setundobuffer(None)  # disable undobuffer to improve performance

        self.max_dist_from_center = 0


    def delay_refresh_until_end(self) -> None:
        print('Delaying screen refresh until turtle is done drawing... Please wait.')
        turtle.tracer(0, 0)

    def get_canvas(self):
        '''Return the tkinter canvas used by this turtle'''
        return turtle.getscreen().getcanvas()

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



class PolarTurtle(TurtlePro):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.max_radius = 0


    def circle_xy(self, radians, radius) -> tuple:
        '''Calc coords of edge of circle at given angle'''
        return (math.cos(radians) * radius, math.sin(radians) * radius)

    def _check_radius(self, radius):
        '''Used to capture maximum radius used for drawing'''
        if radius > self.max_radius:
            self.max_radius = radius

    def set_title(self, text) -> None:
        '''
        Put a title at the top of the drawing.  Do this AT THE END
        OF DRAWING so that TurtlePro knows how far to go!
        '''
        self.write_text(text, 0, self.max_radius + 5, size=16)

    def draw_ark(self, init_radian, end_radian, radius, speed='detailed') -> None:
        '''Draw an ark (part of a circle)'''
        self._check_radius(radius)
        initial_position = self.circle_xy(init_radian, radius)
        if turtle.position() != initial_position:
            turtle.penup()
            turtle.goto(initial_position)
            turtle.pendown()
        if speed == 'superfast':
            # skip num_segments and associated loop below by just using 1 segment
            turtle.goto(*self.circle_xy(end_radian, radius))
            return
        elif speed == 'fast':
            num_segments = 5
        elif speed == 'detailed':
            num_segments = 40
        else:
            print('Incorrect speed kwarg in PolarTurtle.draw_ark().')
            print('Please specify "detailed", "fast", or "superfast"')

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
