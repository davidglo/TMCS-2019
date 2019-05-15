import pyglet
import pyglet.gl
import math
from random import randint
import numpy as np
import numpy.random as npr
import random
import colors

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.center = [self.width / 2 + randint(-20, 20), self.height / 2 + randint(-20, 20)]  # initialize the centre of the triangle
        self.xvelocity = 0
        self.yvelocity = 0
        while(self.xvelocity < 0.5):
            self.xvelocity = 3 * random.random()
            if random.random() < 0.5:
                self.xvelocity *= -1
        while (self.yvelocity < 0.5):
            self.yvelocity = 3 * random.random()
            if random.random() < 0.5:
                self.yvelocity *= -1
        lineColor = random.choice(colors.colors_rgb)
        pyglet.gl.glColor3f(lineColor[0], lineColor[1], lineColor[2])

    def update(self, dt, min_width, min_height, max_width, max_height):
        if (self.center[0] + 1 > max_width) or (self.center[0] + 1 < min_width):
            lineColor = random.choice(colors.colors_rgb)
            pyglet.gl.glColor3f(lineColor[0], lineColor[1], lineColor[2])
            self.xvelocity *= -1

        if (self.center[1] + 1 > max_height) or (self.center[1] + 1 < min_height):
            lineColor = random.choice(colors.colors_rgb)
            pyglet.gl.glColor3f(lineColor[0], lineColor[1], lineColor[2])
            self.yvelocity *= -1

        self.center[0] += self.xvelocity
        self.center[1] += self.yvelocity

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        image = pyglet.resource.image('dvd.png')
        image.blit(self.center[0], self.center[1])

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 100.0, -42, -35, 409, 336)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
