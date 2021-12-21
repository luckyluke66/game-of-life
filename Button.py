import pygame
from cell import *


class Button:
    def __init__(self, WIN):
        self.FONT = pygame.font.Font('font/8-BIT WONDER.ttf', 20)
        self.WIN = WIN

    def draw_buttons(self):
        start_text = self.FONT.render("Start", 1, LIGHT_GRAY)
        reset_text = self.FONT.render("Reset",1, LIGHT_GRAY)
        pause_text = self.FONT.render("Pause", 1, LIGHT_GRAY)
        self.WIN.blit(start_text, (153, 105))
        self.WIN.blit(pause_text, (353, 105))
        self.WIN.blit(reset_text, (553, 105))

    def button_hover(self,mouse):
        # start button()
        if mouse[0] >= 150 and mouse[0] <= 250 and mouse[1] >= 100 and mouse[1]<= 140:
            pygame.draw.rect(self.WIN, DARK_GREEN, [150, 100, 100, 40])
        else:
            pygame.draw.rect(self.WIN, GREEN, [150, 100, 100, 40])
        # pause button
        if mouse[0] >= 350 and mouse[0] <= 450 and mouse[1] >= 100 and mouse[1]<= 140:
            pygame.draw.rect(self.WIN, DARK_BLUE, [350, 100, 100, 40])
        else:
            pygame.draw.rect(self.WIN, BLUE, [350, 100, 100, 40])
        # stop button
        if mouse[0] >= 550 and mouse[0] <= 650 and mouse[1] >= 100 and mouse[1]<= 140: 
            pygame.draw.rect(self.WIN, DARK_RED, [550, 100, 100, 40])
        else:
            pygame.draw.rect(self.WIN, RED, [550, 100, 100, 40])
        