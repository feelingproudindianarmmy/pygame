import pygame

import random

# Initialize Pygame

pygame.init()

# Custom event IDs for color change events

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colors using pygame.Color

# Background colors

BLUE = pygame.Color('blue')

LIGHTBLUE = pygame.Color('lightblue')

DARKBLUE = pygame.Color('darkblue')

# Sprite colors

YELLOW = pygame.Color('yellow')

MAGENTA = pygame.Color('magenta')

ORANGE = pygame.Color('orange')

WHITE = pygame.Color('white')

class sprite(pygame.sprite.Sprite):
    def __init__(self,height,width,color):
        super().__init__
        self.image = pygame.Surface([height,width])