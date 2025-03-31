import pygame
import random
from settings import *
from assets import load_assets
from player import Player
from enemy import Enemy, EnemyManager
from bullet import Bullet
from menu import start_menu, end_menu

def main():
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Futuristic Space Defender")
    clock = pygame.time.Clock()
    
    # Load assets
    assets = load_assets()
    
    # Game objects
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    players = pygame.sprite.Group()
    
    player = Player(assets["player_ship"])
    all_sprites.add(player)
    players.add(player)
    
    enemy_manager = EnemyManager(assets["enemy_ship"])
    
    score = 0
    
    # Game loop
    running = True
    while running:
        # Keep loop running at the right speed
        clock.tick(FPS)
        
        # Process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot(all_sprites, bullets)
        
        # Update
        player.update()
        
        # Spawn enemies
        new_enemy = enemy_manager.update()
        if new_enemy:
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)
        
        bullets.update()
        enemies.update()
        
        # Check for bullet-enemy collisions
        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for hit in hits:
            score += 100
            # Spawn new enemy immediately
            enemy = Enemy(assets["enemy_ship"])
            all_sprites.add(enemy)
            enemies.add(enemy)
        
        # Check for enemy-player collisions
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            player.health -= 10
            if player.health <= 0:
                running = False
        
        # Draw
        screen.blit(assets["background"], (0, 0))
        all_sprites.draw(screen)
        
        # Draw HUD
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, NEON_BLUE)
        screen.blit(score_text, (10, 10))
        
        # Draw health bar
        pygame.draw.rect(screen, (255, 0, 0), (WIDTH - 210, 10, 200, 20))
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH - 210, 10, player.health * 2, 20))
        
        pygame.display.flip()
    
    return score

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    while True:
        if not start_menu(screen):
            break
        
        score = main()
        
        if not end_menu(screen, score):
            break