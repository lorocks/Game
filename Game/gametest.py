import pygame
import socket
import os
import sys
import random
import pyfirmata
from pynput.keyboard import Key, Controller
keyboard = Controller()

board = pyfirmata.Arduino('COM8')
it = pyfirmata.util.Iterator(board)
it.start()
pygame.init()


# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
RUNNING = pygame.image.load(os.path.join("Assets/Hero", "Weakling.png"))

PRIDE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "lionsin.jpg")), (90,90))

JUMPING = pygame.image.load(os.path.join("Assets/Hero", "Weakling.png"))

DUCKING = pygame.image.load(os.path.join("Assets/Hero", "Duck.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

OBS_AGE_18 = [pygame.image.load(os.path.join("Assets/Obstacles", "SmallCactus1.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "SmallCactus2.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "LargeCactus1.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "LargeCactus2.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Boulder.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Boulders.png"))]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 170, 0)
RED = (255,0,0)

SPAWN = [pygame.image.load(os.path.join("Assets/Field", "Goblin.jpg")),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Ogre.jpg")), (90,90)),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Orc.jpg")), (90,90)),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Lich.jpg")), (90,90)),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Dracula.jpg")), (90,90))]

class Weakling:
    X_POS = 105
    Y_POS = 105
    POWER_LVL = 5
    def __init__(self):
        self.image = PRIDE
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))


class Map:
    def __init__(self):
        self.field = random.randint(0,2)
        self.SPAWN_SITE = [[random.randint(0,2) for i in range(9)] for j in range(5)]
        self.SPAWN_SITE[0][0] = -1
        if self.field == 0:
            self.SPAWN_SITE [0][1] = 0
        elif self.field == 1:
            self.SPAWN_SITE[1][0] = 0
        elif self.field == 2:
            self.SPAWN_SITE[0][1] = 0
            self.SPAWN_SITE[1][0] = 0
        for i in range(2):
            for j in range(8):
                self.SPAWN_SITE[i+3][j] += 2
        for i in range(3):
            for j in range(2):
                self.SPAWN_SITE[i][j+7] += 2
        self.SPAWN_SITE[4][8] = -1
        self.SPAWN_SITE[3][8] = -1


class Spawn:
    def __init__(self, type, i, j):
        self.type = type
        if self.type == 0:
            self.power = 3
        elif self.type == 1:
            self.power = 5
        elif self.type == 2:
            self.power = 10
        elif self.type == 3:
            self.power = 25
        elif self.type == 4:
            self.power = 50
        self.image = SPAWN[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = (i * 100) + 105
        self.rect.y = (j * 100) + 105

    def populate(self, SCREEN):
        font = pygame.font.Font('freesansbold.ttf', 20)
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        Power = font.render(str(self.power), 1, YELLOW)
        SCREEN.blit(Power, (self.rect.x, self.rect.y))

BOSS = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Enemy", "Galand.png")), (100,200))

class Boss:
    X_POS = 900
    Y_POS = 400
    POWER_LVL = 500
    def __init__(self):
        self.image = BOSS
        self.boss_rect = self.image.get_rect()
        self.boss_rect.x = self.X_POS
        self.boss_rect.y = self.Y_POS

    def draw(self, SCREEN):
        font = pygame.font.Font('freesansbold.ttf', 20)
        SCREEN.blit(self.image, (self.boss_rect.x, self.boss_rect.y))
        Power = font.render(str(self.POWER_LVL), 1, RED)
        SCREEN.blit(Power, (self.boss_rect.x, self.boss_rect.y))


digital_input_down = board.get_pin('d:10:i')
digital_input_up = board.get_pin('d:11:i')
digital_input_space = board.get_pin('d:9:i')

"""class UdpToPygame():

    def __init__(self):
        UDP_IP="127.0.0.1"
        UDP_PORT=15006
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(0)
        self.sock.bind((UDP_IP,UDP_PORT))

    def update(self):
        try:
            data, addr = self.sock.recvfrom(1024)
            event = pygame.event.Event(pygame.USEREVENT, {'data': data, 'addr': addr})
            pygame.event.post(event)
        except socket.error:
            pass"""
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
        self.video_value = 0
        if self.type == 0 or self.type == 1:
            self.rect.y = 325
        elif self.type == 2 or self.type == 3:
            self.rect.y = 300
        else:
            self.rect.y = 335
            self.video_value = 1

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


def controller():
    downSwitch = digital_input_down.read()
    upSwitch = digital_input_up.read()
    spaceSwitch = digital_input_space.read()
    if downSwitch is True:
        userInput = pygame.key.ScancodeWrapper((
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, True, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False,
            False, False))
    if upSwitch is True:
        userInput = pygame.key.ScancodeWrapper((False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, True, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False, False, False, False, False, False, False, False, False,
                                                False, False))
        # above is userinput tuple for jump
        if spaceSwitch is True:
            userInput = pygame.key.ScancodeWrapper((False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, True, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False, False, False, False, False,
                                    False, False, False, False, False, False, False, False))
            #above is for space"""

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    #dispatcher = UdpToPygame()
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    first = False
    count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False




        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()

        #controller()

        downSwitch = digital_input_down.read()
        upSwitch = digital_input_up.read()
        spaceSwitch = digital_input_space.read()
        if downSwitch is True:
            keyboard.press(Key.down)
            #first = True
        if upSwitch is True:
            keyboard.press(Key.up)
            #first = True
        if spaceSwitch is True:
            keyboard.press(Key.space)
            #first = True
        if downSwitch is False:
            keyboard.release(Key.down)
            #first = True
        if upSwitch is False:
            keyboard.release(Key.up)
            #first = True
        if spaceSwitch is False:
            keyboard.release(Key.space)
            #first = True
        player.draw(SCREEN)
        player.update(userInput)

        if first:
            count+=1


        background()

        if len(obstacles) == 0:
            obstacles.append(SmallCactus(OBS_AGE_18))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed,obstacles)

            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                menu(1)

        score()

        clock.tick(30)
        #dispatcher.update()
        pygame.display.update()
        death_count += 1

