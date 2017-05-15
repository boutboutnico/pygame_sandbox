import pygame
import color
import simulation


def main():

    pygame.init()
    pygame.font.init()

    done = False
    clock = pygame.time.Clock()

    screen_rect = pygame.rect.Rect((0, 0), (800, 800))
    flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
    screen_surface = pygame.display.set_mode(screen_rect.size, flags, 16)
    screen_surface.set_alpha(None)
    pygame.display.set_caption("Pygame Time")

    font = pygame.font.SysFont("monospace", 15)

    simu = simulation.Simulation(screen_rect)

    while not done:

        delta_time = clock.tick(120)

        pygame.event.pump()
        events = pygame.event.get()
        for event in events:

            # Quit
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        simu.compute(delta_time)

        simu.render(screen_surface)

        label = font.render("FPS:{:2.0f} delta_time:{}".format(clock.get_fps(), delta_time), 1, color.BLACK)
        screen_surface.blit(label, (10, 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
