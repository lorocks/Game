import pygame
import random

from Init import *

class Man:
    X_POS = 80
    Y_POS = 300
    Y_POS_DUCK = 340
    JUMP_SPEED = 8.5

    def __init__(self):
        self.ducking_img = DUCKING
        self.running_img = RUNNING
        self.jumping_img = JUMPING

        self.ducking = False
        self.running = True
        self.jumping = False

        self.jump_speed = self.JUMP_SPEED
        self.image = self.running_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS

    def update(self, userInput):
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        if self.jumping:
            self.jump()


        if userInput[pygame.K_UP] and not self.jumping:
            self.ducking = False
            self.running = False
            self.jumping = True
        elif userInput[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False
            self.jumping = False
        elif not (self.jumping or userInput[pygame.K_DOWN]):
            self.ducking = False
            self.running = True
            self.jumping = False

    def duck(self):
        self.image = self.ducking_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS_DUCK

    def run(self):
        self.image = self.running_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS

    def jump(self):
        self.image = self.jumping_img
        if self.jumping:
            self.man_rect.y -= self.jump_speed * 4
            self.jump_speed -= 0.8
        if self.jump_speed < - self.JUMP_SPEED:
            self.jumping = False
            self.jump_speed = self.JUMP_SPEED

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.man_rect.x, self.man_rect.y))


class Obstacle():
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self,game_speed,obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        self.video_value = 2
        if self.type == 0 or self.type == 1:
            self.rect.y = 325
        elif self.type == 2 or self.type == 3:
            self.rect.y = 300
        else:
            self.rect.y = 335
            self.video_value = 3

    def identify(self):
        return self.video_value


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        if self.type == 3 or self.type == 4 or self.type == 5:
            self.rect.y = 325
        else:
            self.rect.y = 300
        #self.rect.y = 300

    def identify(self):
        value = self.type + 3
        return 2


