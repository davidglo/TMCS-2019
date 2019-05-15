import pyglet
import pyglet.gl
import math
from random import randint
import colors as col





def calculate_triangle_vertices(radius,xcenter,ycenter):
    # now we will calculate the list of vertices required to draw a triangle
    numberOfVertices = 3  # specify the number of vertices we need for the shape
    vertices = []  # initialize a list of vertices

    for i in range(0, numberOfVertices):
        angle = i * (2.0 / 3.0) * math.pi  # specify a vertex of the triangle (x,y values)
        x = radius * math.cos(angle) + xcenter
        y = radius * math.sin(angle) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

    # convert the vertices list to pyGlet vertices format for the first triangle
    vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
    return vertexList



class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]  # initialize the centre of the triangle
        self.center2 = [self.width / 2, self.height / 2]  # initialize the centre of the triangle
        col.print_available_colors()



    def update(self, dt):
        print("Updating the center of the triangle")
        self.center1 = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]
        self.center2 = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]



    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # now we will calculate the list of vertices required to draw the FIRST triangle
        radius = 20
        vertexList = calculate_triangle_vertices(radius,self.center1[0],self.center1[1])

        # now use pyGlet commands to draw lines between the vertices for the first triangle
        lineColor = 'green'  # choose color
        pyglet.gl.glColor3f(col.color[lineColor][0], col.color[lineColor][1], col.color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

        # now we will calculate the list of vertices required to draw the SECOND triangle
        radius = 20
        vertexList = calculate_triangle_vertices(radius,self.center2[0],self.center2[1])

        # now use pyGlet commands to draw lines between the vertices for the second triangle
        lineColor = 'blue'  # choose color
        pyglet.gl.glColor3f(col.color[lineColor][0], col.color[lineColor][1], col.color[lineColor][2])  # openGL color specification
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()   # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run() # run pyglet
