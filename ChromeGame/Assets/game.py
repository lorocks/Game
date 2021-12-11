import pygame
import random
import sys

from Models import *
from Videos import *
from Init import *

pygame.init()

#Stage 1
def background_1():
    global x_pos_bg, y_pos_bg
    image_width = BG.get_width()
    SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
    SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= game_speed

def score():
    global points, game_speed
    points += 1
    if points % 100 == 0:
        game_speed += 1

    text = font.render("Points: " + str(points), True, BLACK)
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    SCREEN.blit(text, textRect)

def add_obstacles():
    global Age19, obstacles, points
    if Age19 and points < 30:  # to change 3000
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0 or random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(OBS_AGE_19))
            elif random.randint(0, 2) == 2:
                obstacles.append(Drone(DRONE))
    elif not Age19 and points < 30:  # t change 3000
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0 or random.randint(0, 2) == 1:
                obstacles.append(SmallCactus(OBS_AGE_18))
            elif random.randint(0, 2) == 2:
                obstacles.append(Drone(DRONE))
    elif points > 30:  # to change 3000
        if len(obstacles) == 0:
            obstacles.append(Shrine(SHRINE))

def FirstStage():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, font, Age19
    run = True
    #clock = pygame.time.Clock()
    player = Man()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    obstacles = []
    death_count = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    FPS1 = 30

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        SCREEN.fill(WHITE)
        userInput = pygame.key.get_pressed()

        background_1()

        player.draw(SCREEN)
        player.update(userInput)
        add_obstacles()

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed,obstacles)
            if player.man_rect.colliderect(obstacle.rect) and obstacle.identify() == 9:
                SecondStage()
            elif player.man_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                movie(obstacle.identify())
                death_count += 1
                menu(death_count)

        score()

        clock.tick(FPS1)
        pygame.display.update()

#Stage 2
def background2(player, enemy):
    global font_health
    SCREEN2.blit(BG2, (0, 0))
    Sovereign_HP = font_health.render("Health: " + str(player.HP), 1, WHITE)
    Eye_HP = font_health.render("Health: " + str(enemy.HP), 1, WHITE)
    SCREEN2.blit(Sovereign_HP, (10, 10))
    SCREEN2.blit(Eye_HP, (SCREEN_WIDTH - Eye_HP.get_width() - 10, 10))
    return

def SecondStage():
    global font_health, SCREEN2
    FPS2 = 60
    enemy_attacks = []
    player = Sovereign()
    enemy = Eye()
    font_health = pygame.font.Font('freesansbold.ttf', 20)
    SCREEN2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 100))

    while (1):
        background2(player, enemy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()


        userInput = pygame.key.get_pressed()
        player.draw(SCREEN2)
        enemy.draw(SCREEN2)
        player.movement(userInput)

        if player.bullet_rect.colliderect(enemy.weak_spot_rect):
            enemy.HP -= 1
            player.bullet_rect.x += SCREEN_WIDTH - 3
        if player.bullet_rect.colliderect(enemy.eye_rect):
            player.bullet_rect.x += SCREEN_WIDTH - 3

        num = random.randint(0, 2)
        if not enemy.START_ATTACK:
            enemy.start_attack()
        elif (enemy.HP == 10 and enemy.START_ATTACK and enemy.RAGE_TIME == 0) or (enemy.HP == 1 and enemy.START_ATTACK and enemy.RAGE_TIME == 1):    #to cahneg 24 to 10
            if len(enemy_attacks) == 0:
                enemy_attacks.append(Attack2(ATTACK2))
                enemy.RAGE = True
                enemy.RAGE_TIME += 1
        elif enemy.START_ATTACK:
            if len(enemy_attacks) == 0:
                enemy_attacks.append(Attack1(ATTACK1, num))

        if enemy.RAGE == True:
            for attack in enemy_attacks:
                attack.draw(SCREEN2)
                attack.update(enemy_attacks, enemy)
                if player.sovereign_rect.colliderect(attack.attack_rect):
                    player.HP -= 1
        elif num >=0 or num <= 2:
            for attack in enemy_attacks:
                attack.draw(SCREEN2)
                attack.update(enemy_attacks)
                if player.sovereign_rect.colliderect(attack.part1) or player.sovereign_rect.colliderect(attack.part2) or player.sovereign_rect.colliderect(attack.part3):
                    player.HP -= 1
                    enemy_attacks.pop()

        if player.HP == 0:
            pygame.time.delay(2000)
            menu(1)
        if enemy.HP == 0:
            ThirdStage()

        clock.tick(FPS2)
        pygame.display.update()

#Stage 3
def ThirdStage():
    return

#Start Menu
def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill(WHITE)
        font_menu = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font_menu.render("Press any Key to Start: Reach 500 for Bird", True, (BLACK))
        elif death_count > 0:
            text = font_menu.render("Press any Key to Restart", True, BLACK)
            score = font_menu.render("Your Score: " + str(points), True, BLACK)
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                FirstStage()

def start_age():
    global Age19
    while(1):
        SCREEN.fill(WHITE)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Up Key for 18+, Down Key for <18", True, BLACK)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        pygame.display.update()
        userInput = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif userInput[pygame.K_UP]:
                Age19 = True
                menu(death_count=0)
            elif userInput[pygame.K_DOWN]:
                Age19 = False
                menu(death_count=0)

start_age()

# use pygame.transform.fns to change img dimentions and rotate if necessary
#step_index