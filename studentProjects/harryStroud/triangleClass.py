import math
import pyglet

class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = 0
        self.yvelocity = 0

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter

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

    def getXVelocity(self):
        """ return the velocity of the triangle in the x direction"""
        return self.xvelocity

    def getYVelocity(self):
        """ return the velocity of the triangle in the x direction"""
        return self.yvelocity

    def calculateTriangleVerteces(self):
        numberOfVertices = 3

        vertices = []

        for i in range(3):
            angle = i * (2.0 / 3.0) * math.pi
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list

        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))


        return vertexList

    def setVelocity(self, xvel, yvel):
        """set the x & y velocity components"""
        self.xvelocity = xvel
        self.yvelocity = yvel

    def updateCoordinates(self, windowWidth, windowHeight):

        if ((self.x + self.xvelocity > windowWidth) or (self.x + self.xvelocity < 0)):
            self.xvelocity = -1 * self.xvelocity

        if ((self.y + self.yvelocity > windowHeight) or (self.y + self.yvelocity < 0)):
            self.yvelocity = -1 * self.yvelocity

        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity