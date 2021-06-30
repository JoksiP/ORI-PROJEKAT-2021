import pygame
import os
import random
import sys
from models.cat import *

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

ICON = pygame.image.load(os.path.join("images", "pc_character.png"))
EARTH = pygame.image.load(os.path.join("images", "catwalk.png"))
SKY = pygame.image.load(os.path.join("images", "sky.png"))
FONT = pygame.font.SysFont("comicsansmc", 24)
CAT_WALKING = [pygame.image.load(os.path.join("images", "cat_walk1.png")),
               pygame.image.load(os.path.join("images", "cat_walk2.png")),
               pygame.image.load(os.path.join("images", "cat_walk3.png"))]


def init_screen():
    SCREEN.blit(SKY, (0, 0))
    SCREEN.blit(EARTH, (0, 420))


def main():
    pygame.display.set_caption("Cat-jump master")
    pygame.display.set_icon(ICON)
    init_screen()

    yep_clock = pygame.time.Clock()

    cats = [Cat(SCREEN, CAT_WALKING)]

    while True:
        input_key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        init_screen()

        for cat in cats:
            cat.update()
            cat.draw()

        for i, cat in enumerate(cats):
            if input_key[pygame.K_SPACE]:
                cat.is_jumping = True
                cat.is_running = False

        yep_clock.tick(30)
        pygame.display.update()

if __name__ == '__main__':
    main()
