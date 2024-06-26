import pygame, random

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Kill the Monster!")

FPS = 60
clock = pygame.time.Clock()

white = (255, 255, 255)
purple = (128, 0, 128)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font = pygame.font.Font('Abrushow.ttf', 23)

target_text = font.render("CURRENT CATCH", True, white)
target_text_rect = target_text.get_rect()
target_text_rect.center = (WINDOW_WIDTH//2,20)

title_text = font.render("MONSTER WRANGLER", True, white)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

start_text = font.render("MONSTER WRANGLER", True, white)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 30)









game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

            pause = True
            while pause:
                display_surface.blit(title_text, title_text_rect)
                display_surface.blit(start_text, start_text_rect)
                for ev in pygame.event.get():
                    if ev.type == pygame.K_RETURN:
                        game_running = False


   

    display_surface.blit(target_text, target_text_rect)

    pygame.draw.line(display_surface, purple, (0, 90), (1200, 90), 5)
    pygame.draw.line(display_surface, purple, (0, 610), (1200, 610), 5)
    pygame.draw.line(display_surface, purple, (1197, 90), (1197, 610), 5)
    pygame.draw.line(display_surface, purple, (2, 90), (2, 610), 5)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit