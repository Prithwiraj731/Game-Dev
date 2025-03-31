import pygame
from settings import *

def draw_text(surface, text, size, x, y, color=NEON_BLUE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def start_menu(screen):
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(BG_COLOR)
        draw_text(screen, "FUTURISTIC SPACE DEFENDER", 64, WIDTH//2, HEIGHT//4)
        draw_text(screen, "Press any key to start", 36, WIDTH//2, HEIGHT//2)
        draw_text(screen, "Arrow keys to move, Space to shoot", 24, WIDTH//2, HEIGHT*3//4)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYUP:
                running = False
                
        clock.tick(FPS)
    return True

def end_menu(screen, score):
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(BG_COLOR)
        draw_text(screen, "GAME OVER", 64, WIDTH//2, HEIGHT//4)
        draw_text(screen, f"Final Score: {score}", 48, WIDTH//2, HEIGHT//2)
        draw_text(screen, "Press R to restart or ESC to quit", 24, WIDTH//2, HEIGHT*3//4)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
                
        clock.tick(FPS)
    return False