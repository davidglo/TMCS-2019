import pyglet
from random import uniform

class pillarClass(pyglet.sprite.Sprite):
    """ Class for pillar/pipe obstacle """

    def __init__(self, side, x=0, y=0, speed=0):

        if (side == 'bottom'):

            # Load image into sprite
            image = pyglet.image.load("assets/beam_bottom.png")
            image.anchor_y = image.height

        elif (side == 'top'):

            # Load image into sprite
            image = pyglet.image.load("assets/beam_top.png")

        # Create sprite
        super().__init__(image)

        # Scale image to be 64x64 px
        self.scale = 1.0 / 1.5

        # Starting position and speed
        self.x = x
        self.y = y
        self.speed = speed



    def scroll(self, dt):
        """ Scroll the pillar along the screen """

        # Move the pillar
        self.x -= (self.speed * dt)


    def reset(self, speed, window_width, lower_bound, upper_bound):

        self.x = window_width
        self.y = uniform(lower_bound, upper_bound)

        self.speed = speed

        return


    def hitbox(self):

        return self.x, self.x + self.width, self.y





