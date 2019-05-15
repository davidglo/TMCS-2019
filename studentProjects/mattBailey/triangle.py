"""
A triangle class, structured as three vertices and
some velocities through space, angles, and colorspace.
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import colors
import pyglet

def generate_rotation_matrix(angle, axis):
    if axis == "z":
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                    [np.sin(angle), np.cos(angle), 0],
                                    [0, 0, 1]])
    elif axis == "y":
        rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                                    [0, 1, 0],
                                    [-np.sin(angle), 0, np.cos(angle)]])
    elif axis == "x":
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(angle), -np.sin(angle)],
                                    [0, np.sin(angle), np.cos(angle)]])

    return rotation_matrix


class Shape():
    def __init__(self, vertices,
                 velocity=np.array([0.0, 0.0, 0.0]),
                 angular_velocity=np.array([0.0, 0.0, 0.0]),
                 colormap=plt.get_cmap("viridis"),
                 color_location=0.0,
                 color_velocity=0.0):
        self.velocity = velocity
        self.angular_velocity = angular_velocity
        self.vertices = vertices
        self.color_location = color_location
        self.color_velocity = color_velocity
        self.colormap = colormap
        self.color = self.colormap(self.color_location)
        self.number_of_vertices = self.vertices.shape[0]

    @property
    def centre(self):
        return np.mean(self.vertices, axis=0)

    def translate(self, offset):
        """
        Translates the shape in 3D space
        by a numpy array.

        :param offset:
        :return:
        """
        self.vertices += offset

    def rotate(self, angles):
        """
        Rotates the shape in 3D
        space about a vector of angles [R_x, R_y, R_z]
        :param angles:
        :return:
        """
        axes = ["x", "y", "z"]
        old_centre = self.centre
        self.translate(-old_centre)
        for i, angle in enumerate(angles):
            rotation_matrix = generate_rotation_matrix(angle, axes[i])
            self.vertices = np.matmul(self.vertices, rotation_matrix)

        self.translate(old_centre)

    def color_translate(self, offset):
        """
        Translates through the linear colorspace
        of the triangle.
        :param offset:
        :return:
        """
        self.color_location += offset
        if self.color_location >= 1.0:
            self.color_location -= 1.0
        elif self.color_location < 0.0:
            self.color_location += 1.0
        self.color = self.colormap(self.color_location)

class Square(Shape):
    def __init__(self, vertex_1, vertex_2, vertex_3, vertex_4,
                 velocity=np.array([0.0, 0.0, 0.0]),
                 angular_velocity=np.array([0.0, 0.0, 0.0]),
                 texture_vertices=np.array([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]),
                 texture=None,
                 *args, **kwargs):
        self.vertices = np.array([vertex_1, vertex_2, vertex_3, vertex_4])
        self.velocity = velocity
        self.angular_velocity = angular_velocity
        self.texture_vertices = texture_vertices
        self.texture_filename = texture
        if texture is not None:
            self.texture = pyglet.image.load(texture).get_texture()
        else:
            self.texture = None


        Shape.__init__(self, vertices=self.vertices,
                       velocity=velocity,
                       angular_velocity=angular_velocity,
                       *args,
                       **kwargs)

    @property
    def vec_1(self):
        return self.vertices[1, :] - self.vertices[0, :]

    @property
    def vec_2(self):
        return self.vertices[3, :] - self.vertices[0, :]

    @property
    def vec_norm(self):
        """
        Constructs a normal vector from the two
        side vectors.
        :return:
        """
        vec_norm = np.cross(self.vec_1, self.vec_2)
        if np.dot(vec_norm, self.vec_1) > 0.001:
            print("Error, normal vector not normal to vec 1")
        if np.dot(vec_norm, self.vec_2) > 0.001:
            print("Error, normal vector not normal to vec 2")
        if np.dot(self.vec_2, self.vec_1) > 0.001:
            print("Error, vec_1 not normal to vec 1")

        return vec_norm / np.sqrt(np.dot(vec_norm, vec_norm))

    @property
    def plane_d(self):
        return np.dot(self.vec_norm, self.vertices[0, :])

    def distance_to(self, point):
        """

        Calculates the distance to a point from this plane.
        We can skip the normalising it because we know
        how long the unit vector is (1)
        :param point:
        :return:
        """
        distance = (np.dot(point, self.vec_norm) - self.plane_d)
        return distance

    def line_intersection(self, origin, vector):
        """
        Checks the intersection of a line in the form
        origin + lambda vector, and return the number of lambdas
        required to intersect with this plane.
        :param origin:
        :param vector:
        :return:
        """
        is_parallel = np.dot(vector, self.vec_norm)
        if is_parallel > 1e-4:
            return (self.plane_d - np.dot(origin, self.vec_norm)) / is_parallel
        return None

    def is_inside(self, point):
        """
        Checks if a point in the plane of the square
        is inside the square.
        :param point:
        :return:
        """
        vec_to_point = point - self.vertices[0, :]
        proj_1 = np.dot(vec_to_point, self.vec_1) / np.sqrt(np.dot(self.vec_1, self.vec_1))
        proj_2 = np.dot(vec_to_point, self.vec_2) / np.sqrt(np.dot(self.vec_2, self.vec_2))
        if proj_1 < 0.0 or proj_2 < 0.0:
            return False
        return True

    def triangle_list(self):
        return [Triangle(self.vertices[0, :], self.vertices[1, :], self.vertices[2, :],
                         colormap=self.colormap, color_location=self.color_location,
                         color_velocity=self.color_velocity, texture=self.texture,
                         texture_vertices=np.array([self.texture_vertices[0, :],
                                                    self.texture_vertices[1, :],
                                                    self.texture_vertices[2, :]])),
                Triangle(self.vertices[3, :],
                         self.vertices[2, :],
                         self.vertices[0, :],
                         colormap=self.colormap, color_location=self.color_location,
                         color_velocity=self.color_velocity, texture=self.texture,
                         texture_vertices=np.array([self.texture_vertices[3, :],
                                                    self.texture_vertices[2, :],
                                                    self.texture_vertices[0, :]]))]


class Triangle(Shape):
    def __init__(self, vertex_1, vertex_2, vertex_3,
                 velocity=np.array([0.0, 0.0, 0.0]),
                 angular_velocity=np.array([0.0, 0.0, 0.0]),
                 colormap=plt.get_cmap("viridis"),
                 color_location=0.0,
                 color_velocity=0.0,
                 texture_vertices=np.array([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]),
                 texture=None):
        self.vertices = np.array([vertex_1, vertex_2, vertex_3])
        self.texture_vertices = texture_vertices
        self.texture = texture
        Shape.__init__(self,
                       vertices=self.vertices,
                       velocity=velocity,
                       angular_velocity=angular_velocity,
                       colormap=colormap,
                       color_location=color_location,
                       color_velocity=color_velocity)

    @property
    def vertex_list(self):
        return tuple(self.vertices.ravel())

    @property
    def texture_list(self):
        return tuple(self.texture_vertices.ravel())

    def triangle_list(self):
        return [self]
