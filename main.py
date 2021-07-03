import pygame
import os
import random
import sys
from models.cat import *
from models.scoreboard import *
from models.enemy import *
from utils.util import *
import config.neat_config
import neat

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
           pygame.image.load(os.path.join("images", "enemy_1_2.png"))]


def init_screen(scoreboard, x, y):
    SCREEN.blit(SKY, (0, 0))
    earth_width = EARTH.get_width()
    SCREEN.blit(EARTH, (x, y))
    SCREEN.blit(EARTH, (earth_width + x, y))
    if x <= -earth_width:
        x = 0
    x -= scoreboard.speed
    return x, y


def remove_cat(idx, cats, cat_genomes, cat_nns):
    cats.pop(idx)
    cat_genomes.pop(idx)
    cat_nns.pop(idx)


def pause(is_paused):
    while True:
        input_key = pygame.key.get_pressed()
        if input_key[pygame.K_ESCAPE]:
            return not is_paused


def evaluate(genomes, config_file):
    pygame.display.set_caption("Cat-jump master")
    pygame.display.set_icon(ICON)

    yep_clock = pygame.time.Clock()

    scoreboard = Scoreboard(SCREEN, FONT, 100)  # 100 = value at which the game speed increments
    x_earth, y_earth = init_screen(scoreboard, 0, 420)

    cats = []
    enemies = []
    cat_genomes = []
    cat_nns = []

    is_paused = False

    for genome_id, genome in genomes:
        cats.append(Cat(SCREEN, CAT_WALKING))
        cat_genomes.append(genome)
        cat_nn = neat.nn.FeedForwardNetwork.create(genome, config_file)
        cat_nns.append(cat_nn)
        genome.fitness = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_paused = pause(is_paused)

        if not is_paused:
            x_earth, y_earth = init_screen(scoreboard, x_earth, y_earth)
            if not cats:
                break
            if len(enemies) == 0:
                idx = random.randint(0, 5)
                enemies.append(Enemy(SCREEN, ENEMIES, idx, scoreboard.speed))

            for enemy in enemies:
                enemy.draw()
                enemy.update(enemies)
                for i, cat in enumerate(cats):
                    cat_genomes[i].fitness += 0.1
                    if cat.rect.colliderect(enemy.rect):
                        cat_genomes[i].fitness -= 1
                        remove_cat(i, cats, cat_genomes, cat_nns)

            for cat in cats:
                cat.update()
                cat.draw()

            display_generation(SCREEN, FONT, population.generation)
            display_population(SCREEN, FONT, str(len(cats)))

            if len(enemies) != 0:
                for i, cat in enumerate(cats):
                    output = cat_nns[i].activate((cat.rect.y, cat.calc_distance(enemies[0]), enemies[0].flying * 500000))
                    if output[0] > 0.5 and cat.rect.y == CAT_Y:
                        cat.is_jumping = True
                        cat.is_running = False
                    """ [ MANUAL CONTROL ]
                    if input_key[pygame.K_SPACE]:
                        cat.is_jumping = True
                        cat.is_running = False
                    """

            scoreboard.increment_score()
            scoreboard.display_score()
        display_pause(SCREEN, FONT)
        yep_clock.tick(30)
        pygame.display.update()
    write_logs(population.generation, scoreboard.score)


if __name__ == '__main__':
    global population
    empty_logs()
    population = config.neat_config.run()
    population.run(evaluate, 1000)
