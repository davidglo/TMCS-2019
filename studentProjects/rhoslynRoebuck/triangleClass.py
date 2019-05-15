import math
import pyglet
import pyglet.gl

class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad,numberOfVertices,xvelocity,yvelocity):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.vertices = numberOfVertices
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    def setCentreCoordinates(self,timestep):
        """ set the x,y coordinates of the triangle """
        self.x = self.x + self.xvelocity*timestep
        self.y = self.y + self.yvelocity*timestep



    def getColor(self):
        """ return the color of the triangle """
        return self.color

    def getRadius(self):
        """ return the radius of the triangle """
        return self.radius

    def getX(self):
        """ return the x coordinate of the triangle """
        return self.x

    def getY(self):
        """ return the y coordinate of the triangle """
        return self.y

    def calculateTriangleVertices(self,timestep,window_height, window_width):
        """function which calculates the vertex list required to draw an equilateral triangle"""

        vertices_list = []                 # initialize a list of vertices

        for i in range(0, self.vertices):
            angle = i * (2.0 / 3.0) * math.pi  # specify a vertex of the triangle (x,y values)
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            vertices_list.append(x)  # append the x value to the vertex list
            vertices_list.append(y)  # append the y value to the vertex list

       # window2 = pyglet.window.Window()
        #print(window2)


        if x not in range(480):

            xvelocity = - self.xvelocity
            x = self.x + self.xvelocity * timestep

        if y not in range(480):
            yvelocity = - self.yvelocity
            y = self.y + self.yvelocity * timestep


        # convert the vertices list to pyGlet vertices format for the first triangle & return this list
        vertexList = pyglet.graphics.vertex_list(self.vertices, ('v2f', vertices_list))

        return vertexList
