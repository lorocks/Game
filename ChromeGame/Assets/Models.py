import pygame
import os
import random


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


RUNNING = pygame.image.load(os.path.join("Assets/man", "Untitled.png"))

JUMPING = pygame.image.load(os.path.join("Assets/man", "Untitled.png"))

DUCKING = pygame.image.load(os.path.join("Assets/man", "Untitled1.png"))

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

DRONE = [pygame.image.load(os.path.join("Assets/drone", "Drone.png")),
        pygame.image.load(os.path.join("Assets/drone", "DroneRed.png"))]

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

class Man:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.man_duck = False
        self.man_run = True
        self.man_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS

    def update(self, userInput):
        if self.man_duck:
            self.duck()
        if self.man_run:
            self.run()
        if self.man_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.man_jump:
            self.man_duck = False
            self.man_run = False
            self.man_jump = True
        elif userInput[pygame.K_DOWN] and not self.man_jump:
            self.man_duck = True
            self.man_run = False
            self.man_jump = False
        elif not (self.man_jump or userInput[pygame.K_DOWN]):
            self.man_duck = False
            self.man_run = True
            self.man_jump = False

    def duck(self):
        self.image = self.duck_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.man_jump:
            self.man_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.man_jump = False
            self.jump_vel = self.JUMP_VEL

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
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


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
