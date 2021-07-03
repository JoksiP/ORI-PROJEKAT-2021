import os


def display_score(screen, font, score):
    text = font.render(f'Score:  {score}', True, (0, 0, 0))
    screen.blit(text, (85, 650))


def display_generation(screen, font, generation):
    text = font.render(f'Generation:  {generation + 1}', True, (0, 0, 0))
    screen.blit(text, (270, 650))


def display_population(screen, font, population):
    text = font.render(f'Population:  {population}', True, (0, 0, 0))
    screen.blit(text, (515, 650))


def display_pause(screen, font):
    text = font.render(f'"Esc" - {"Pause/Resume"}', True, (0, 0, 0))
    screen.blit(text, (900, 650))


def empty_logs():
    open(os.path.join('output', 'logs.txt'), 'w').close()


def write_logs(generation, score):
    f = open(os.path.join('output', 'logs.txt'), "a")
    f.write(f'Generation:  {generation + 1}\n\tBest score:  {score}\n\n')
    f.close()

