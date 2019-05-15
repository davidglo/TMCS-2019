import pyglet
import pyglet.gl
import math
from random import randint
import numpy

colors = {"red": [1, 0, 0], "green": [0, 1, 0], "blue": [0, 0, 1], "white": [1, 1, 1]}


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.center1 = [self.width / 4, self.height / 4]  # initialize the centre of the triangle
        self.x = self.center1[0]
        self.y = self.center1[1]
        self.xvelocity = -1
        self.yvelocity = -1



    def update(self, dt, min_width, max_width, min_height, max_height):
       
        #self.center1 = [i + 1 for i in self.center1]

        if ((self.x + self.xvelocity > max_width) or (self.x + self.xvelocity < min_width)):
            self.xvelocity = -1 * self.xvelocity

        if ((self.y + self.yvelocity > max_height) or (self.y + self.yvelocity < min_height)):
            self.yvelocity = -1 * self.yvelocity

        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity





    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        image = pyglet.resource.image('dug.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.x, self.y)




        lineColor1 = "white"
        pyglet.gl.glColor3f(colors[lineColor1][0], colors[lineColor1][1], colors[lineColor1][2])  # specify colors




# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 100.0, 55, 585, 70, 410)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run the infinite pyglet loop


