import triangle
import numpy as np
import random

COLLISION_RADIAL = 4.0
MAX_SPEED = 20.0
COLLISION_WALL = 1.5 * MAX_SPEED / 60.0

def check_collision(walls, sprites):
    """

    Checks collision between sprites and other
    sprites, at which point they swap
    velocities and their angular
    velocity is minimised,
    and between sprites and walls
    which reverses the sprites.
    :param walls:
    :param sprites:
    :return:
    """
    # Is there a better way to do pairwise sums?
    # Sprite collision is radial
    for index in range(len(sprites)):
        item = sprites[index]
        for otherindex in range(index):
            otheritem = sprites[otherindex]
            distance = np.sqrt(np.dot(otheritem.centre - item.centre, otheritem.centre - item.centre))
            if np.abs(distance) < COLLISION_RADIAL:
                temp_velocity = item.velocity
                item.velocity = otheritem.velocity
                otheritem.velocity = temp_velocity
                item.angular_velocity = np.array([random.uniform(-1.0, 1.0) for _ in range(3)])
                otheritem.angular_velocity = np.array([random.uniform(-1.0, 1.0) for _ in range(3)])

    for sprite in sprites:
        for wall in walls:
            distance = wall.distance_to(sprite.centre)
            if np.abs(distance) < COLLISION_WALL:
                closest_point = sprite.centre - (distance * wall.vec_norm)
                if wall.is_inside(closest_point):
                    sprite.velocity *= random.uniform(-1.0/1.25, -1.25)
                    sprite.angular_velocity = np.array([random.uniform(-1.0, 1.0) for _ in range(3)])