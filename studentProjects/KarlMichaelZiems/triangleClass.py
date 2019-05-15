import math
import pyglet
import pyglet.gl
import numpy

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
        self.vertices = [0]*6
        self.theta = 0
        self.thetaIncrement = 0
        self.speed = 0

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

    def getSpeed(self):
        """return speed"""
        return self.speed

    def setSpeed(self, value):
        """set speed"""
        self.speed = value

    def updateVertices(self):
        """This function updates the vertices for the triangle"""
        self.vertices = []  # initialize a list of vertices

        angle = [0.0, (2.0 / 3.0) * math.pi, (4.0 / 3.0) * math.pi]
        for i in range(0, len(angle)):
            x = self.radius * math.cos(angle[i]) + self.x
            y = self.radius * math.sin(angle[i]) + self.y
            self.vertices.append(x)  # append the x value to the vertex list
            self.vertices.append(y)  # append the y value to the vertex list

    def rotateVertices(self):
        """function to translate a set of coordinates to the (0,0) origin & then rotate them by some angle theta"""

        # translate vertices to the origin
        c = numpy.array([[self.vertices[0] - self.x,self.vertices[1] - self.y],
                         [self.vertices[2] - self.x,self.vertices[3] - self.y],
                         [self.vertices[4] - self.x,self.vertices[5] - self.y]])

        theta = (self.theta / 180.) * numpy.pi       # calculate theta in radians & the corresponding rotation matrix
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c,rotMatrix)                # matrix-matrix multiplication with numpy

        self.vertices = [c[0][0] + self.x,c[0][1] + self.y,    # translate the rotated vertices back to the center
                         c[1][0] + self.x,c[1][1] + self.y,
                         c[2][0] + self.x,c[2][1] + self.y]


    def getVertices(self):
        """get vertices in oyglet format"""
        return pyglet.graphics.vertex_list(3, ('v2f', self.vertices))

    def setVelocity(self, xv, yv):
        """set x and y velocity components"""
        self.xvelocity = xv
        self.yvelocity = yv

    def updatePosition(self, windowWidth, windowHeight):
        """update position based on current position and velocity"""

        newx = self.x + self.xvelocity
        newy = self.y + self.yvelocity

        if (newx > windowWidth) or (newx < 0):
            self.xvelocity = -1 * self.xvelocity
            newx = self.x + self.xvelocity


        if (newy > windowHeight) or (newy < 0):
            self.yvelocity = -1 * self.yvelocity
            newy = self.y + self.yvelocity

        self.x = newx
        self.y = newy

    def setThetaIncrement(self, value):
        self.thetaIncrement = value

    def updateTheta(self):
        self.theta = self.theta + self.thetaIncrement