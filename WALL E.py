from OpenGL.GLUT import*
from OpenGL.GL import*
from OpenGL.GLU import*
import numpy as np
from math import *
def draw_cirle(r=0.5 ,x1=0.2 ,x2=0.02):
    # glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.01):
       # glColor3f(1-theta/(2*pi) ,theta/2*pi ,1)
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x+x1, y+x2)
    glEnd()

def draw_uncomplete_cirle(r=0.5, x1=0.2, x2=0.02 ,solid_or_not = True, theta1 = 0.0):
        # glColor3f(0,0,0)
        if solid_or_not:
            glBegin(GL_POLYGON)
        else:
            glBegin(GL_LINE_STRIP)
        for theta in np.arange(pi, 2 * pi * theta1 ,0.00001):
            # glColor3f(1-theta/(2*pi) ,theta/2*pi ,1)
            x = r * cos(theta)
            y = r * sin(theta)
            glVertex(x + x1, y + x2)
        glEnd()

def draw():
    glClearColor(1 ,1 ,1 ,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(25)

    # the right leg
    glColor(112/255, 128/255 , 144/255)
    glBegin(GL_POLYGON)
    glVertex(0.5, -0.45)
    glVertex(0.55, -0.45)
    glVertex(.55, -.7)
    glVertex(0.5, -0.75)
    glVertex(0.3, -0.75)
    glVertex(0.3, -0.7)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINE_STRIP)
    glVertex(0.5, -0.45)
    glVertex(0.55, -0.45)
    glVertex(.55, -.7)
    glVertex(0.5, -0.75)
    glVertex(0.3, -0.75)
    glVertex(0.3, -0.7)
    glEnd()

    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_POLYGON)
    glVertex(0.5, -0.8)
    glVertex(0.55, -0.8)
    glVertex(0.55, -0.85)
    glVertex(0.5, -0.85)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINES)
    glVertex(0.5, -0.8)
    glVertex(0.55, -0.8)
    glVertex(0.5, -0.85)
    glVertex(0.55, -0.85)
    glEnd()

    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_POLYGON)
    glVertex(0.5, -0.75)
    glVertex(0.5, -0.9)
    glVertex(0.37, -0.9)
    glVertex(0.3, -0.83)
    glVertex(0.3, -0.75)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINE_STRIP)
    glVertex(0.5, -0.75)
    glVertex(0.5, -0.9)
    glVertex(0.37, -0.9)
    glVertex(0.3, -0.83)
    glVertex(0.3, -0.75)
    glEnd()

    glColor(0, 0, 0)
    draw_cirle(0.017, 0.37, -0.83)

    # the left leg
    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.5, -0.45)
    glVertex(-0.55, -0.45)
    glVertex(-0.55, -.7)
    glVertex(-0.5, -0.75)
    glVertex(-0.3, -0.75)
    glVertex(-0.3, -0.7)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINE_STRIP)
    glVertex(-0.5, -0.45)
    glVertex(-0.55, -0.45)
    glVertex(-0.55, -.7)
    glVertex(-0.5, -0.75)
    glVertex(-0.3, -0.75)
    glVertex(-0.3, -0.7)
    glEnd()

    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.5, -0.8)
    glVertex(-0.55, -0.8)
    glVertex(-0.55, -0.85)
    glVertex(-0.5, -0.85)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINES)
    glVertex(-0.5, -0.8)
    glVertex(-0.55, -0.8)
    glVertex(-0.5, -0.85)
    glVertex(-0.55, -0.85)
    glEnd()

    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.5, -0.75)
    glVertex(-0.5, -0.9)
    glVertex(-0.37, -0.9)
    glVertex(-0.3, -0.83)
    glVertex(-0.3, -0.75)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINE_STRIP)
    glVertex(-0.5, -0.75)
    glVertex(-0.5, -0.9)
    glVertex(-0.37, -0.9)
    glVertex(-0.3, -0.83)
    glVertex(-0.3, -0.75)
    glEnd()

    glColor(0, 0, 0)
    draw_cirle(0.017, -0.37, -0.83)

    glColor(255/255 ,215/255 ,0) # the triangle
    glBegin(GL_QUADS)
    glVertex(-0.5, 0.2)
    glVertex(0.5, 0.2)
    glVertex(0.5, -0.7)
    glVertex(-0.5, -0.7)
    glEnd()

