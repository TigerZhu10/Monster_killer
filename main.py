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
round = 1

white = (255, 255, 255)
purple = (128, 0, 128)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

catch_sound = pygame.mixer.Sound('catch.wav')
miss_sound = pygame.mixer.Sound('die.wav')

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
        monster_speed = 3
        monster_direction = random.choice([1,-1])
        monster_speed = monster_speed * monster_direction
        self.dx = monster_speed
        self.dy = monster_speed
        self.is_target = False
        self.choice = random.choice([1,0])

    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.dx

        if self.choice == 1:
            self.rect.y += self.dy
        else:
            self.rect.y -= self.dy

        if self.rect.right >= WINDOW_WIDTH -3:
            self.dx = -self.dx
        if self.rect.bottom >= 610 - 3:
            self.dy = -self.dy
        if self.rect.left <= 3:
            self.dx = -self.dx
        if self.rect.top <= 93:
            self.dy = -self.dy


monster_group = pygame.sprite.Group()

monster_group.add(Monster("blue_monster.png", random.randint(64, 1137), random.randint(154, 546)))
monster_group.add(Monster("green_monster.png", random.randint(64, 1137), random.randint(154, 546)))
monster_group.add(Monster("purple_monster.png", random.randint(64, 1137), random.randint(154, 546)))
monster_group.add(Monster("yellow_monster.png", random.randint(64, 1137), random.randint(154, 546)))

target_monster_first = random.choice(monster_group.sprites())
target_monster_first.is_target = True

current_target_monster = target_monster_first

class Player(pygame.sprite.Sprite):
    def __init__(self, knight, x, y, monster_group, Monster):
        super().__init__()
        self.monster_group = monster_group
        self.Monster = Monster
        self.in_round = 1
        
        self.flag = True
        
        self.image = pygame.image.load(knight)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)     

        self.velocity = 5
    def update(self):
        self.move()
        self.collisions()
        self.Chance()

    def move(self):  
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 92:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < 610:
            self.rect.y += self.velocity

    def collisions(self):
            #Global makes local variabal to an global variable 
            global current_target_monster, score, live, score_text, lives_text, round, round_text    
            collide_target = pygame.sprite.spritecollideany(self, self.monster_group)
            if collide_target:
                if collide_target.is_target:
                    catch_sound.play(0)
                    self.monster_group.remove(collide_target)
                    score += 1
                    if len(self.monster_group.sprites()) > 0:
                        target_monster = random.choice(monster_group.sprites())
                        target_monster.is_target = True
                        current_target_monster = target_monster
                    if len(self.monster_group.sprites()) <= 0 and self.flag == True:
                        self.rect.center = (WINDOW_WIDTH//2, 650) 
                        self.in_round += 1
                        self.flag = False
                        self.next_round()
                        round += 1
                # else 的逻辑是属于第136行的，但是不应该放在前面。因为如果放在前面第140行到第149行就不会执行。
                else:
                    self.rect.center = (WINDOW_WIDTH//2, 650) 
                    miss_sound.play(0)
                    live -= 1
                    
                    

                round_text = font.render(f"CURRENT ROUND: {round}", True, white)
                score_text = font.render(f"SCORE: {score}", True, white)
                lives_text = font.render(f"LIVES: {live}", True, white)

    def next_round(self):
        global current_target_monster
        for i in range(self.in_round):
            self.monster_group.add(self.Monster("blue_monster.png", random.randint(64, 1137), random.randint(154, 546)))
            self.monster_group.add(self.Monster("green_monster.png", random.randint(64, 1137), random.randint(154, 546)))
            self.monster_group.add(self.Monster("purple_monster.png", random.randint(64, 1137), random.randint(154, 546)))
            self.monster_group.add(self.Monster("yellow_monster.png", random.randint(64, 1137), random.randint(154, 546)))
        self.flag = True

        if len(self.monster_group.sprites()) > 0:
            target_monster = random.choice(monster_group.sprites())
            target_monster.is_target = True
            current_target_monster = target_monster

    def Chance(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.bottom = (680)
        



          

player_group = pygame.sprite.Group()
player_group.add(Player("knight.png", WINDOW_WIDTH//2, 650, monster_group, Monster))
            


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
        player_group.update()
        monster_group.update() 
        if current_target_monster:
            display_surface.blit(current_target_monster.image, (567, 27))


    clock.tick(FPS)     
    pygame.display.update()

pygame.quit