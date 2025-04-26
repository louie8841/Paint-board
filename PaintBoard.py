import sys, pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP
from random import randint

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPS = pygame.time.Clock()
color = (0, 0, 0)
    
def changeColor():
    global color
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
        
def main():
    SURFACE.fill((255, 255, 255))
    mousepos = []
    mousedown = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousedown = True
                elif event.button == 3:
                    changeColor()

            elif event.type == MOUSEMOTION:
                if mousedown == True:
                    mousepos.append(event.pos)

            elif event.type == MOUSEBUTTONUP:
                mousedown = False
                mousepos.clear()

        if len(mousepos) > 1:
            pygame.draw.lines(SURFACE, color, False, mousepos, 3)

        pygame.display.update()

if __name__ == '__main__':
    main()
