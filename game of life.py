import pygame
import sys
from game_window import *

pygame.init()

FONT = pygame.font.Font('font/8-BIT WONDER.ttf', 20)
WIDTH, HEIGHT = 800, 800
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
game_window = Game_window(WIN, 100,180)
clock = pygame.time.Clock()

def update():
    game_window.update()

def draw():
    WIN.fill(BLACK)
    game_window.draw()
    
def mouse_on_grid(pos):                             # osetruje aby neslo klikat mimo pripraveny prostor                         
    if pos[0] > 100 and pos[0] < WIDTH - 100:   
        if pos[1] > 180 and pos[1] < HEIGHT - 20:
            return True
    return False

def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]             # seznam ma 2 promenne 1 pozice x mysi a pozice y 
    grid_pos[0] = grid_pos[0]//20                   # tyto promenne muzou nabyvat jen hodnot jen v poli 
    grid_pos[1] = grid_pos[1]//20                   # delime hodnoty velikosti bunky 
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True
    
def buttons():
    start_text = FONT.render("Start", 1, LIGHT_GRAY)
    reset_text = FONT.render("Reset",1, LIGHT_GRAY)
    pause_text = FONT.render("Pause", 1, LIGHT_GRAY)
    WIN.blit(start_text, (153, 105))
    WIN.blit(pause_text, (353, 105))
    WIN.blit(reset_text, (553, 105))

def button_hover(mouse):
    # start button()
    if mouse[0] >= 150 and mouse[0] <= 250 and mouse[1] >= 100 and mouse[1]<= 140:
        pygame.draw.rect(WIN, DARK_GREEN, [150, 100, 100, 40])
    else:
        pygame.draw.rect(WIN, GREEN, [150, 100, 100, 40])
    # pause button
    if mouse[0] >= 350 and mouse[0] <= 450 and mouse[1] >= 100 and mouse[1]<= 140:
        pygame.draw.rect(WIN, DARK_BLUE, [350, 100, 100, 40])
    else:
        pygame.draw.rect(WIN, BLUE, [350, 100, 100, 40])
    # stop button
    if mouse[0] >= 550 and mouse[0] <= 650 and mouse[1] >= 100 and mouse[1]<= 140: 
        pygame.draw.rect(WIN, DARK_RED, [550, 100, 100, 40])
    else:
        pygame.draw.rect(WIN, RED, [550, 100, 100, 40])

def main():
    run = True
    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_on_grid(mouse_pos):
                    click_cell(mouse_pos)
                if mouse[0] >= 150 and mouse[0] <= 250 and mouse[1] >= 100 and mouse[1]<= 140:
                    print("start")
                if mouse[0] >= 350 and mouse[0] <= 450 and mouse[1] >= 100 and mouse[1]<= 140:
                    print("pause")
                if mouse[0] >= 550 and mouse[0] <= 650 and mouse[1] >= 100 and mouse[1]<= 140:
                    print("stop")

        update()
        draw()
        button_hover(mouse)
        buttons()
        pygame.display.update()
    pygame.quit()
    sys.exit()
main()
