#!/usr/bin/env python3
import cv2
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
# import OpenGL.GLUT as GLUT
import pygame
from pygame.locals import *
import face_detection

print("Imports successful!")

cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
cubeColors = ((1,0,0),(0,1,0),(0,0,1),(0,1,0),(1,1,1),(0,1,1),(1,0,0),(0,1,0),(0,0,1),(1,0,0),(1,1,1),(0,1,1))

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        x = 0
        for cubeVertex in cubeQuad:
            x += 1
            glColor3fv(cubeColors[x])
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

# def showScreen():
#     GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)

if __name__ == "__main__":

    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    x = 0
    y = 0
    theta_x = 0
    theta_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #If both are None Types
        try:
            temp_x, temp_y = face_detection.get_face_location()
        except:
            continue

        if temp_x != None:
            x = 45*(temp_x - 500)/500
        if temp_y != None:
            y = -1*45*(temp_y - 175)/175

        glRotatef(x - theta_x, 0, 1, 0)
        glRotatef(y - theta_y, 1, 0, 0)
        theta_y = y
        theta_x = x

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        solidCube()
        wireCube()
        pygame.display.flip()
        pygame.time.wait(10)