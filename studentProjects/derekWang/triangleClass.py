import math
import pyglet

class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad,xvelocity,yvelocity):
        """ initialize a triangle 
        :rtype: object
        """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter

    def setXVelocity(self, newXVelocity):
        """ set the x velocity of the triangle """
        self.xvelocity = newXVelocity

    def setYVelocity(self, newYVelocity):
        """ set the y velocity of the triangle """
        self.yvelocity = newYVelocity

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
        """ return the y coordinate of the triangle """
        return self.xvelocity

    def getYVelocity(self):
        """ return the y coordinate of the triangle """
        return self.yvelocity

    def calculateTriangleVertices(self):
        """Calculate the vertices of a triangle. Points are located 0, 2*pi/3, and \
        4*pi/3 around the center at 'radius' distance away."""

        # now we will calculate the list of vertices required to draw the triangle
        numberOfVertices = 3  # specify the number of vertices we need for the shape
        vertices = []  # initialize a list of vertices

        angles = [0.0, (2.0 / 3.0) * math.pi,
                  (4.0 / 3.0) * math.pi]  # specify the first vertex of the triangle (x,y values)
        x = [self.getRadius() * math.cos(angle) + self.getX() for angle in angles]
        y = [self.getRadius() * math.sin(angle) + self.getY() for angle in angles]
        for i in range(0, len(x)):
            vertices.append(x[i])
            vertices.append(y[i])

        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
        return vertexList