def Background1(player):
    global font_health
    font_health = pygame.font.Font('freesansbold.ttf', 20)
    powerLvl = font_health.render("Power Level: " + str(player.POWER_LVL), 1, BLACK)
    SCREEN.blit(powerLvl, (10, 10))
    blockSize = 100
    for x in range(100, SCREEN_WIDTH - 100, blockSize):
        for y in range(100, SCREEN_HEIGHT - 100, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

def get_map(field, player):
    global totalPower
    totalPower = 0
    for i in range(5):
        for j in range(9):
            if not field.SPAWN_SITE[i][j] == -1:
                spawn = Spawn(field.SPAWN_SITE[i][j], j, i)
                spawn.populate(SCREEN)
                totalPower += spawn.power
                if player.rect.colliderect(spawn.rect):
                    if player.POWER_LVL > spawn.power:
                        player.POWER_LVL += spawn.power
                    elif player.POWER_LVL == spawn.power:
                        player.POWER_LVL += 2
                    elif player.POWER_LVL + 2 >= spawn.power:
                        player.POWER_LVL -= 1
                    else:
                        menu(8, 0)
                    field.SPAWN_SITE[i][j] = -1

def isDoable():
    if totalPower < 600:
        FirstStage()

def FirstStage():
    doableCheck = False
    player = Weakling()
    field = Map()
    enemy = Boss()
    while 1:
        SCREEN.fill(WHITE)
        Background1(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.rect.x > 105:
                        player.rect.x -= 100
                if event.key == pygame.K_UP:
                    if player.rect.x < 905:
                        player.rect.x += 100
                if event.key == pygame.K_DOWN:
                    if player.rect.y < 505:
                        player.rect.y += 100

        downSwitch = digital_input_down.read()
        upSwitch = digital_input_up.read()
        spaceSwitch = digital_input_space.read()
        if downSwitch is True:
            keyboard.press(Key.down)
            # first = True
        if upSwitch is True:
            keyboard.press(Key.up)
            # first = True
        if spaceSwitch is True:
            keyboard.press(Key.space)
            # first = True
        if downSwitch is False:
            keyboard.release(Key.down)
            # first = True
        if upSwitch is False:
            keyboard.release(Key.up)
            # first = True
        if spaceSwitch is False:
            keyboard.release(Key.space)
            # first = True

        get_map(field, player)
        if not doableCheck:
            isDoable()
            doableCheck = True

        if player.rect.colliderect(enemy.boss_rect):
            if player.POWER_LVL >= enemy.POWER_LVL:

                menu(2)
            else:

                menu(8)

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        pygame.display.update()



def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        userInput = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                FirstStage()

        downSwitch = digital_input_down.read()
        upSwitch = digital_input_up.read()
        spaceSwitch = digital_input_space.read()
        if downSwitch is True:
            keyboard.press(Key.down)
        if upSwitch is True:
            keyboard.press(Key.up)
        if spaceSwitch is True:
            keyboard.press(Key.space)

menu(death_count=0)
