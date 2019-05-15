"""A code to create two colored triangles moving around"""

import pyglet
import pyglet.gl
import math
from random import randint
import colors
from triangleClass import triangleClass
from pyglet.window import key

SCORE = 0
CLOCK = 0

difficulty = {"easy":15, "medium":10, "hard":5}
setDifficulty = "medium"

# initialize the triangles that we will be drawing
# initialize a list of triangles
triangles = []

# populate the list of triangles
triangles.append(triangleClass('triangle1', 'blue',    0, 0, 20))
triangles.append(triangleClass('triangle2', 'hotpink', 0, 0, 20))
triangles.append(triangleClass('triangle3', 'red', 0, 0, 10))
triangles.append(triangleClass('triangle4', 'yellow', 0, 0, 20))
triangles.append(triangleClass('triangle5', 'sienna', 0, 0, 10))
triangles.append(triangleClass('triangle5', 'orange', 0, 0, 25))

triangles.append(triangleClass('mytriangle', 'green', 0, 0, 30))

triangles[0].setVelocity(1,1)
triangles[1].setVelocity(2,0.5)
triangles[2].setVelocity(-2,0.5)
triangles[3].setVelocity(2,-0.5)
triangles[4].setVelocity(5,-1)
triangles[5].setVelocity(-3,-4)
triangles[6].setVelocity(5,5)


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        for i in range(0, len(triangles)):
            triangles[i].setCentreCoordinates(self.width / 2, self.height / 2)
            triangles[i].updateVertices()
            triangles[i].setThetaIncrement(5 * i)
        triangles[-1].setThetaIncrement(5)
        triangles[-1].setSpeed(3)
        colors.printAvailableColors()


    def on_key_press(self,symbol, modifiers):
        global setDifficulty

        if symbol == key._1:
            setDifficulty = "easy"
        elif symbol == key._2:
            setDifficulty = "medium"
        elif symbol == key._3:
            setDifficulty = "hard"

        if symbol == key.PLUS:
            triangles[-1].setSpeed(triangles[-1].getSpeed()+1)
        elif symbol == key.MINUS:
            triangles[-1].setSpeed(triangles[-1].getSpeed() - 1)

        if symbol == key.RIGHT:
            triangles[-1].setCentreCoordinates(triangles[-1].getX()+triangles[-1].getSpeed(), triangles[-1].getY())
        elif symbol == key.UP:
            triangles[-1].setCentreCoordinates(triangles[-1].getX(), triangles[-1].getY()+triangles[-1].getSpeed())
        elif symbol == key.DOWN:
            triangles[-1].setCentreCoordinates(triangles[-1].getX(), triangles[-1].getY()-triangles[-1].getSpeed())
        elif symbol == key.LEFT:
            triangles[-1].setCentreCoordinates(triangles[-1].getX()-triangles[-1].getSpeed(), triangles[-1].getY())

    def update(self, dt):
        global SCORE, difficulty, setDifficulty, CLOCK
        print("Updating the center of the triangle")
        CLOCK += 1
        for i in range(0, len(triangles)-1):
            triangles[i].updatePosition(window.width, window.height)
            triangles[i].updateVertices()
            triangles[i].updateTheta()
            triangles[i].rotateVertices()

        triangles[-1].updateVertices()
        triangles[-1].updateTheta()
        triangles[-1].rotateVertices()

        if CLOCK > 200:
            for i in range(0, len(triangles)-1):
                for j in range(i+1, len(triangles)-1):
                    if (abs(triangles[i].getX() - triangles[j].getX()) < 5) and (abs(triangles[i].getY() - triangles[j].getY()) < 5):
                        SCORE -= 1
                        explosion.play()

            for i in range(0,len(triangles)-1):
                if (abs(triangles[i].getX() - triangles[-1].getX()) < difficulty[setDifficulty]) and (
                        abs(triangles[i].getY() - triangles[-1].getY()) < difficulty[setDifficulty]):
                    SCORE += 1
                    coin.play()

    def on_draw(self):
        global SCORE, setDifficulty, CLOCK
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        for i in range(0, len(triangles)):
            vertexList = triangles[i].getVertices()
            # now use pyGlet commands to draw lines between the vertices
            linecolor = triangles[i].color
            pyglet.gl.glColor3f(colors.color[linecolor][0], colors.color[linecolor][1], colors.color[linecolor][2])  # specify colors
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw
        pyglet.text.Label('Speed = ' + str(triangles[-1].getSpeed()),font_name='Times New Roman',font_size=10,x=5, y=window.height - 5,anchor_x='left', anchor_y='top').draw()
        pyglet.text.Label('Score = ' + str(SCORE), font_name='Times New Roman', font_size=10,x=window.width-5,
                              y=window.height - 5, anchor_x='right', anchor_y='top').draw()
        pyglet.text.Label('Difficulty = ' + setDifficulty, font_name='Times New Roman', font_size=10, x=window.width // 2,
                              y=window.height - 5, anchor_x='center', anchor_y='top').draw()

        if CLOCK > 0 and CLOCK <30:
            pyglet.text.Label('3', font_name='Times New Roman', font_size=25,
                              x=window.width // 2,
                              y=window.height //2, anchor_x='center', anchor_y='center').draw()
            pyglet.resource.media('Blip_Select.wav', streaming=False).play()
        if CLOCK > 50 and CLOCK <80:
            pyglet.text.Label('2', font_name='Times New Roman', font_size=25,
                              x=window.width // 2,
                              y=window.height //2, anchor_x='center', anchor_y='center').draw()
            pyglet.resource.media('Blip_Select.wav', streaming=False).play()
        if CLOCK > 100 and CLOCK <130:
            pyglet.text.Label('1', font_name='Times New Roman', font_size=25,
                              x=window.width // 2,
                              y=window.height //2, anchor_x='center', anchor_y='center').draw()
            pyglet.resource.media('Blip_Select.wav', streaming=False).play()
        if CLOCK > 150 and CLOCK <200:
            pyglet.text.Label('GO', font_name='Times New Roman', font_size=25,
                              x=window.width // 2,
                              y=window.height //2, anchor_x='center', anchor_y='center').draw()
            pyglet.resource.media('Powerup4.wav', streaming=False).play()

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    explosion = pyglet.resource.media('explosion.wav', streaming=False)
    coin = pyglet.resource.media('Pickup_Coin.wav', streaming=False)
    pyglet.clock.schedule_interval(window.update, 1 / 40.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet