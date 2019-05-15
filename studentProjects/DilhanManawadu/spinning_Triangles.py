import pyglet
import pyglet.gl
import math
from random import randint
import colors
from triangleClass import triangleClass

# initialize the triangles that we will be drawing
triangles = []
triangles.append(triangleClass('triangle1', 'blue', 0, 0, 20, 0, 0, [0,0,0,0,0,0],0))
triangles.append(triangleClass('triangle1', 'red', 0, 0, 20, 0, 0, [0,0,0,0,0,0],0))
triangles.append(triangleClass('triangle1', 'green', 0, 0, 20, 0, 0, [0,0,0,0,0,0],0))
triangles.append(triangleClass('triangle1', 'blue', 0, 0, 20, 0, 0, [0,0,0,0,0,0],0))
triangles.append(triangleClass('triangle1', 'white', 0, 0, 20, 0, 0, [0,0,0,0,0,0],0))

image = pyglet.resource.image('Images/surprise.png')
image.width = 100
image.height = 100

rotationAngle = 100


class graphicsWindow(pyglet.window.Window) :
    def __init__(self) :
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class



        for i in triangles:
            i.setCentreCoordinates(self.width / 2, self.height / 2)
            i.setVelocity(randint(-10, 10), randint(-10,10))
            i.setVertices()
            i.setRotationAngle(0)


        colors.printAvailableColors()

    def update(self, interval, dt) :
        for i in triangles :
            # move triangles to new coordinates
            i.moveTriangle(dt,self.width,self.height)

            # move the coordinates to respective positions (unrotated)
            i.setVertices()

            # change rotation angle by 'rotationAngle'
            i.setRotationAngle(i.getRotationAngle()+rotationAngle)




            i.rotateVertices()






    def on_draw(self) :
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        image.blit(window.width // 2, window.height // 2)

        for i in triangles:
            # calculate vertices of triangle i
            #vertices = i.calculateTriangleVertices()

            vertices = i.getVertices()
            # rotate vertices of triangle i
            #vertices = i.rotateVertices(i.vertices, 1)

            # convert the vertices list to pyGlet vertices format
            vertexList = pyglet.graphics.vertex_list(3, ('v2f', vertices))

            # now use pyGlet commands to draw lines between the vertices
            lineColor = i.color
            pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1],
                                colors.color[lineColor][2])  # specify colors
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw





# this is the main game engine loop
if __name__ == '__main__' :
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1./30, 0.50)  # tell pyglet the on_draw() & update() timestep
    # First arg is interval and varies runtime due to latency. Therefore second argument dt is used for calculations
    pyglet.app.run()  # run pyglet


