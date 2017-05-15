import pygame


class Physics:

    f = 1
    r = 1

    def __init__(self):
        self.solids = list()
        self.mobiles = list()

    def compute(self):

        for mobile in self.mobiles:
            for solid in self.solids:
                if mobile.rect.colliderect(solid.rect):

                    n = None

                    if mobile.rect.colliderect(solid.left):
                        n = solid.v_left
                        mobile.rect.right = solid.rect.left
                        mobile.x = mobile.rect.centerx

                    elif mobile.rect.colliderect(solid.top):
                        n = solid.v_top
                        mobile.rect.bottom = solid.rect.top
                        mobile.y = mobile.rect.centery

                    elif mobile.rect.colliderect(solid.right):
                        n = solid.v_right
                        mobile.rect.left = solid.rect.right
                        mobile.x = mobile.rect.centerx

                    elif mobile.rect.colliderect(solid.bottom):
                        n = solid.v_bottom
                        mobile.rect.top = solid.rect.bottom
                        mobile.y = mobile.rect.centery

                    if n:
                        # u = pygame.math.Vector2(mobile.v.dot(n) * n)
                        # w = pygame.math.Vector2(mobile.v - u)
                        # mobile.v = Physics.f * w - Physics.r * u
                        mobile.v.reflect_ip(n)
