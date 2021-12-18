import pygame
import sys
from game_window_class import *

pygame.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WIDTH, HEIGHT = 800, 800
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
game_window = Game_window(WIN, 100,180)
   
def update():
    game_window.update()

def draw():
    WIN.fill((234,56,78))
    game_window.draw()
    

def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update()
        draw()
        pygame.display.update()
    pygame.quit()
    sys.exit()

main()



