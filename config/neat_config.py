import os
import neat


def run():
    config_neat = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        os.path.join("config", "config.txt")
    )
    population = neat.Population(config_neat)
    return population
