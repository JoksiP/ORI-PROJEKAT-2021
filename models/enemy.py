from static.constants import *
import random


class Enemy:
    def __init__(self, screen, images, image_idx, speed, second):
        self.screen = screen
        self.image = images[image_idx]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        if second:
            self.rect.x += WIDTH * 3/5
        self.rect.y = ENEMY_Y[0 if random.randint(0, 12) > 2 else 1]
        if image_idx > 2:
            self.rect.y -= 40
        if image_idx == 3:
            self.rect.y -= 45
        self.speed = speed

    def update(self, enemies):
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            enemies.pop(0)

    def draw(self):
        self.screen.blit(self.image, self.rect)