import pygame


class Physics:

    f = 1
    r = 1

    def __init__(self):
        self.solids = list()
        self.mobiles = list()

    def compute(self):

        self.do_mobile_solid_collision()
        self.do_mobile_collision()

        for m in self.mobiles:
            m.physics_flag = False

    @staticmethod
    def is_circle_collision(c1, c2):
        dx = c1.rect.centerx - c2.rect.centerx
        dx *= dx

        dy = c1.rect.centery - c2.rect.centery
        dy *= dy

        sum_radii = c1.SIZE # s/2 + s/2
        sum_radii *= sum_radii

        return (dx + dy) <= sum_radii

    def do_mobile_collision(self):

        for m1 in self.mobiles:

            m1.physics_flag = True

            for m2 in self.mobiles:

                # if not m2.physics_flag and m1.rect.colliderect(m2.rect):
                if not m2.physics_flag and self.is_circle_collision(m1, m2):
                    n = pygame.math.Vector2((m1.rect.centerx - m2.rect.centerx, m1.rect.centery - m2.rect.centery))

                    if n.length() <= 0: continue

                    n.normalize_ip()

                    a1 = m1.v.dot(n)
                    a2 = m2.v.dot(n)

                    opti_p = (2.0 * (a1 - a2)) / 1

                    m1.v = m1.v - opti_p * 1 * n
                    m2.v = m2.v + opti_p * 1 * n

    def do_mobile_solid_collision(self):
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
