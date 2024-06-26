from src.objects.Ship import Ship
from OpenGL.GL import *
from OpenGL.GLUT import *

class Game:
    def __init__(self):
        self.ship = Ship()
        self.projectiles = []

        self.FPS = 60
        self.frente = False
        self.tras = False
        self.esquerda = False
        self.direita = False

        self.janelaAlt = 80
        self.janelaLar = 80
        self.mundoAlt = 20
        self.muldoLar = 20

    def inicio(self):
        glClearColor(0.5, 0.5, 0.5, 1)
        glEnable(GL_MULTISAMPLE)

    def tecladoSpecial(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.esquerda = True
        elif key == GLUT_KEY_RIGHT:
            self.direita = True

    def tecladoUpSpecial(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.esquerda = False
        elif key == GLUT_KEY_RIGHT:
            self.direita = False

    def reshape(self, w, h):
        self.janelaLar = w
        self.janelaAlt = h
        self.mundoLar = self.mundoAlt * w / h
        glViewport(0, 0, w, h)

    def timer(self, v):
        glutTimerFunc(int(1000 / self.FPS), self.timer, 0)
        
        self.ship.updatePosition(self)
        for projectil in self.projectiles:
            projectil.updatePosition()
            
            if (projectil.position.y > self.mundoAlt/2) or (projectil.position.y < -self.mundoAlt/2):
                self.projectiles.remove(projectil)
                
        self.ship.fireRate -= 1
        self.ship.atirar(self)
        
        glutPostRedisplay()

    def run(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.mundoLar / 2, self.mundoLar / 2, -self.mundoAlt / 2, self.mundoAlt / 2, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        for projectile in self.projectiles:
            projectile.draw()
        self.ship.draw()
        
        glutSwapBuffers()