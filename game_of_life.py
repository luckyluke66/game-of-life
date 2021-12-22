import pygame
import sys
from game_window import *
from Button import *
pygame.init()

FONT = pygame.font.Font('font/8-BIT WONDER.ttf', 20)
WIDTH, HEIGHT = 800, 800
FPS = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
game_window = Game_window(WIN, 100,180)
clock = pygame.time.Clock()
state = "setting"

def update():
    game_window.update()

def draw():
    WIN.fill(BLACK)
    game_window.draw()
def running_update():
    game_window.update()
    game_window.evaluate()
def running_draw():
    WIN.fill(BLACK)
    game_window.draw()
def paused_update():
    game_window.update()
def paused_draw():
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
    
def run_game():
    global state 
    state = "running"

def pause_game():
    global state 
    state = "paused"
def reset_game():
    global state
    state = "setting"

def main():
    button = Button(WIN)
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
                    run_game()
                if mouse[0] >= 350 and mouse[0] <= 450 and mouse[1] >= 100 and mouse[1]<= 140:
                    pause_game()
                if mouse[0] >= 550 and mouse[0] <= 650 and mouse[1] >= 100 and mouse[1]<= 140:
                    reset_game()
                    game_window.__init__(WIN, 100,180)
                    
        if state == "setting":
            update()
            draw()   
        if state == "running":
            running_update()
            running_draw()
        if state == "paused":
            paused_update()
            paused_draw()

        button.button_hover(mouse)
        button.draw_buttons()
        pygame.display.update()
    pygame.quit()
    sys.exit()
main()
