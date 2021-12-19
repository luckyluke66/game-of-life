import pygame
import sys
from game_window import *

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GRAY = (64,64,64)
LIGHT_GRAY = (84,84,84)

clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 800
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
game_window = Game_window(WIN, 100,180)
   
def update():
    game_window.update()

def draw():
    WIN.fill(BLACK)
    game_window.draw()
    
def mouse_on_grid(pos):                         # osetruje aby neslo klikat mimo pripraveny prostor                         
    if pos[0] > 100 and pos[0] < WIDTH - 100:   
        if pos[1] > 180 and pos[1] < HEIGHT - 20:
            return True
    return False

def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]         # seznam ma 2 promenne 1 pozice x mysi a pozice y 
    grid_pos[0] = grid_pos[0]//20               # tyto promenne muzou nabyvat jen hodnot jen v poli 
    grid_pos[1] = grid_pos[1]//20               # delime hodnoty velikosti bunky 
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
    

def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_on_grid(mouse_pos):
                    click_cell(mouse_pos)

        update()
        draw()
        pygame.display.update()
    pygame.quit()
    sys.exit()
main()
