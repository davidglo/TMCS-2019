import pyglet.gl
from get_triangle_function import *


name_colors = ['yellow', 'blue', 'red', 'green', 'sienna', 'hotpink']
number_colors = [[1.0, 1.0, 0.0],[0.0, 0.0, 1.0],[1.0, 0.0, 0.0],[0.0, 1.0, 0.0],[0.627, 0.322, 0.176],[1.0, 0.412, 0.706]]

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()            # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]  # initialize the centre of the triangle
        self.center2 = [self.width / 2, self.height / 2]  # initialize the centre of the triangle

    def update(self, dt):
        print("Updating the center of the triangle")
        self.center1 = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # now we will calculate the list of vertices required to draw the triangle
        numberOfVertices = 3       # specify the number of vertices we need for the shape
        radius = 100               # specify the radius of each point from the center
        num_triangles = 5          # number of trippy triangles in one group
        num_groups = 10            # number of groups of triangles

        for i in range(num_groups):


            scale_factor_x = 2 * random.randint(0,2) - 1
            scale_factor_y = 2 * random.randint(0, 2) - 1

            for triangle in range(num_triangles):
                #radius = random.randint(50, 100)
                xcenter = self.center1[0]  # specify xcenter
                ycenter = self.center1[1]  # specify ycenter
                xcenter = xcenter - 10*triangle + i*100*scale_factor_x
                ycenter = ycenter - 10*triangle + i*100*scale_factor_y
                vertexList = get_triangle(radius, xcenter, ycenter, numberOfVertices)
                print(vertexList)

                # randomly generate colors
                k = random.randint(0,len(name_colors)-1)
                linecolor_1, linecolor_2, linecolor_3 = number_colors[k][0], number_colors[k][1], number_colors[k][2]

                # now use pyGlet commands to draw lines between the vertices
                pyglet.gl.glLineWidth(5.0)                                    # specify line width
                pyglet.gl.glColor3f(linecolor_1, linecolor_2, linecolor_3)    # specify colors
                vertexList.draw(pyglet.gl.GL_LINE_LOOP)                       # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet