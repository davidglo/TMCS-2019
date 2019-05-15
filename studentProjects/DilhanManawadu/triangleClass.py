import math
import pyglet
import numpy
class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad, xvel, yvel, vertices, rotangle):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = xvel
        self.yvelocity = yvel
        self.vertices = vertices
        self.rotangle = rotangle

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter

    def setVelocity(self,xvel,yvel):
        """ set the x,y velocities of the triangle """
        self.xvelocity = xvel
        self.yvelocity = yvel

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

    def setRotationAngle(self, angle):
        self.rotangle = math.pi * angle / 180.0

    def getRotationAngle(self):
        return 180.0 * self.rotangle / math.pi

    def moveTriangle(self, time, xmax, ymax):
        self.x = self.x + self.xvelocity * time
        if self.x > xmax:
            self.x = xmax
            self.xvelocity = -1 * self.xvelocity
        elif self.x < 0:
            self.x = 0
            self.xvelocity = -1 * self.xvelocity

        self.y = self.y + self.yvelocity * time
        if self.y > ymax:
            self.y = ymax
            self.yvelocity = -1 * self.yvelocity
        elif self.y < 0:
            self.y = 0
            self.yvelocity = -1 * self.yvelocity

    def setVertices(self):
        """This function calculates polygen vertices for a given shape, radius and center coordinates"""
        numberOfVertices = 3  # specify the number of vertices we need for the shape
        vertices = []  # initialize a list of vertices

        for i in range(3) :
            angle = 2.0 * math.pi * i / 3
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list


        self.vertices = vertices

    def rotateVertices(self) :
        """function to translate a set of coordinates to the (0,0) origin & then rotate them by some angle theta"""

        # translate vertices to the origin
        c = numpy.array([[self.vertices[0] - self.x, self.vertices[1] - self.y],
                         [self.vertices[2] - self.x, self.vertices[3] - self.y],
                         [self.vertices[4] - self.x, self.vertices[5] - self.y]])

        theta = self.rotangle
        #theta = (theta / 180.) * numpy.pi  # calculate theta in radians & the corresponding rotation matrix
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c, rotMatrix)  # matrix-matrix multiplication with numpy

        vertices = [c[0][0] + self.x, c[0][1] + self.y,  # translate the rotated vertices back to the center
                         c[1][0] + self.x, c[1][1] + self.y,
                         c[2][0] + self.x, c[2][1] + self.y]

        self.vertices = vertices

    def getVertices(self):
        return self.vertices
