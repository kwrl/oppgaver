import pygame
import itertools
from operator import sub
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, OPENGL | DOUBLEBUF)

gluPerspective(45, display[0]/display[1], 0.1, 50)
glTranslatef(0, 0, -5)

vertices = list(itertools.product((-1, 1), repeat=3))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glColor3fv((0, 127, 127))
    glBegin(GL_LINES)

    for edge in itertools.combinations(vertices, 2):
        vec = tuple(map(sub, edge[0], edge[1]))
        if len([x for x in vec if abs(x)>0]) > 1: continue
        glVertex3fv(edge[0])
        glVertex3fv(edge[1])
    glEnd()

    glRotatef(1, 1, 1, -1)
    pygame.display.flip()
    pygame.time.wait(10)
