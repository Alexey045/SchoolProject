import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, screen, b_rect):
        self.b_rect = b_rect
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        img = pygame.image.load(f'data/characters/{self.char_type}.png')
        white = (255, 255, 255)
        img.set_colorkey(white)
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

    def move(self, moving_left, moving_right):
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

        if self.rect.bottom + dy > 200:
            self.in_air = False
            dy = 200 - self.rect.bottom
        # ToDo добавь при любой большой скорости
        if self.b_rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
            if self.direction == 1:
                self.rect.right = self.b_rect.left
            elif self.direction == -1:
                self.rect.left = self.b_rect.right
            dx = 0
        # check for collision in y direction
        if self.b_rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
            # check if below the ground i.e. jumping
            if self.vel_y < 0:
                dy = self.b_rect.bottom - self.rect.top
                self.vel_y = 0
            # check if above the ground i.e. falling
            elif self.vel_y >= 0:
                dy = self.b_rect.top - self.rect.bottom
                self.vel_y = 0

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
