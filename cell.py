import pygame 

BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GRAY = (64,64,64)
LIGHT_GRAY = (84,84,84)
RED = (222, 7, 25)

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.grid_x * 20, self.grid_y * 20)

    def draw(self):
        if self.alive:
            self.image.fill(LIGHT_GRAY)
        else:
            self.image.fill(LIGHT_GRAY)
            pygame.draw.rect(self.image, DARK_GRAY, (2,2,18,18))
        
        self.surface.blit(self.image, (self.grid_x * 20, self.grid_y * 20))
        