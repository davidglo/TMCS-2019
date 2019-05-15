import pyglet
import pyglet.gl
from random import randint
import colors
from triangleClass import triangleClass

# initialize the triangles that we will be drawing
# def __init__(self,ID,color,xcenter,ycenter,rad,numberOfVertices,xvelocity,yvelocity):
triangle1 = triangleClass('triangle1', 'hotpink', 320, 240, 50,3,30,30)
triangle2 = triangleClass('triangle2', 'hotpink', 320, 240, 50,3,30,30)
timestep = 1.0/30

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        triangle1.setCentreCoordinates(timestep)
        triangle2.setCentreCoordinates(timestep)
        colors.printAvailableColors()

    def update(self, timestep):
        print("Updating the center of the triangle")
        triangle1.setCentreCoordinates(timestep)
        triangle2.setCentreCoordinates(timestep)

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # now we will calculate the list of vertices required to draw the FIRST triangle
        vertexList = triangle1.calculateTriangleVertices(timestep, self.height, self.width)

        # now use pyGlet commands to draw lines between the vertices for the first triangle
        lineColor = triangle1.getColor()  # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

        # now we will calculate the list of vertices required to draw the SECOND triangle
        radius = 20
        vertexList = triangle2.calculateTriangleVertices(timestep)

        # now use pyGlet commands to draw lines between the vertices for the second triangle
        lineColor = triangle2.getColor()   # choose color
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, timestep)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run() # run the infinite pyglet loop