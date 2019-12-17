import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.left, self.rect.top = position
        self.speed = 15
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        self.attack = 1

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = True

    def reset(self, position):
        self.active = True
        self.rect.left, self.rect.top = position