class Drone(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

    def identify(self):
        return 2
        #return 7


class Shrine(Obstacle):
    def __init__(self,image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 75

    def identify(self):
        return 9


class Sovereign:
    X_POS = 75
    Y_POS = SCREEN_HEIGHT - 30
    SPEED = 8
    HP = 5
    READY_SHOOT = True
    BULLET_SPEED = 10
    COUNT = 0
    SHOOT = False
    def __init__(self):
        self.image = SOVEREIGN
        self.sovereign_rect = self.image.get_rect()
        self.sovereign_rect.x = self.X_POS
        self.sovereign_rect.y = self.Y_POS
        self.bullet_img = BULLET
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_rect.x = self.sovereign_rect.x + 40
        self.bullet_rect.y = self.sovereign_rect.y + 50

    def movement(self, userInput):
        if not self.SHOOT:
            if userInput[pygame.K_UP] and self.sovereign_rect.y - self.SPEED > 20:
                self.sovereign_rect.y -= self.SPEED
                self.bullet_rect.y -= self.SPEED
            if userInput[pygame.K_DOWN] and self.sovereign_rect.y + self.SPEED < SCREEN_HEIGHT - 30:
                self.sovereign_rect.y += self.SPEED
                self.bullet_rect.y += self.SPEED
        else:
            if userInput[pygame.K_UP] and self.sovereign_rect.y - self.SPEED > 20:
                self.sovereign_rect.y -= self.SPEED
            if userInput[pygame.K_DOWN] and self.sovereign_rect.y + self.SPEED < SCREEN_HEIGHT - 30:
                self.sovereign_rect.y += self.SPEED

    def shoot(self):
        if self.READY_SHOOT:
            self.SHOOT = True

    def shooting(self):
        if self.bullet_rect.x > SCREEN_WIDTH:
            self.bullet_rect.x = self.sovereign_rect.x + 40
            self.bullet_rect.y = self.sovereign_rect.y + 50
            self.READY_SHOOT = False
            self.SHOOT = False
        if self.COUNT == 200:
            self.READY_SHOOT = True
            self.COUNT = 0
        if not self.READY_SHOOT:
            self.COUNT += 1
        if self.SHOOT:
            self.bullet_rect.x += self.BULLET_SPEED

    def draw(self, SCREEN2):
        SCREEN2.blit(self.image, (self.sovereign_rect.x, self.sovereign_rect.y))
        if self.READY_SHOOT:
            SCREEN2.blit(self.bullet_img, (self.bullet_rect.x, self.bullet_rect.y))
        self.shooting()

class Eye:
    X_POS = SCREEN_WIDTH - EYE_WIDTH
    Y_POS = (SCREEN_HEIGHT // 2) - (EYE_HEIGHT // 2)
    HP = 3           #to change 25
    COUNT = 0
    START_ATTACK = False
    RAGE = False
    RAGE_TIME = 1       # to change 0
    def __init__(self):
        self.image = EYE
        self.eye_rect = self.image.get_rect()
        self.eye_rect.x = self.X_POS
        self.eye_rect.y = self.Y_POS
        self.weak_spot_img = WEAKNESS
        self.weak_spot_rect = self.weak_spot_img.get_rect()
        self.weak_spot_rect.x = self.X_POS
        self.weak_spot_rect.y = self.Y_POS + (EYE_HEIGHT // 2) - 20

    def start_attack(self):
        self.COUNT += 1
        if self.COUNT == 50:
            self.START_ATTACK = True

    def draw(self, SCREEN2):
        SCREEN2.blit(self.weak_spot_img, (self.weak_spot_rect.x, self.weak_spot_rect.y))
        SCREEN2.blit(self.image, (self.eye_rect.x, self.eye_rect.y))



class Attack1:
    SPEED = 7
    def __init__(self,image,num):
        self.image = image
        self.part1 = self.image.get_rect()
        self.part2 = self.image.get_rect()
        self.part3 = self.image.get_rect()
        self.part1.x = 800
        self.part2.x = 800
        self.part3.x = 800
        if num == 0:
            self.part1.y = 100
            self.part2.y = SCREEN_HEIGHT // 2
            self.part3.y = SCREEN_HEIGHT - 100
        if num == 1:
            self.part1.y = 100
            self.part2.y = 200
            self.part3.y = 300
        if num == 2:
            self.part1.y = 450
            self.part2.y = 550
            self.part3.y = 650

    def update(self, enemy_attacks):
        self.part1.x -= self.SPEED
        self.part2.x -= self.SPEED
        self.part3.x -= self.SPEED
        if self.part1.x < 0:
            enemy_attacks.pop()

    def draw(self,SCREEN2):
        SCREEN2.blit(self.image, (self.part1.x, self.part1.y))
        SCREEN2.blit(self.image, (self.part2.x, self.part2.y))
        SCREEN2.blit(self.image, (self.part3.x, self.part3.y))


class Attack2:
    TIMER = 0
    def __init__(self, image):
        self.image = image
        self.attack_rect = self.image.get_rect()
        self.attack_rect.x = 0
        self.attack_rect.y = 200

    def update(self, enemy_attacks, enemy):
        self.TIMER += 1
        if self.TIMER == 40:
            enemy_attacks.pop()
            enemy.RAGE = False

    def draw(self,SCREEN2):
        SCREEN2.blit(self.image, (self.attack_rect.x, self.attack_rect.y))

class Champion:
    X_POS = 100
    Y_POS = 150
    HP = 5
    TASK1 = []
    TASK2 = -1
    TASK_NUM = 0
    def __init__(self):
        self.image = CHAMPION
        self.champ_rect = self.image.get_rect()
        self.champ_rect.x = self.X_POS
        self.champ_rect.y = self.Y_POS

    def draw(self, SCREEN3):
        SCREEN3.blit(self.image, (self.champ_rect.x, self.champ_rect.y))


class Demon:
    X_POS = 770
    Y_POS = 200
    HP = 3
    TASK1 = []
    TASK2 = -1
    TASK1_MAX_CNT = 5
    HARD = False
    def __init__(self):
        self.image = DEVIL
        self.demon_rect = self.image.get_rect()
        self.demon_rect.x = self.X_POS
        self.demon_rect.y = self.Y_POS
        self.task1_img = DARKNESS
        self.task1_rect1 = self.task1_img.get_rect()
        self.task1_rect2 = self.task1_img.get_rect()
        self.task1_rect3 = self.task1_img.get_rect()
        self.task1_rect1.x = SCREEN_WIDTH // 4 - 100
        self.task1_rect2.x = SCREEN_WIDTH // 2 - 100
        self.task1_rect3.x = SCREEN_WIDTH*3 / 4 - 100
        self.task1_rect1.y = SCREEN_HEIGHT - 200
        self.task1_rect2.y = SCREEN_HEIGHT - 200
        self.task1_rect3.y = SCREEN_HEIGHT - 200

    def task1(self, screen_type):
        if screen_type == 0:
            SCREEN.blit(self.task1_img, (self.task1_rect1.x, self.task1_rect1.y))
        elif screen_type == 1:
            SCREEN.blit(self.task1_img, (self.task1_rect2.x, self.task1_rect2.y))
        elif screen_type == 2:
            SCREEN.blit(self.task1_img, (self.task1_rect3.x, self.task1_rect3.y))

    def draw(self, SCREEN3):
        SCREEN3.blit(self.image, (self.demon_rect.x, self.demon_rect.y))