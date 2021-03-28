import sys
from character import Player
import pygame
from pygame.locals import *


def main():
    pygame.init()

    BACKGROUND_COLOR = (144, 201, 120)
    RED = (220, 0, 0)

    WINDOW_SIZE = (400, 300)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('text')

    clock = pygame.time.Clock()
    FPS = 60

    box = pygame.image.load('data/objects/box.png')
    b_rect = box.get_rect()
    b_rect.center = 100, 180

    player = Player('hero', 100, 50, 1, 5, screen, b_rect)
    moving_left = False
    moving_right = False

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    moving_left = True
                if event.key == K_d:
                    moving_right = True
                if event.key == K_w and not player.in_air:
                    player.jump = True
            if event.type == pygame.KEYUP:
                if event.key == K_a:
                    moving_left = False
                if event.key == K_d:
                    moving_right = False
                if event.key == K_ESCAPE:
                    run = False
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.line(screen, RED, (0, 200), (400, 200))
        player.move(moving_left, moving_right)

        player.draw()
        screen.blit(box, b_rect)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