# the left triangle leg
    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_QUADS)
    glVertex(-0.55, -0.43)
    glVertex(-0.55, -1)
    glVertex(-0.9, -1)
    glVertex(-0.9, -0.43)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINE_LOOP)
    glVertex(-0.55, -0.43)
    glVertex(-0.55, -1)
    glVertex(-0.9, -1)
    glVertex(-0.9, -0.43)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINES)
    for vd in np.arange(-0.43 ,-1 ,-0.1):
       glVertex(-0.55, vd)
       glVertex(-0.9, vd)
    glEnd()

    # the right triangle leg
    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_QUADS)
    glVertex(0.55, -0.43)
    glVertex(0.55, -1)
    glVertex(.9, -1)
    glVertex(0.9, -0.43)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINE_LOOP)
    glVertex(0.55, -0.43)
    glVertex(0.55, -1)
    glVertex(0.9, -1)
    glVertex(0.9, -0.43)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINES)
    for vd in np.arange(-0.43, -1, -0.1):
        glVertex(0.55, vd)
        glVertex(0.9, vd)
    glEnd()

    # frame of the big triangle
    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINE_LOOP)
    glVertex(-0.5, 0.2)
    glVertex(0.5, 0.2)
    glVertex(0.5, -0.7)
    glVertex(-0.5, -0.7)
    glEnd()

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(0.2, -0.09)
    glVertex(0.2, 0)
    glVertex(0.325, 0.05)
    glVertex(0.43, 0.05)
    glVertex(0.43, -0.09)
    glEnd()

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(0.43, -0.2)
    glVertex(0.43, -0.32)
    glVertex(0.35, -0.32)
    glVertex(0.2, -0.29)
    glVertex(0.2, -0.2)
    glEnd()

    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_POLYGON)
    glVertex(0.25, -0.09)
    glVertex(0.25, -0.2)
    glVertex(0.55, -0.2)
    glVertex(0.55, -0.09)
    glEnd()

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(0.43, -0.09)
    glVertex(0.43, 0.05)
    glVertex(0.6, 0.05)
    glVertex(0.67, -0.01)
    glVertex(0.55, -0.01)
    glVertex(0.55, -0.09)
    glEnd()

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(0.43, -0.2)
    glVertex(0.43, -0.32)
    glVertex(0.6, -0.32)
    glVertex(0.67, -0.29)
    glVertex(0.55, -0.29)
    glVertex(0.55, -0.2)
    glEnd()

# the right hand\
    glBegin(GL_LINE_LOOP)
    glColor(25 / 255, 25 / 255, 112 / 255)


    glVertex(0.2, 0)
    glVertex(0.325, 0.05)
    glVertex(0.6, 0.05)
    glVertex(0.67, -0.01)
    glVertex(0.67, -0.27)
    glVertex(0.59, -0.32)
    glVertex(0.35, -0.32)
    glVertex(0.2, -0.29)
    glVertex(0.2, -0.2)
    glVertex(0.55, -0.2)
    glVertex(0.55, -0.09)
    glVertex(0.2, -0.09)
    glEnd()

    glBegin(GL_LINES)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.25, -0.09)
    glVertex(0.25, -0.2)
    glVertex(0.43, 0.05)
    glVertex(0.43, -0.09)
    glVertex(0.43, -0.2)
    glVertex(0.43, -0.32)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(175 / 255, 255 / 255, 250 / 255)
    glVertex(0.67, -0.01)
    glVertex(0.55, -0.01)
    glVertex(0.55, -0.27)
    glVertex(0.67, -0.27)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.67, -0.01)
    glVertex(0.55, -0.01)
    glVertex(0.55, -0.27)
    glVertex(0.67, -0.27)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, .7, 0)
    glVertex(0.51, 0.2)
    glVertex(0.51, 0.06)
    glVertex(0.58, 0.06)
    glVertex(0.59, 0.12)

    glEnd()

    glBegin(GL_LINES)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.275, 0.023)
    glVertex(0.275, 0.2)
    glVertex(0.275, 0.12)
    glVertex(0.5, 0.12)
    glVertex(0.5, 0.2)
    glVertex(0.59, 0.12)
    glVertex(0.58, 0.12)
    glVertex(0.58, 0.06)
    glEnd()


