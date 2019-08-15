'''
Python module implementing turtle-controlling classes.
'''
import turtle
import math
import tkinter as tk



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
        self.pan_and_zoomable()


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

    def pan_and_zoomable(self) -> None:
        # See: https://stackoverflow.com/questions/41656176/tkinter-canvas-zoom-move-pan/48137257
        # for how to handle mouse events!!!
        canvas = self.get_canvas()

        def zoom(event):
            amount = 0.95 if event.delta < 0 else 1.05
            canvas.scale(tk.ALL, 0, 0, amount, amount)
        canvas.bind('<MouseWheel>', zoom)

        def pan(event):
            canvas.scan_mark(event.x, event.y)
            canvas.scan_dragto(event.x, event.y, gain=1)

        def pan_start(event):
            canvas.scan_mark(event.x, event.y)
        canvas.bind('<ButtonPress-1>', pan_start)

        def pan_move(event):
            canvas.scan_dragto(event.x, event.y, gain=1)
        canvas.bind('<B1-Motion>', pan_move)

    def draw_line(self, point1, point2) -> None:
        '''
        Draw a line from the first point to the second point.
        '''
        turtle.penup()
        turtle.goto(point1)
        turtle.pendown()
        turtle.goto(point2)

    def draw_lines(self, points) -> None:
        '''
        Draw lines through all given "points" (iterable).
        '''
        if len(points) < 2:
            raise Exception('draw_lines() arg must have at least 2 points!')
        turtle.penup()
        turtle.goto(points.pop(0))
        turtle.pendown()
        while points:
            turtle.goto(points.pop(0))



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

    def set_title(self, text, force_radius=None, size=16) -> None:
        '''
        Put a title at the top of the drawing.  Do this AT THE END
        OF DRAWING so that TurtlePro knows how far to go!
        '''
        if force_radius is None:
            self.write_text(text, 0, self.max_radius + 5, size=size)
        else:
            self.write_text(text, 0, force_radius, size=size)

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

    def write_polartext(self, text, angle, radius, font='Arial', size=16) -> None:
        '''Calculate x and y from angle and radius and than call cartesian write_text'''
        x, y = self.circle_xy(angle, radius)
        self.write_text(text, x=x, y=y, font=font, size=size)
