import pygame
import copy
from cell import *

vec = pygame.math.Vector2

class Game_window:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x,y)
        self.width, self.height = 600,600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = 30
        self.cols = 30
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)]for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.read_neighbours(self.grid)


    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((LIGHT_GRAY))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image,(self.pos.x,self.pos.y))

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)]for y in range(self.rows)]

    def evaluate(self):
        new_grid = copy.copy(self.grid)
        
        for row in self.grid:
            for cell in row:
                cell.live_neighbours()
        
        for y_index, row in enumerate(self.grid):
            for x_index, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbours == 2 or cell.alive_neighbours == 3:
                        new_grid[y_index][x_index].alive = True
                    if cell.alive_neighbours < 2:
                        new_grid[y_index][x_index].alive = False
                    if cell.alive_neighbours > 3:
                        new_grid[y_index][x_index].alive = False
                else:
                    if cell.alive_neighbours == 3:
                        new_grid[y_index][x_index].alive = True
                        
        self.grid = new_grid        

