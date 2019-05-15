"""
A Simple Camera Class
"""
import numpy as np
class Camera():
    def __init__(self, vel, angle_vel=np.array([0.0,0.0,0.0])):
        self.vel = vel
        self.angle_vel = angle_vel
