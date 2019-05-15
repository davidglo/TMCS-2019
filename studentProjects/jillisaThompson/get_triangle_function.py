import pyglet
import pyglet.gl
import random
import math
from random import randint

def get_triangle(radius, xcenter, ycenter, numberOfVertices):

    """
    This function takes an (x,y) coordinate and a triangle
    radius to ouput the coordinates of the triangle as a
    list.

    :param radius: radius of the triangle
    :param xcenter: x center of the triangle
    :param ycenter: y center of the triangle
    :param numberOfVertices: number of vertices
    :return: returns list of coordinates of the vertices

    """


    angles = [0.0, (2. / 3.0) * math.pi, (4.0 / 3.0) * math.pi]

    vertices = []

    for angle in range(0, len(angles)):
        x = radius * math.cos(angles[angle]) + xcenter
        y = radius * math.sin(angles[angle]) + ycenter
        vertices.append(x)  # append the x value to the vertex list
        vertices.append(y)  # append the y value to the vertex list

    # convert the vertices list to pyGlet vertices format
    vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))

    return vertexList