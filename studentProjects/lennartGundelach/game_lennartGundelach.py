import pyglet
import pyglet.gl
import math
from random import randint
from pyglet.window import key
from pyglet.window import mouse
import color_mod
import random
import numpy



class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad,xvel,yvel,rvel):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.vertices = []
        self.radius = rad
        #self.numberOfVertices = 3  #specify the number of vertices we need for the shape
        self.numberOfVertices = 3
        #self.angles = [0.0, (2.0 / 3.0) * math.pi, (4.0 / 3.0) * math.pi]
        self.angles=[]

        if random.randrange(0,2) ==0:
            self.angles_set= 2
        else:
            self.angles_set =1


        for i in range(self.numberOfVertices):
            self.angles= [0.0 , self.angles_set * (math.pi /3.0 ), self.angles_set * (2*math.pi/3.0)]
        #self.angles = [0.0, (2.0 / 3.0) * math.pi, (3.0 / 3.0) * math.pi]
        self.vertexList = None
        self.xvelocity = xvel
        self.yvelocity = yvel
        self.rvelocity = rvel
        self.theta=60
        self.setRandomColor()

    def setRandomColor(self):
        key_list=list(color_mod.color.keys())
        number_of_keys=len(key_list)
        random_choice=random.randrange(0,number_of_keys)
        self.color=key_list[random_choice]

    def rotateVertices(self):
        """function to translate a set of coordinates to the (0,0) origin & then rotate them by some angle theta"""

        # translate vertices to the origin
        c = numpy.array([[self.vertices[0] - self.x, self.vertices[1] - self.y],
                         [self.vertices[2] - self.x, self.vertices[3] - self.y],
                         [self.vertices[4] - self.x, self.vertices[5] - self.y]])

        theta = (self.theta / 180.) * numpy.pi  # calculate theta in radians & the corresponding rotation matrix
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c, rotMatrix)  # matrix-matrix multiplication with numpy

        self.vertices = [c[0][0] + self.x, c[0][1] + self.y,  # translate the rotated vertices back to the center
                         c[1][0] + self.x, c[1][1] + self.y,
                         c[2][0] + self.x, c[2][1] + self.y]

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter


    def generate_triangle(self):
        # numberOfVertices, radius, xcenter, ycenter, angles
        """function to generate vertices of triangle"""
        self.vertices = []  # initialize a list of vertices
        for angle in self.angles:
            self.vertices.append(self.radius * math.cos(angle) + self.x)
            self.vertices.append(self.radius * math.sin(angle) + self.y)
        self.rotateVertices()
        self.vertexList = pyglet.graphics.vertex_list(self.numberOfVertices, ('v2f', self.vertices))
        return self.vertexList

    def update_theta(self):
        self.theta += self.rvelocity


    def update_position(self):
        ''''Updates centre position based on velocity'''
        self.x += self.xvelocity
        self.y += self.yvelocity

    def getColor(self):
        """ return the color of the triangle """
        return self.color

    def getRadius(self):
        """ return the radius of the triangle """
        return self.radius

    def getX(self):
        """ return the x coordinate of the triangle """
        return self.x

    def getY(self):
        """ return the y coordinate of the triangle """
        return self.y