# the end of the right hand

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.2, -0.09)
    glVertex(-0.2, 0)
    glVertex(-0.325, 0.05)
    glVertex(-0.43, 0.05)
    glVertex(-0.43, -0.09)
    glEnd()

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.43, -0.2)
    glVertex(-0.43, -0.32)
    glVertex(-0.35, -0.32)
    glVertex(-0.2, -0.29)
    glVertex(-0.2, -0.2)
    glEnd()

    glColor(112 / 255, 128 / 255, 144 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.25, -0.09)
    glVertex(-0.25, -0.2)
    glVertex(-0.55, -0.2)
    glVertex(-0.55, -0.09)
    glEnd()

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.43, -0.09)
    glVertex(-0.43, 0.05)
    glVertex(-0.6, 0.05)
    glVertex(-0.67, -0.01)
    glVertex(-0.55, -0.01)
    glVertex(-0.55, -0.09)
    glEnd()

    glColor(175 / 255, 255 / 255, 250 / 255)
    glBegin(GL_POLYGON)
    glVertex(-0.43, -0.2)
    glVertex(-0.43, -0.32)
    glVertex(-0.6, -0.32)
    glVertex(-0.67, -0.29)
    glVertex(-0.55, -0.29)
    glVertex(-0.55, -0.2)
    glEnd()

    #the left hand

    glBegin(GL_LINE_LOOP)
    glColor(25 / 255, 25 / 255, 112 / 255)

    glVertex(-0.2, 0)
    glVertex(-0.325, 0.05)
    glVertex(-0.6, 0.05)
    glVertex(-0.67, -0.01)
    glVertex(-0.67, -0.27)
    glVertex(-0.59, -0.32)
    glVertex(-0.35, -0.32)
    glVertex(-0.2, -0.29)
    glVertex(-0.2, -0.2)
    glVertex(-0.55, -0.2)
    glVertex(-0.55, -0.09)
    glVertex(-0.2, -0.09)
    glEnd()

    glBegin(GL_LINES)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(-0.25, -0.09)
    glVertex(-0.25, -0.2)
    glVertex(-0.43, 0.05)
    glVertex(-0.43, -0.09)
    glVertex(-0.43, -0.2)
    glVertex(-0.43, -0.32)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(175 / 255, 255 / 255, 250 / 255)
    glVertex(-0.67, -0.01)
    glVertex(-0.55, -0.01)
    glVertex(-0.55, -0.27)
    glVertex(-0.67, -0.27)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(-0.67, -0.01)
    glVertex(-0.55, -0.01)
    glVertex(-0.55, -0.27)
    glVertex(-0.67, -0.27)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, .7, 0)
    glVertex(-0.51, 0.2)
    glVertex(-0.51, 0.06)
    glVertex(-0.58, 0.06)
    glVertex(-0.59, 0.12)


    glEnd()

    glBegin(GL_LINES)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(-0.275, 0.023)
    glVertex(-0.275, 0.2)
    glVertex(-0.275, 0.12)
    glVertex(-0.5, 0.12)
    glVertex(-0.5, 0.2)
    glVertex(-0.59, 0.12)
    glVertex(-0.58, 0.12)
    glVertex(-0.58, 0.06)
    glEnd()

# the end of the left hand

    glBegin(GL_LINES)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.2 ,-0.045)
    glVertex(-0.2 ,-0.045)
    glEnd()


