import pyglet

class backgroundClass(pyglet.sprite.Sprite):
    """ Class for background slates """

    def __init__(self, window_height, x, speed):

        # Load image into sprite
        image = pyglet.image.load("assets/slates/backgroundColorForest.png")
        super().__init__(image)

        # Scale image to fill screen
        self.scale = window_height / self.height

        # Set speed at which the background scrolls
        self.speed = speed

        # Set positions
        self.x = x
        self.y = 0



    def scroll(self, dt):
        """ Background scroll """

        # Move the background
        self.x -= (self.speed * dt)

