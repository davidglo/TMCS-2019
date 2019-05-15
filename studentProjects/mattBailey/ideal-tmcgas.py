#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:22:54 2019

@author: matthew-bailey
"""
import numpy as np

import pyglet
import pyglet.gl
import random
import triangle
import camera
import graphicswindow

import physics
MAX_SPEED = physics.MAX_SPEED


def sprite_from_name(filename):
    """
    Generates a sprite from the name of a
    file -- should be a 2^n x 2^n png
    :param filename:
    :return:
    """
    shape = triangle.Square(np.array([10, 10, DEPTH]), np.array([10, -10, DEPTH]),
                           np.array([-10, -10, DEPTH]), np.array([-10, 10, DEPTH]),
                           angular_velocity=np.array([0.0, 0.0, -0.5]),
                           velocity=np.array([random.uniform(-MAX_SPEED, MAX_SPEED),
                                              0.0,
                                              random.uniform(-MAX_SPEED, MAX_SPEED)]),
                           texture_vertices=np.array([[1, 1], [1, 0], [0, 0], [0, 1]]),
                           texture=filename)
    shape.translate(np.array([random.uniform(-10, 10) for _ in range(3)]))
    return shape


# this is the main game engine loop
if __name__ == "__main__":
    DEPTH = -20.0

    FLOOR = triangle.Square(np.array([1000, 1000, DEPTH]), np.array([1000, -1000, DEPTH]),
                            np.array([-1000, -1000, DEPTH]), np.array([-1000, 1000, DEPTH]),
                            angular_velocity=np.array([0.0, 0.0, 0.0]),
                            color_location=0.5
                            )
    FLOOR.rotate(np.array([np.pi / 2, 0.0, 0.0]))
    FLOOR.translate(np.array([0.0, -20.0, 0.0]))

    CEILING = triangle.Square(np.array([1000, 1000, DEPTH]), np.array([1000, -1000, DEPTH]),
                              np.array([-1000, -1000, DEPTH]), np.array([-1000, 1000, DEPTH]),
                              angular_velocity=np.array([0.0, 0.0, 0.0]),
                              color_location=0.75)
    CEILING.rotate(np.array([np.pi / 2, 0.0, 0.0]))
    CEILING.translate(np.array([0.0, 20.0, 0.0]))

    RIGHTWALL = triangle.Square(np.array([100, 100, DEPTH]), np.array([100, -100, DEPTH]),
                                np.array([-100, -100, DEPTH]), np.array([-100, 100, DEPTH]),
                                angular_velocity=np.array([0.0, 0.0, 0.0]),
                                texture_vertices=np.array([[16, 16], [16, 0], [0, 0], [0, 16]]),
                                texture="./Resources/brick.png")
    RIGHTWALL.rotate(np.array([0.0, np.pi / 2, 0.0]))
    RIGHTWALL.translate(np.array([100.0, 0.0, 0.0]))
    LEFTWALL = triangle.Square(np.array([100, 100, DEPTH]), np.array([100, -100, DEPTH]),
                               np.array([-100, -100, DEPTH]), np.array([-100, 100, DEPTH]),
                               angular_velocity=np.array([0.0, 0.0, 0.0]),
                               texture_vertices=np.array([[16, 16], [16, 0], [0, 0], [0, 16]]),
                               texture="./Resources/wood.png"
                               )
    LEFTWALL.rotate(np.array([0.0, np.pi / 2, 0.0]))
    LEFTWALL.translate(np.array([-100.0, 0.0, 0.0]))

    BACKWALL = triangle.Square(np.array([100, 100, 0.0]), np.array([100, -100, 0.0]),
                               np.array([-100.0, -100, 0.0]), np.array([-100.0, 100, 0.0]),
                               angular_velocity=np.array([0.0, 0.0, 0.0]),
                               texture_vertices=np.array([[16, 16], [16, 0], [0, 0], [0, 16]]),
                               texture="./Resources/dirt.png"
                               )

    FRONTWALL = triangle.Square(np.array([100, 100, -100.0]), np.array([100, -100, -100.0]),
                                np.array([-100, -100, -100.0]), np.array([-100, 100, -100.0]),
                                angular_velocity=np.array([0.0, 0.0, 0.0]),
                                texture_vertices=np.array([[16, 16], [16, 0], [0, 0], [0, 16]]),
                                texture="./Resources/log.png"
                                )

    filenames = ["./Resources/80swilson.png",
                 "./Resources/80snallan.png",
                 "./Resources/leema.png",
                 "./Resources/karl.png",
                 "./Resources/nallan.png",
                 "./Resources/glowacki.png",
                 "./Resources/manby.png",
                 "./Resources/mulholland.png",
                 "./Resources/badboybarford.png",
                 "./Resources/galpin.png",
                 "./Resources/kmz.png",
                 "./Resources/lennart.png",
                 "./Resources/logan.png",
                 "./Resources/mano.png"]

    SPRITES = [sprite_from_name(filename) for filename in filenames]
    CAMERA = camera.Camera(np.array([0.0, 0.0, 0.0]))
    WINDOW = graphicswindow.GraphicsWindow(walls=[FLOOR, CEILING, LEFTWALL, RIGHTWALL, BACKWALL, FRONTWALL],
                                           sprites=SPRITES,
                                           camera=CAMERA,
                                           fullscreen=False,
                                           width=1920,
                                           height=1080,
                                           caption='Ideal TMCgaS')
    # tell pyglet the on_draw() & update() timestep
    pyglet.clock.schedule_interval(WINDOW.update, 1 / 60.0)
    pyglet.app.run()
