import pygame
import random

'''地鼠'''
class Mole(pygame.sprite.Sprite):
    def __init__(self, image_paths, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.transform.scale(pygame.image.load(image_paths[0]), (101, 103)),
                       pygame.transform.scale(pygame.image.load(image_paths[1]), (101, 103)),
                       pygame.transform.scale(pygame.image.load(image_paths[2]), (101, 103)),
                       pygame.transform.scale(pygame.image.load(image_paths[3]), (101, 103))]
        #随机生成地鼠形象
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.setPosition(position)
        self.is_hammer = False
    '''设置位置'''
    def setPosition(self, pos):
        self.rect.left, self.rect.top = pos
        #控制地鼠只会在指定的洞的区域出现
    '''设置被击中'''
    def setBeHammered(self):
        self.is_hammer = True
    '''显示在屏幕上'''
    def draw(self, screen):
        if self.is_hammer: self.image=self.image
        screen.blit(self.image, self.rect)
    '''重置地鼠'''
    def reset(self):
        self.image = random.choice(self.images)
        self.is_hammer = False