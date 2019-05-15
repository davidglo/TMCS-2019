import pyglet
import pyglet.gl
from pyglet.window import key
import math
import random
import colors
from triangleClass import triangleClass

# initialize the triangles that we will be drawing
triangles = []
triangles.append(triangleClass('triangle1', 'blue',    0, 0, 20, 30, -40))
triangles.append(triangleClass('triangle2', 'hotpink', 0, 0, 20, -30, 80))
triangles.append(triangleClass('triangle3', 'green',    0, 0, 20, -20, -60))
triangles.append(triangleClass('triangle4', 'red', 0, 0, 20, -10, 50))
triangles.append(triangleClass('triangle5', 'sienna',    0, 0, 20, 80, -80))
triangles.append(triangleClass('triangle6', 'yellow', 0, 0, 20, -70, 50))

#lineColor = { "red" : [1, 0, 0], "green" : [0, 1, 0], "blue" : [0, 0, 1] }


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        for i in range(0, len(triangles)):
            triangles[i].setCentreCoordinates(self.width / 2, self.height / 2)
        colors.printAvailableColors()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            triangles.append(triangleClass('triangle6', colors.getRandColorString(), random.random()*self.width,
                                           random.random()*self.width, random.randint(0,20), random.randint(-80,80),
                                           random.randint(-80,80)))

    def update(self, dt):
        """Randomly shift the center of the two triangles"""
        print("Updating the center of the triangle")
        for i in range(0, len(triangles)):
            if triangles[i].getX() > window.width or triangles[i].getX() < 0:
                triangles[i].setXVelocity(triangles[i].getXVelocity() * -1.0)
            if triangles[i].getY() > window.width or triangles[i].getY() < 0:
                triangles[i].setYVelocity(triangles[i].getYVelocity() * -1.0)
            triangles[i].setCentreCoordinates(triangles[i].getX() + triangles[i].getXVelocity() * dt, \
                                              triangles[i].getY() + triangles[i].getYVelocity() * dt)
    def on_draw(self):
        """Calculate new vertex locations and draw them"""
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # convert the vertices list to pyGlet vertices format
        radius = 20
        numberOfVertices = 3

        for i in range(0, len(triangles)):
            vertexList = triangles[i].calculateTriangleVertices()
            color1 = triangles[i].getColor()
            # now use pyGlet commands to draw lines between the vertices
            # specify colors
            pyglet.gl.glColor3f(colors.color[color1][0], colors.color[color1][1], colors.color[color1][2])
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    timestep = 1/30.0
    pyglet.clock.schedule_interval(window.update, timestep)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet