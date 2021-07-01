import pygame
import os
import random
import sys
from models.cat import *
from models.scoreboard import *
from models.enemy import *

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

ICON = pygame.image.load(os.path.join("images", "pc_character.png"))
EARTH = pygame.image.load(os.path.join("images", "earth.png"))
SKY = pygame.image.load(os.path.join("images", "sky.png"))
FONT = pygame.font.SysFont("comicsansmc", 36)
CAT_WALKING = [pygame.image.load(os.path.join("images", "cat_walk1.png")),
               pygame.image.load(os.path.join("images", "cat_walk2.png")),
               pygame.image.load(os.path.join("images", "cat_walk3.png"))]
ENEMIES = [pygame.image.load(os.path.join("images", "enemy_0_0.png")),
           pygame.image.load(os.path.join("images", "enemy_0_1.png")),
           pygame.image.load(os.path.join("images", "enemy_0_2.png")),
           pygame.image.load(os.path.join("images", "enemy_1_0.png")),
           pygame.image.load(os.path.join("images", "enemy_1_1.png")),
           pygame.image.load(os.path.join("images", "enemy_1_2.png")),]


def init_screen(scoreboard, x, y):
    SCREEN.blit(SKY, (0, 0))
    earth_width = EARTH.get_width()
    SCREEN.blit(EARTH, (x, y))
    SCREEN.blit(EARTH, (earth_width + x, y))
    if x <= -earth_width:
        x = 0
    x -= scoreboard.speed
    return x, y


def remove_cat(idx, cats):
    cats.pop(idx)
    return cats


def main():
    pygame.display.set_caption("Cat-jump master")
    pygame.display.set_icon(ICON)

    yep_clock = pygame.time.Clock()

    scoreboard = Scoreboard(SCREEN, FONT, 100)  # 100 = value at which the game speed increments
    x_earth, y_earth = init_screen(scoreboard, 0, 420)
    cats = [Cat(SCREEN, CAT_WALKING)]
    enemies = []

    while True:
        input_key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x_earth, y_earth = init_screen(scoreboard, x_earth, y_earth)

        if not cats:
            break
        if len(enemies) == 0:
            idx = random.randint(0, 5)
            enemies.append(Enemy(SCREEN, ENEMIES, idx, scoreboard.speed, False))
            idx = random.choice([i for i in range(0, 5) if i not in [idx]])
            enemies.append(Enemy(SCREEN, ENEMIES, idx, scoreboard.speed, True))

        for enemy in enemies:
            enemy.draw()
            enemy.update(enemies)
            for i, cat in enumerate(cats):
                if cat.rect.colliderect(enemy.rect):
                    cats = remove_cat(i, cats)

        for cat in cats:
            cat.update()
            cat.draw()

        for i, cat in enumerate(cats):
            if input_key[pygame.K_SPACE]:
                cat.is_jumping = True
                cat.is_running = False

        scoreboard.increment_score()
        scoreboard.display_score()
        yep_clock.tick(30)
        pygame.display.update()


if __name__ == '__main__':
    main()
