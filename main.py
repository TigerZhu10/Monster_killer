import pygame, random

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Kill the Monster!")

FPS = 60
clock = pygame.time.Clock()

score = 0
live = 5
round = 0

white = (255, 255, 255)
purple = (128, 0, 128)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font = pygame.font.Font('Abrushow.ttf', 23)


title_text = font.render("MONSTER WRANGLER", True, white)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

start_text = font.render("PRESS ENTER TO START", True, white)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 30)

target_text = font.render("CURRENT CATCH", True, white)
target_text_rect = target_text.get_rect()
target_text_rect.center = (WINDOW_WIDTH//2,20)

score_text = font.render(f"SCORE: {score}", True, white)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (5, 5)

lives_text = font.render(f"LIVES: {live}", True, white)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topleft = (5, 30)

round_text = font.render(f"CURRENT ROUND: {round}", True, white)
round_text_rect = round_text.get_rect()
round_text_rect.topleft = (5, 55)

class Monster(pygame.sprite.Sprite):
    def __init__(self, image ,x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

monster_group = pygame.sprite.Group()

monster_group.add(Monster("blue_monster.png", random.randint(64, 1137), random.randint(154, 546)))
monster_group.add(Monster("green_monster.png", random.randint(64, 1137), random.randint(154, 546)))
monster_group.add(Monster("purple_monster.png", random.randint(64, 1137), random.randint(154, 546)))
monster_group.add(Monster("yellow_monster.png", random.randint(64, 1137), random.randint(154, 546)))

class Player(pygame.sprite.Sprite):
    def __init__(self, knight, x, y):
        super().__init__()
        self.image = pygame.image.load(knight)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

player_group = pygame.sprite.Group()

player_group.add(Player("knight.png", WINDOW_WIDTH//2, 650))



pause = True
game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                pause = False

        display_surface.fill((0, 0, 0))
        if pause:
            display_surface.blit(title_text, title_text_rect)
            display_surface.blit(start_text, start_text_rect)



   
        else:
            display_surface.fill((0, 0, 0))
            display_surface.blit(round_text, round_text_rect)
            display_surface.blit(lives_text, lives_text_rect)
            display_surface.blit(score_text, score_text_rect)
            display_surface.blit(target_text, target_text_rect)
            pygame.draw.line(display_surface, purple, (0, 90), (1200, 90), 5)
            pygame.draw.line(display_surface, purple, (0, 610), (1200, 610), 5)
            pygame.draw.line(display_surface, purple, (1197, 90), (1197, 610), 5)
            pygame.draw.line(display_surface, purple, (2, 90), (2, 610), 5)
            monster_group.draw(display_surface)
            player_group.draw(display_surface)
            
            clock.tick(FPS)
            
    pygame.display.update()
pygame.quit
               