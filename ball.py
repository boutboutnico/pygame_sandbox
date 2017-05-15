import pygame
import random


class Ball:

    SIZE = 50
    SPEED = 150 # px/s

    def __init__(self, pos):
        self.rect = pygame.rect.Rect(pos, (Ball.SIZE, Ball.SIZE))
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.v = pygame.math.Vector2()
        self.v.from_polar((1, random.randint(-180, 180)))
        self.color = random.sample(range(0,255), 3)
        self.physics_flag = False

    def compute(self, delta_time):

        self.v.scale_to_length(delta_time * Ball.SPEED / 1000.0)

        self.x += self.v.x
        self.y += self.v.y
        self.rect.center = (self.x, self.y)

    def render(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, int(Ball.SIZE/2))
