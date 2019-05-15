import pyglet
import pyglet.gl
import math
from random import randint
from random import choice
import colors


# function which calculates the vertex list required to draw an equilateral triangle
def calculateTriangleVertices(radius,xcenter,ycenter):
    numberOfVertices = 3  # specify the number of vertices we need for the shape
    vertices = []  # initialize a list of vertices

    for i in range(0, numberOfVertices):
        angle = i * (2.0 / 3.0) * math.pi  # specify a vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

    # convert the vertices list to pyGlet vertices format for the first triangle & return this list
    vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
    return vertexList


def rotateVertices(self):
    """function to translate a set of coordinates to the (0,0) origin & then rotate them by some angle theta"""

    # translate vertices to the origin
    c = numpy.array([[self.vertices[0] - self.x, self.vertices[1] - self.y],
                     [self.vertices[2] - self.x, self.vertices[3] - self.y],
                     [self.vertices[4] - self.x, self.vertices[5] - self.y]])

    theta = (self.theta / 180.) * numpy.pi  # calculate theta in radians & the corresponding rotation matrix
    rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                             [numpy.sin(theta), numpy.cos(theta)]])

    c = numpy.matmul(c, rotMatrix)  # matrix-matrix multiplication with numpy

    self.vertices = [c[0][0] + self.x, c[0][1] + self.y,  # translate the rotated vertices back to the center
                     c[1][0] + self.x, c[1][1] + self.y,
                     c[2][0] + self.x, c[2][1] + self.y]

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]  # initialize the centre of the triangle
        self.xvelocity = -2
        self.yvelocity = 2

    def update(self, dt):
        self.center1[0] += self.xvelocity
        self.center1[1] += self.yvelocity

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        image = pyglet.resource.image('logan.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.center1[0], self.center1[1])

        lineColor = choice(list(colors.color.keys()))  # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification

        image = pyglet.resource.image('manby.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.center1[0]+100, self.center1[1]-100)

        lineColor = choice(list(colors.color.keys()))  # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1],colors.color[lineColor][2])  # openGL color specification

        image = pyglet.resource.image('trivial.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))

        lineColor = choice(list(colors.color.keys()))  # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification

        image = pyglet.resource.image('talk_science.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))

        image = pyglet.resource.image('essex.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.center1[0]-100, self.center1[1]-100)

        lineColor = choice(list(colors.color.keys()))  # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification

        image = pyglet.resource.image('comfortable.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))


        image = pyglet.resource.image('mano.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.center1[0]+150, self.center1[1]+150)

        lineColor = choice(list(colors.color.keys()))  # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1],colors.color[lineColor][2])  # openGL color specification

        image = pyglet.resource.image('great.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        image.blit(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))

        lineColor = choice(list(colors.color.keys()))  # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 1.5)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run() # run the infinite pyglet loopun pyglet
