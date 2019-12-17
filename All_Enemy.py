import pygame
import random


class Small_Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        # 加载爆炸图片
        self.down_images = []
        self.down_images.extend([
            pygame.image.load("images/enemy1_down1.png").convert_alpha(),
            pygame.image.load("images/enemy1_down2.png").convert_alpha(),
            pygame.image.load("images/enemy1_down3.png").convert_alpha(),
            pygame.image.load("images/enemy1_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = width, height

        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-5 * self.height, 0)
        # 设置速度
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top <= self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-5 * self.height, 0)


class Mid_Enemy(pygame.sprite.Sprite):
    ph = 5

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        # 加载爆炸图片
        self.down_images = []
        self.down_images.extend([
            pygame.image.load("images/enemy2_down1.png").convert_alpha(),
            pygame.image.load("images/enemy2_down2.png").convert_alpha(),
            pygame.image.load("images/enemy2_down3.png").convert_alpha(),
            pygame.image.load("images/enemy2_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = width, height

        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-10 * self.height, -2 * self.height)
        # 设置速度
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.ph = Mid_Enemy.ph
        self.hit = False

    def move(self):
        if self.rect.top <= self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.ph = Mid_Enemy.ph
        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-10 * self.height, -2 * self.height)


class Big_Enemy(pygame.sprite.Sprite):
    ph = 10

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        # 加载爆炸图片
        self.down_images = []
        self.down_images.extend([
            pygame.image.load("images/enemy3_down1.png").convert_alpha(),
            pygame.image.load("images/enemy3_down2.png").convert_alpha(),
            pygame.image.load("images/enemy3_down3.png").convert_alpha(),
            pygame.image.load("images/enemy3_down4.png").convert_alpha(),
            pygame.image.load("images/enemy3_down5.png").convert_alpha(),
            pygame.image.load("images/enemy3_down6.png").convert_alpha()])
        self.rect = self.image1.get_rect()
        self.width, self.height = width, height

        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-15 * self.height, -5 * self.height)
        # 设置速度
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)
        self.ph = Big_Enemy.ph
        self.hit = False

    def move(self):
        if self.rect.top <= self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.ph = Big_Enemy.ph
        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-15 * self.height, -5 * self.height)
