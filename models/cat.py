import math

import pygame
from static.constants import *


class Cat:
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.x = CAT_X
        self.y = CAT_Y
        self.jump_velocity = JUMP_VELOCITY
        self.is_running = True
        self.is_jumping = False
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        if self.image_idx > 14:
            self.image_idx = 0
        if self.is_running:
            self.run()
        if self.is_jumping:
            self.jump()

    def run(self):
        self.image = self.images[self.image_idx // 5]
        self.image_idx += 1
        self.rect.x = CAT_X
        self.rect.y = CAT_Y

    def jump(self):
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity <= -JUMP_VELOCITY:
            self.is_jumping = False
            self.is_running = True
            self.jump_velocity = JUMP_VELOCITY

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def calc_distance(self, enemy):
        cat_pos = (self.rect.x, self.rect.y)
        enemy_pos = enemy.rect.midtop
        dx = cat_pos[0] - enemy_pos[0]
        dy = cat_pos[1] - enemy_pos[1]
        return math.sqrt(dx**2+dy**2)