import triangle
import pyglet
import pyglet.gl
import physics
import numpy as np


class GraphicsWindow(pyglet.window.Window):
    def __init__(self, width=2560, height=1600, camera=None, walls=None, sprites=None, *args, **kwargs):
        super(GraphicsWindow, self).__init__(*args, **kwargs)
        self.width = width
        self.height = height
        self.camera = camera
        self.walls = walls
        self.sprites = sprites
        self.mouse_frames = 0

    def update(self, dt):
        """
        Updates the triangles by moving them
        through their color space and real space.
        """
        for this_shape in self.sprites:
            this_shape.translate(this_shape.velocity * dt)
            this_shape.rotate(this_shape.angular_velocity * dt)
            this_shape.color_translate(this_shape.color_velocity * dt)
        for this_shape in self.walls:
            this_shape.translate(this_shape.velocity * dt)
            this_shape.rotate(this_shape.angular_velocity * dt)
            this_shape.color_translate(this_shape.color_velocity * dt)

    def on_resize(self, width, height):
        """
        Sets the correct projection parameters
        when we resize the window (or create it.
        :param width:
        :param height:
        :return:
        """
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D,
                                  pyglet.gl.GL_TEXTURE_MIN_FILTER,
                                  pyglet.gl.GL_LINEAR_MIPMAP_LINEAR);
        pyglet.gl.gluPerspective(85, width / float(height), .1, 1000)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        self.set_exclusive_mouse(True)
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        """
        Moves the player around.
        TODO: Make it relative to camera position.
        :param symbol:
        :param modifiers:
        :return:
        """
        MOVE_SPEED = 1.0
        if symbol == pyglet.window.key.RIGHT or symbol == pyglet.window.key.D:
            self.camera.vel[0] = -MOVE_SPEED
        elif symbol == pyglet.window.key.UP or symbol == pyglet.window.key.W:
            self.camera.vel[2] = MOVE_SPEED
        elif symbol == pyglet.window.key.DOWN or symbol == pyglet.window.key.S:
            self.camera.vel[2] = -MOVE_SPEED
        elif symbol == pyglet.window.key.LEFT or symbol == pyglet.window.key.A:
            self.camera.vel[0] = MOVE_SPEED
        elif symbol == pyglet.window.key.ESCAPE:
            exit()
        else:
            print(symbol, "not recognised")

    def on_key_release(self, symbol, modifiers):
        """
        Detects when a key is released and resets
        the camera velocity.
        :param symbol:
        :param modifiers:
        :return:
        """
        if symbol == pyglet.window.key.RIGHT or symbol == pyglet.window.key.D:
            self.camera.vel[0] = 0.0
        elif symbol == pyglet.window.key.UP or symbol == pyglet.window.key.W:
            self.camera.vel[2] = 0.0
        elif symbol == pyglet.window.key.DOWN or symbol == pyglet.window.key.S:
            self.camera.vel[2] = 0.0
        elif symbol == pyglet.window.key.LEFT or symbol == pyglet.window.key.A:
            self.camera.vel[0] = 0.0

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Deals with firing code.
        TODO: Separate the firing code.
        :param x:
        :param y:
        :param button:
        :param modifiers:
        :return:
        """
        if button == pyglet.window.mouse.LEFT:
            a = (pyglet.gl.GLfloat * 16)()
            mvm = pyglet.gl.glGetFloatv(pyglet.gl.GL_MODELVIEW_MATRIX, a)
            forward_vector = np.array([-list(a)[2], list(a)[6], -list(a)[10]])
            forward_vector = forward_vector / np.sqrt(np.dot(forward_vector, forward_vector))
            self.mouse_frames = 10
            deadsprite = None
            max_dist = 10000

            for sprite in self.sprites:
                distance = sprite.line_intersection(np.array([0.0,0.0,0.0]), forward_vector)
                if distance and distance > 0.0:
                    if distance < max_dist:
                        max_dist = distance
                        if sprite.is_inside(distance * forward_vector):
                            print(distance, sprite.texture_filename)
                            deadsprite = sprite

            newsprites = []
            for sprite in self.sprites:
                if sprite is not deadsprite:
                    newsprites.append(sprite)

            self.sprites = newsprites


    def on_mouse_motion(self, x, y, dx, dy):
        """
        Mouse look handler -- looks left and right
        depending on how far x the mouse moves.
        :param x:
        :param y:
        :param dx:
        :param dy:
        :return:
        """
        sensitivity = 0.2
        # pyglet.gl.glRotatef(sensitivity * dy, -1.0, 0.0, 0.0)
        pyglet.gl.glRotatef(sensitivity * dx, 0.0, 1.0, 0.0)

    def draw_set(self, shapes):
        """
        Draws a batch of shapes.
        :param shapes:
        :return:
        """

        textured_batch = pyglet.graphics.Batch()
        untextured_batch = pyglet.graphics.Batch()

        for this_shape in shapes:
            this_shape.translate(self.camera.vel)
            for this_triangle in this_shape.triangle_list():

                if this_triangle.texture:
                    pyglet.gl.glColor3f(1.0, 1.0, 1.0)
                    vertex_list = textured_batch.add(3, pyglet.gl.GL_TRIANGLES,
                                                     pyglet.graphics.TextureGroup(this_triangle.texture),
                                                     ('v3f', this_triangle.vertex_list),
                                                     ('t2f', this_triangle.texture_list))
                else:
                    pyglet.gl.glColor3f(this_triangle.color[0], this_triangle.color[1], this_triangle.color[2])
                    triangle_color = [this_triangle.color[:3] for _ in range(3)]
                    triangle_color = [item for sublist in triangle_color for item in sublist]
                    vertex_list = untextured_batch.add(3, pyglet.gl.GL_TRIANGLES, None,
                                                       ('v3f', this_triangle.vertex_list),
                                                       ("c3f", triangle_color))
        untextured_batch.draw()
        textured_batch.draw()

    def on_draw(self):
        """
        Overrides the Pyglet on_draw method,
        to update our triangles. This is called
        every frame and propagates the triangles
        through space.
        :return:
        """
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        pyglet.gl.glClear(pyglet.gl.GL_DEPTH_BUFFER_BIT)

        pyglet.gl.glEnable(pyglet.graphics.GL_DEPTH_TEST)
        pyglet.gl.glDepthFunc(pyglet.gl.GL_LESS)

        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glEnable(pyglet.graphics.GL_ALPHA_TEST)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

        self.draw_set(self.walls)
        self.draw_set(self.sprites)

        a = (pyglet.gl.GLfloat * 16)()
        mvm = pyglet.gl.glGetFloatv(pyglet.gl.GL_MODELVIEW_MATRIX, a)
        forward_vector = np.array([list(a)[2], list(a)[6], -list(a)[10]])
        forward_vector = forward_vector / np.sqrt(np.dot(forward_vector, forward_vector))
        if self.mouse_frames:
            pyglet.gl.glColor3d(1, 0.875, 0)
            pyglet.gl.glLineWidth(10.0);
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ("v3f", (0, -50.0, 0.0, -forward_vector[0] * 10, 0.0, forward_vector[2] * 10.0))
                             )
            self.mouse_frames -= 1
        physics.check_collision(walls=self.walls, sprites=self.sprites)