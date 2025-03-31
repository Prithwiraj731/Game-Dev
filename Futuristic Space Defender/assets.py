import pygame
import random
from settings import *

def load_assets():
    assets = {}
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Player ship (simple triangle for now)
    player_ship = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(player_ship, NEON_BLUE, [(15, 0), (0, 30), (30, 30)])
    
    # Enemy ship (simple shape)
    enemy_ship = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(enemy_ship, NEON_PINK, [(0, 0), (30, 15), (0, 30)])
    
    # Bullet (simple circle)
    bullet = pygame.Surface((10, 10), pygame.SRCALPHA)
    pygame.draw.circle(bullet, NEON_BLUE, (5, 5), 5)
    
    # Background (starfield)
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(BG_COLOR)
    for _ in range(200):  # Draw stars
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.circle(background, (255, 255, 255), (x, y), 1)
    
    assets = {
        "player_ship": player_ship,
        "enemy_ship": enemy_ship,
        "bullet": bullet,
        "background": background
    }
    
    return assets