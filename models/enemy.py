from static.constants import *
import random


class Enemy:
    def __init__(self, screen, images, image_idx, speed):
        self.screen = screen
        self.image = images[image_idx]
        self.flying = 0 if random.randint(0, 10) > 2 else 1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = ENEMY_Y[self.flying]
        self.speed = speed

    def update(self, enemies):
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            enemies.pop()

    def draw(self):
        self.screen.blit(self.image, self.rect)