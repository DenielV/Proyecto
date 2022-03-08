import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import CalcularRectangulos

def MarioSilueta(recsS ):
    for rectangulo in recsS:
        glDisable(GL_LIGHTING)

        glColor4ub(0,0,0,255)
        glBegin(GL_POLYGON)
        for vertice in rectangulo:
            glVertex2fv(vertice)
        glEnd()

#deniel puto
def MarioRelleno(recsR, colores, paleta):
    coloresListaIndex = 0
    for recR in recsR:
        coloresIndex = 0
        for relleno in recR:
            glDisable(GL_LIGHTING)
            glColor4ub(
            paleta[colores[coloresListaIndex][coloresIndex]][0],
            paleta[colores[coloresListaIndex][coloresIndex]][1],
            paleta[colores[coloresListaIndex][coloresIndex]][2],
            paleta[colores[coloresListaIndex][coloresIndex]][3])
            glBegin(GL_POLYGON)
            for vertice in relleno:
                glVertex2fv(vertice)
            glEnd()
            coloresIndex+=1
        coloresListaIndex+=1

def main():
    resultados = CalcularRectangulos.Formar()
    pygame.init()
    display = (960,540)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glClearColor(255,255,255,255)
    glTranslatef(0.0,0.0,-5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.15,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.15,0,0)
        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        MarioSilueta(resultados[0])
        MarioRelleno(resultados[1],resultados[2],resultados[3])
        pygame.display.flip()
        pygame.time.wait(10)


main()
