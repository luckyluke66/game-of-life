import pygame

WHITE = (255,255,255)
vec = pygame.math.Vector2

class Game_window:
    def __init__(self, WIN, x, y):
        self.WIN = WIN
        self.pos = vec(x,y)
        self.width, self.height = 600,600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.topleft = self.pos

    def draw(self):
        self.image.fill((WHITE))
        self.WIN.blit(self.image,(self.pos.x,self.pos.y))

