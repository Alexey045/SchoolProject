import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        img = pygame.image.load(f'data/sprites/characters/{self.char_type}.png').convert_alpha()
        self.image = pygame.transform.scale(img,
                                            (int(img.get_width() * scale),
                                             int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.screen = screen
        self.direction = 1  # 1 is right. -1 is left
        self.flip = False
        self.jump = False
        self.in_air = True
        self.vel_y = 0  # velocity for y coordinate
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.tile_air = False

    def move(self, moving_left, moving_right, rectangles):
        gravity = 0.75
        dx = 0
        dy = 0

        if moving_right and moving_left:
            dx = 0
        elif moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        elif moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if self.jump and not self.in_air:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        self.vel_y += gravity
        if self.vel_y > 8:
            self.vel_y = 8
        dy += self.vel_y

        for rect in rectangles:
            # ToDo добавь при любой большой скорости
            if rectangles[rect].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                if self.direction == 1:
                    self.rect.right = rectangles[rect].left
                elif self.direction == -1:
                    self.rect.left = rectangles[rect].right
                dx = 0
            if rectangles[rect].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = rectangles[rect].bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = rectangles[rect].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False

        if abs(self.vel_y) > 1:  # ToDo
            self.in_air = True

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
