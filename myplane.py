import pygame


class MyPlan(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("images/hero1.png").convert_alpha()
        self.image2 = pygame.image.load("images/hero2.png").convert_alpha()
        # self.image2 = pygame.image.load("")
        # 加载爆炸图片
        self.down_images = []
        self.down_images.extend([
            pygame.image.load("images/hero_blowup_n1.png").convert_alpha(),
            pygame.image.load("images/hero_blowup_n2.png").convert_alpha(),
            pygame.image.load("images/hero_blowup_n1.png").convert_alpha(),
            pygame.image.load("images/hero_blowup_n1.png").convert_alpha()])
        # 获取图片所在的矩形位置
        self.rect = self.image1.get_rect()
        # 设置宽高
        self.width, self.height = width, height
        # 设置图片所在的位置
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        # 设置速度
        self.speed = 10
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= self.height - self.rect.height:
            self.rect.top = self.height - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= self.width - self.rect.width:
            self.rect.left = self.width - self.rect.width
        else:
            self.rect.left += self.speed

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
