import pyglet
import pyglet.gl
import colours
from triangleClass import triangleClass
from random import randint

# initialize a list of triangles
triangles = []

# populate the list of triangles
for i in range(100):
    if (i%5 == 0):
        triangles.append(triangleClass('triangle'+ str(i), 'blue', 0, 0, 20))
    elif (i % 3 == 0):
        triangles.append(triangleClass('triangle' + str(i), 'yellow', 0, 0, 20))
    else:
        triangles.append(triangleClass('triangle'+ str(i), 'hotpink', 0, 0, 20))


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        for i in range(0, len(triangles)):
            triangles[i].setCentreCoordinates(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))
            triangles[i].updateVertices()
            triangles[i].setVelocity(i + 100, i + 200)
            triangles[i].setThetaIncrement(10 * i)

    def update(self, dt):
        print("Updating the center of the triangle")
        for i in range(0, len(triangles)):
            triangles[i].updateCoordinates(self.width, self.height)
            triangles[i].updateVertices()
            triangles[i].updateTheta()
            triangles[i].rotateVertices()

    def on_draw(self):
        # clear the graphics bufferx
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        label_1 = pyglet.text.Label('Select all the faces', x=window.width // 2, y=window.height - 20, font_name='Times New Roman',
                                  font_size= 15,
                                  anchor_x ='center', anchor_y='center')
        label_1.draw()

        score_no = 0
        score = 'Score' +' ' + str(score_no)
        label_2 = pyglet.text.Label(score, x=window.width - 60, y=window.height - 20,
                                    font_name='Times New Roman',
                                    font_size=15,
                                    anchor_x='center', anchor_y='center')
        label_2.draw()

        image = pyglet.resource.image('logan.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

        for i in range(0, len(triangles)):
            # now we will calculate the list of vertices required to draw the triangle
            vertexList = triangles[i].getVertices()

            # now use pyGlet commands to draw lines between the vertices
            lineColor = triangles[i].color
            pyglet.gl.glColor3f(colours.color[lineColor][0], colours.color[lineColor][1],
                            colours.color[lineColor][2])  # specify colors
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw
            for i in range(0, len(triangles)):
                if (triangles[i].color == 'yellow'):
                    image.blit(triangles[i].x, triangles[i].y)

    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            for i in range(0, len(triangles)):
                x_min = triangles[i].x - triangles[i].radius
                x_max = triangles[i].x + triangles[i].radius
                y_min = triangles[i].x - triangles[i].radius
                y_max = triangles[i].x + triangles[i].radius
                if( x>x_min and x< x_max):
                    if(y>y_min and y< y_max):
                        del triangles[i]
                score_no += 1


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 0.5)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet