import pyglet
import pyglet.gl
from random import randint
import colours
import math
from triangleClass import triangleClass

# initialize the triangles that we will be drawing
triangle1 = triangleClass('triangle1', 'blue',    0, 0, 30)
triangle2 = triangleClass('triangle2', 'hotpink', 0, 0, 20)

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        triangle1.setCentreCoordinates(self.width / 2, self.height / 2)
        triangle2.setCentreCoordinates(self.width / 2, self.height / 2)

        triangle1.setVelocity(6,3)
        triangle2.setVelocity(-4,5)

    def update(self, dt):
        # print("Updating the center of the triangle")
        triangle1.updateCoordinates(self.width, self.height )
        triangle2.updateCoordinates(self.width, self.height )

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        vertexList1 = triangle1.calculateTriangleVerteces()
        vertexList2 = triangle2.calculateTriangleVerteces()

        # select "random" for a random colour of triangle every time
        random_colour = True

        # now use pyGlet commands to draw lines between the vertices
        if random_colour == True:
            line_colour = colours.random_colour()
            pyglet.gl.glColor3f(line_colour[0], line_colour[1], line_colour[2])
            vertexList1.draw(pyglet.gl.GL_LINE_LOOP)  # draw triangle 1
            vertexList2.draw(pyglet.gl.GL_LINE_LOOP)
        else:
            line_colour = triangle1.getColor()
            pyglet.gl.glColor3f(colours.colour_palette[line_colour][0], colours.colour_palette[line_colour][1],
                                colours.colour_palette[line_colour][2])
            vertexList1.draw(pyglet.gl.GL_LINE_LOOP)
            line_colour = triangle2.getColor()
            pyglet.gl.glColor3f(colours.colour_palette[line_colour][0], colours.colour_palette[line_colour][1],
                                colours.colour_palette[line_colour][2])
            vertexList2.draw(pyglet.gl.GL_LINE_LOOP)


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