# Get color dictionary from color_mod module
color = color_mod.color
line_color='green'


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        color_mod.printColorOptions()
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.triangle_list=[]
        self.number_of_triangle=10
        self.score=0
        self.time=20
        self.time_counter=0
        self.exit=0
        self.num_or_green=0

        for i in range(self.number_of_triangle):
            xvel = random.randrange(-10, 10)
            yvel = random.randrange(-10, 10)
            rvel = random.randrange(0, 10)
            rad = random.randrange(10,30)
            self.triangle_list.append(triangleClass(i, 'red', self.width / 2, self.height / 2, rad, xvel, yvel, rvel))
            if self.triangle_list[i].color=='green':
                self.num_or_green+=1




    def update(self, dt):
        """function to update centers of triangle"""
        self.time_counter+=1
        if self.time_counter>=1/dt:
            self.time_counter=0
            self.time -= 1
        for i in range(len(self.triangle_list)):
            # self.triangle_list[i].setCentreCoordinates(self.width / 2 + randint(-200, 200),self.height / 2 + randint(-200, 200))
            if self.triangle_list[i].x<0 or self.triangle_list[i].x>self.width:
                self.triangle_list[i].xvelocity = -self.triangle_list[i].xvelocity
            if self.triangle_list[i].y<0 or self.triangle_list[i].y>self.height:
                self.triangle_list[i].yvelocity = -self.triangle_list[i].yvelocity
            self.triangle_list[i].update_position()
            self.triangle_list[i].update_theta()

    def on_draw(self):

        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        if self.exit==0:
            for i in range(len(self.triangle_list)):
                vertexList = self.triangle_list[i].generate_triangle()
                pyglet.gl.glColor3f(*color[self.triangle_list[i].color])
                vertexList.draw(pyglet.gl.GL_LINE_LOOP)

            score_text='Score: ' + str(self.score) + " Time: " + str(self.time)
            pyglet.text.Label(score_text, font_name='Times New Roman', font_size=30,
                                      x=self.width-50, y=self.height-40,
                                      anchor_x='right', anchor_y='bottom').draw()
            if self.score>=self.number_of_triangle-self.num_or_green:
                pyglet.text.Label("You WIN. GG WP", font_name='Times New Roman', font_size=50,
                                  x=self.width/2, y=self.height/2,
                                  anchor_x='center', anchor_y='center').draw()
                self.exit=1


            if self.time <= 0 :
                self.triangle_list = []
                pyglet.text.Label("NOOOB. PATHETIC.", font_name='Times New Roman', font_size=50,
                                  x=self.width / 2, y=self.height / 2,
                                  anchor_x='center', anchor_y='center').draw()
                self.exit=1
        if self.exit==1:
            if self.score >= self.number_of_triangle-self.num_or_green:
                pyglet.text.Label("You WIN. GG WP", font_name='Times New Roman', font_size=50,
                                  x=self.width / 2, y=self.height / 2,
                                  anchor_x='center', anchor_y='center').draw()
                self.exit = 1

            if self.time <= 0:
                self.triangle_list = []
                pyglet.text.Label("NOOOB. PATHETIC.", font_name='Times New Roman', font_size=50,
                                  x=self.width / 2, y=self.height / 2,
                                  anchor_x='center', anchor_y='center').draw()
                self.exit = 1
        if self.exit==2:
            pyglet.text.Label("NOOOB. DONT GREEN.", font_name='Times New Roman', font_size=40,
                              x=self.width / 2, y=self.height / 2,
                              anchor_x='center', anchor_y='center').draw()






    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')
            kill_list=[]
            for i in range(len(self.triangle_list)):
                x_min = self.triangle_list[i].x -self.triangle_list[i].radius
                x_max = self.triangle_list[i].x +self.triangle_list[i].radius
                y_min = self.triangle_list[i].y - self.triangle_list[i].radius
                y_max = self.triangle_list[i].y + self.triangle_list[i].radius
                if x > x_min and x < x_max:
                    if y > y_min and y < y_max:
                        kill_list.append(i)
                        if self.triangle_list[i].color=='green':
                            self.exit=2
                        self.score+=1
                        yes_choice=random.randrange(0,3)
                        player.queue(yes_list[yes_choice])
                        player.play()






            for index in sorted(kill_list, reverse=True):
                del self.triangle_list[index]


        if button == mouse.RIGHT:
            print('The left mouse button was pressed.')


    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            pass
        elif symbol == key.LEFT:
            for i in range(len(self.triangle_list)):
                self.triangle_list[i].radius += 5
        elif symbol == key.RIGHT:
            for i in range(len(self.triangle_list)):
                self.triangle_list[i].radius -= 5




# this is the main game engine loop

yes1 = pyglet.media.load('yes-hahahaa.wav',streaming=False)
yes2 = pyglet.media.load('yes-indeed.wav',streaming=False)
yes3 = pyglet.media.load('yes-please.wav',streaming=False)
yes_list=[yes1,yes2,yes3]
player = pyglet.media.Player()

if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 30.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet