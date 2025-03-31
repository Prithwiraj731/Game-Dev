import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, ENEMY_SPEED + 1)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        # Bounce off the sides
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = -self.speedx
            
        # Respawn at top if goes off bottom
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, ENEMY_SPEED + 1)

class EnemyManager:
    def __init__(self, enemy_image):
        self.enemy_image = enemy_image
        self.last_spawn = pygame.time.get_ticks()
        
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_spawn > ENEMY_SPAWN_RATE:
            self.last_spawn = now
            return Enemy(self.enemy_image)
        return None