#the triangle above the big triangle
    glBegin(GL_LINE_STRIP)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.1 ,0.2)
    glVertex(0.1, 0.4)
    glVertex(-0.1, 0.4)
    glVertex(-0.1, 0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(255 / 255, 215 / 255, 0 / 255)
    glVertex(0.092, 0.21)
    glVertex(0.092, 0.39)
    glVertex(-0.092, 0.39)
    glVertex(-0.092, 0.21)
    glEnd()

    # the highest triangle

    glBegin(GL_POLYGON)
    glColor(255 / 255, 215 / 255, 0 / 255)
    glVertex(0.07, 0.4)
    glVertex(0.07, 0.55)
    glVertex(-0.07, 0.55)
    glVertex(-0.07, 0.4)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.07, 0.4)
    glVertex(0.07, 0.55)
    glVertex(-0.07, 0.55)
    glVertex(-0.07, 0.4)
    glEnd()

# #the right eye with its details
    glColor(175 / 255, 255 / 255, 250 / 255)
    draw_cirle(0.15, 0.32, 0.625)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.15, 0.32, 0.625 ,False ,3)

    glColor(112 / 255, 128 / 255, 144 / 255)
    draw_cirle(0.125, 0.25, 0.7)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.125, 0.25, 0.7, False, 3)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.053, 0.25, 0.7, False, 2)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_cirle(0.02, 0.41, 0.65)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_cirle(0.02, 0.29, 0.54)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_cirle(0.02, 0.12, 0.82)

    glBegin(GL_LINE_STRIP)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.066, 0.87)
    glVertex(0.176, 0.55)
    glVertex(0.06, 0.87)
    glVertex(0.33, 0.82)
    glEnd()

# the left eye with its details
    glColor(175 / 255, 255 / 255, 250 / 255)
    draw_cirle(0.15, -0.32, 0.625)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.15, -0.32, 0.625, False, 3)

    glColor(112 / 255, 128 / 255, 144 / 255)
    draw_cirle(0.125, -0.25, 0.7)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.125, -0.25, 0.7, False, 3)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.053, -0.25, 0.7, False, 2)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_cirle(0.02, -0.41, 0.65)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_cirle(0.02, -0.29, 0.54)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_cirle(0.02, -0.12, 0.82)

    glBegin(GL_LINE_STRIP)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(-0.066, 0.87)
    glVertex(-0.176, 0.55)
    glVertex(-0.06, 0.87)
    glVertex(-0.33, 0.82)
    glEnd()
#the line that tangnt the right eye
    glBegin(GL_LINES)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0.07, 0.55)
    glVertex(0.15 ,0.6)
    glEnd()

    # the line that tangnt the left eye
    glBegin(GL_LINES)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(-0.07, 0.55)
    glVertex(-0.15, 0.6)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.047 ,0.12 , 0.55 , False , 1)

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_uncomplete_cirle(0.047, -0.12, 0.55, False, 1)

    glColor(25 / 255, 25 / 255, 112 / 255)
    glBegin(GL_LINES)
    glVertex(0.09, 0.8)
    glVertex(-0.09, 0.8)
    glEnd()

    glColor(47 / 255, 79 / 255, 79 / 255)
    draw_uncomplete_cirle(0.12, 0, 0.74, False, 1)

    glBegin(GL_POLYGON)
    glColor(0 ,191/255 ,1)
    glVertex(0, 0)
    glVertex(-0.2, 0)
    glVertex(-0.2, 0.15)
    glVertex(0, 0.15)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(25 / 255, 25 / 255, 112 / 255)
    glVertex(0, 0)
    glVertex(-0.2, 0)
    glVertex(-0.2, 0.15)
    glVertex(0, 0.15)
    glEnd()

    glColor(25 / 255, 25 / 255, 112 / 255)
    draw_cirle(0.05, 0.1, 0.07)

    glColor(255 / 255, 0 / 255, 255 / 255)
    draw_cirle(0.018, 0.1, 0.07)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(930,100)
glutInitWindowSize(600, 600)
glutCreateWindow(b"WALL E")
glutDisplayFunc(draw)
glutMainLoop()

