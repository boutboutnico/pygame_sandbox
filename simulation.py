import pygame
import random
import color
from physics import Physics
from ball import Ball
from wall import Wall


class Simulation:

    def __init__(self, screen_rect):

        self.wall_group = list()

        rect = pygame.rect.Rect((0, 0), (10, screen_rect.h))
        rect.topright = screen_rect.topright
        self.wall_group.append(Wall(rect))

        rect = pygame.rect.Rect((0, 0), (screen_rect.w, 10))
        rect.bottomleft = screen_rect.bottomleft
        self.wall_group.append(Wall(rect))

        rect = pygame.rect.Rect((0, 0), (10, screen_rect.h))
        rect.topleft = screen_rect.topleft
        self.wall_group.append(Wall(rect))

        rect = pygame.rect.Rect((0, 0), (screen_rect.w, 10))
        rect.topleft = screen_rect.topleft
        self.wall_group.append(Wall(rect))

        self.ball_group = list()
        for i in range(50):
            b = Ball((random.randint(0, screen_rect.w), random.randint(0, screen_rect.h)))
            if not any(Physics.is_circle_collision(b, ball) for ball in self.ball_group):
                self.ball_group.append(b)

        self.physics = Physics()
        self.physics.solids.extend(self.wall_group)
        self.physics.mobiles.extend(self.ball_group)

    def compute(self, delta_time):
        for ball in self.ball_group:
            ball.compute(delta_time)

        self.physics.compute()

    def render(self, surface):
        surface.fill(color.WHITE)

        for wall in self.wall_group:
            wall.render(surface)

        for ball in self.ball_group:
            ball.render(surface)



