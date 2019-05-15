import pyglet
import pyglet.gl
from pyglet.window import key
from player import playerClass
from background import backgroundClass
from pillar import pillarClass
from random import uniform


class graphicsWindow(pyglet.window.Window):

    # Responsible for initializing the important data structures required
    def __init__(self):

        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        # If game is idle or in play
        self.in_play = False

        # Floor and roof
        self.floor = self.height * 0
        self.roof = self.height * 1

        # Range of pillar heights
        self.gap_range = [self.height * 0.2, self.height * 0.8]
        self.gap_width = 0.15 * self.height

        # Initial pillar speed
        self.pillar_speed_init = 100
        self.pillar_speed = self.pillar_speed_init


    def update(self, dt):
        """ Procedure to update the game at each time step """

        # Background scroll
        for slates in BG:
            slates.scroll(dt)

            # Loop background if it goes off screen
            if (slates.x < -slates.width):
                slates.x = 2 * slates.width


        # In-Game
        if (self.in_play):

            # Fall due to gravity
            player.fall(dt)

            # Fail states
            if (player.y < self.floor) or (player.y > self.roof):
                self.fail()

            if check_hitbox(player, beams):
                self.fail()




            for beam in beams:

                # Move pillars
                beam.scroll(dt)

            # Reset pillars if they go off screen
            if (beams[0].x < -beams[0].width):

                self.pillar_speed += 10

                for beam in beams:
                    # Set positions to right of screen
                    beam.x = self.width

                    # Set beam speeds
                    beam.speed = self.pillar_speed

                # Randomly select a height
                gap_centre = uniform(*self.gap_range)

                # Set beam heights
                beams[0].y = gap_centre - self.gap_width
                beams[1].y = gap_centre + self.gap_width

        # Menu
        else:
            pass



    def fail(self):
        """ Procedure for when the game enters a fail state """

        # Reset to menu mode
        self.in_play = False

        # Reset player positions
        player.y = player.start_y

        # Reset pipes
        self.pillar_speed = self.pillar_speed_init

        for beam in beams:

            # Set positions to right of screen
            beam.x = self.width

            # Set beam speeds
            beam.speed = self.pillar_speed


        # Randomly select a height
        gap_centre = uniform(*self.gap_range)

        # Set beam heights
        beams[0].y = gap_centre - self.gap_width
        beams[1].y = gap_centre + self.gap_width

        return



    def on_key_press(self, symbol, modifiers):
        """ Procedure upon key press """

        # In-Game
        if (self.in_play):

            if (symbol == key.UP) or (symbol == key.SPACE):
                player.jump()

        # Menu
        else:

            # Start game
            if (symbol == key.UP) or (symbol == key.SPACE):
                self.in_play = True
                player.jump()


            # Change player model
            elif (symbol == key.LEFT):
                player.change_model('L')

            elif (symbol == key.RIGHT):
                player.change_model('R')



    def on_draw(self):
        """ Draw objects """

        # Clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        for slates in BG:
            slates.draw()

        for beam in beams:
            beam.draw()

        player.draw()


def check_hitbox(player, beams):

    # Get player hitbox
    player_left, player_right, player_bottom, player_top = player.hitbox()

    # Check bottom beam collision
    beam_left, beam_right, beam_height = beams[0].hitbox()

    if (player_bottom < beam_height):

        if (beam_left < player_right) and (player_right < beam_right):
            return True

        elif (beam_left < player_left) and (player_left < beam_right):
            return True

        else:
            return False

    # Check top beam collision
    beam_left, beam_right, beam_height = beams[1].hitbox()

    if (player_top > beam_height):

        if (beam_left < player_right) and (player_right < beam_right):
            return True

        elif (beam_left < player_left) and (player_left < beam_right):
            return True

        else:
            return False






# Main game engine loop
if __name__ == '__main__':

    # Create an instance of a window
    window = graphicsWindow()

    # Create background slates
    BG_speed = 50
    BG = []
    BG.append(backgroundClass(window_height=window.height, x=0, speed=BG_speed))
    BG.append(backgroundClass(window_height=window.height, x=BG[0].width, speed=BG_speed))
    BG.append(backgroundClass(window_height=window.height, x=2*BG[0].width, speed=BG_speed))

    # Create player model
    player = playerClass(window_width=window.width, window_height=window.height)

    # Create pillars
    beams = [pillarClass(side='bottom'), pillarClass(side='top')]

    # Set to menu
    window.fail()

    # Input the time step
    dt = 1. / 60.
    pyglet.clock.schedule_interval(window.update, dt)

    # Run
    pyglet.app.run()

