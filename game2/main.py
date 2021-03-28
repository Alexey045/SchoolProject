import sys
from character import Player
import pygame
from pygame.locals import *
import map


def main():
    pygame.init()

    BACKGROUND_COLOR = (144, 201, 120)

    WINDOW_SIZE = (400, 300)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('text')

    clock = pygame.time.Clock()
    FPS = 60

    player = Player('hero', 50, 184, 1, 4, screen)
    moving_left = False
    moving_right = False

    run = True
    level = map.Map('test_scene.tmx', 'data/maps')
    rects = level.get_rect_tiles()
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
        player.move(moving_left, moving_right, rects)
        level.render(screen)
        player.draw()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
