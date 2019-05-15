import pyglet


class playerClass(pyglet.sprite.Sprite):
    """ Class inherited from pyglet sprite """

    def __init__(self, window_width, window_height):

        # Load player models
        self.models = models()
        self.models_index = 0
        self.n_models = len(self.models)
        super().__init__(self.models[self.models_index])

        # Scale
        self.scale = 0.5

        # Calculate starting positions
        self.x = 0.5 * (window_width - self.width)

        self.start_y = 0.5 * (window_height - self.height)
        self.y = self.start_y

        # Acceleration due to gravity
        self.accel = -400.

        # Initial velocity
        self.velocity = 0.

        # Jump velocity
        self.jump_vel = 200.


    def fall(self, dt):
        """ Fall due to gravity """

        # Initial height and velocity
        h = self.y
        v = self.velocity

        # Integrate motion under constant force due to gravity
        h += (v + (0.5 * self.accel * dt)) * dt
        v += self.accel * dt

        # Reassign values
        self.y = h
        self.velocity = v

        return


    def jump(self):
        """ Jump upwards """
        self.velocity = self.jump_vel

        return


    def change_model(self, direction):

        # Decreaasing
        if (direction == 'L'):

            if (self.models_index == 0):
                self.models_index = self.n_models - 1

            else:
                self.models_index -= 1

        # Increasing
        else:

            if (self.models_index == self.n_models - 1):
                self.models_index = 0

            else:
                self.models_index += 1

        # Change image
        self.image = self.models[self.models_index]


    def hitbox(self):
        """ Returns the top-right and bottom-right hitbox coordinates of the player model """

        left = self.x
        right_x = self.x + self.width
        lower_y = self.y
        upper_y = self.y + self.height
        return left, right_x, lower_y, upper_y


def models():

    # Construct list of filenames
    filenames = ['logan',
                 '80snallan', '80swilson', 'badboybarford', 'galpin', 'glowacki', 'karl', 'khalid',
                 'kmz', 'leema', 'lennart', 'manby', 'mano', 'mulholland', 'nallan'
                 ]

    images = []

    for i in range(len(filenames)):

        image = pyglet.image.load('assets/faces/'+filenames[i]+'.png')
        images.append( image )

    return images




