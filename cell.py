import pygame 
import random

# 
BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GRAY = (64,64,64)
LIGHT_GRAY = (84,84,84)
RED = (222, 7, 25)
GREEN = (12,89,16)
DARK_GREEN = (3, 43, 5)
BLUE = (34, 37, 212)
DARK_BLUE = (0, 2, 110)
DARK_RED = (74, 3, 3)


cell_size = 18
border_size = 1

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.neighbours = []
        self.highlighted_by_neighbour = False
        self.alive_neighbours = 0

    def update(self):
        self.rect.topleft = (self.grid_x * 20, self.grid_y * 20)
        """
        for cell in self.neighbours:
            if cell.alive:
                self.highlighted_by_neighbour = True
        """

    def draw(self):
        if self.alive:
            self.image.fill(LIGHT_GRAY)
        else:
            self.image.fill(LIGHT_GRAY)
            pygame.draw.rect(self.image, DARK_GRAY, (border_size, border_size,cell_size,cell_size))
        
        self.surface.blit(self.image, (self.grid_x * 20, self.grid_y * 20))

    def read_neighbours(self, grid):
        neighbour_list = [[1,1], [-1,-1], [-1,1], [1,-1], [0,-1], [0,1], [1,0], [-1,0]]       # mozne pozice kolem bunky 3x3 pole 
        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x
            neighbour[1] += self.grid_y
        for neighbour in neighbour_list:
            if neighbour[0] < 0:
                neighbour[0] += 30
            if neighbour[1] < 0:
                neighbour[1] += 30
            if neighbour[0] > 29:
                neighbour[0] -= 30
            if neighbour[1] > 29:
                neighbour[1] -= 30
        for neighbour in neighbour_list:
            try:
                self.neighbours.append(grid[neighbour[1]][neighbour[0]])
            except:
                print(neighbour)

    def live_neighbours(self):
        count = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                count += 1
        self.alive_neighbours = count
