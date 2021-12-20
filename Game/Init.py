import pygame
import os


SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

EYE_HEIGHT = 200
EYE_WIDTH = 125
EYE_DIM = (EYE_WIDTH, EYE_HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 170, 0)
RED = (255,0,0)

PRIDE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "lionsin.jpg")), (90,90))

SPAWN = [pygame.image.load(os.path.join("Assets/Field", "Goblin.jpg")),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Ogre.jpg")), (90,90)),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Orc.jpg")), (90,90)),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Lich.jpg")), (90,90)),
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Field", "Dracula.jpg")), (90,90))]

BOSS = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Enemy", "Galand.png")), (100,200))

RUNNING = pygame.image.load(os.path.join("Assets/Hero", "Weakling.png"))

JUMPING = pygame.image.load(os.path.join("Assets/Hero", "Weakling.png"))

DUCKING = pygame.image.load(os.path.join("Assets/Hero", "Duck.png"))

OBS_AGE_18 = [pygame.image.load(os.path.join("Assets/Obstacles", "SmallCactus1.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "SmallCactus2.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "LargeCactus1.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "LargeCactus2.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Boulder.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Boulders.png"))]

OBS_AGE_19 = [pygame.image.load(os.path.join("Assets/Obstacles", "ManEater.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Fire.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Lycoris.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Spikes.png")),
              pygame.image.load(os.path.join("Assets/Obstacles", "Swords.png"))]

DRONE = [pygame.image.load(os.path.join("Assets/Obstacles", "Drone.png")),
        pygame.image.load(os.path.join("Assets/Obstacles", "DroneRed.png"))]

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

SHRINE = [pygame.image.load(os.path.join("Assets/Other", "Shrine.png"))]

SOVEREIGN = pygame.image.load(os.path.join("Assets/Hero", "Sovereign.png"))

BULLET = pygame.transform.rotate(pygame.image.load(os.path.join("Assets/Hero", "rhitta.png")), -45)
BULLET = pygame.transform.scale(BULLET, (120, 70))

EYE = pygame.image.load(os.path.join("Assets/Enemy", "Eye.png"))
EYE = pygame.transform.scale(EYE, EYE_DIM)

WEAKNESS = pygame.image.load(os.path.join("Assets/Enemy", "Weak.png"))

ATTACK1 = pygame.image.load(os.path.join("Assets/Enemy", "Attack.png"))

ATTACK2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Enemy", "Attack.png")), (SCREEN_WIDTH - 200, 300))

BG2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", "BG3.jfif")), (SCREEN_WIDTH, SCREEN_HEIGHT + 100))

CHAMPION = pygame.image.load(os.path.join("Assets/Hero", "Champion_.png"))
CHAMPION_SHOW = pygame.transform.scale(CHAMPION, (250,200))

DEVIL = pygame.image.load(os.path.join("Assets/Enemy", "Devil_.png"))

DARKNESS = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Enemy", "Darkness_.png")), (175,125))

BG3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", "vs2.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))
BG3SWITCH = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", "BGAfter.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

FINALBG = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", "FinalBG.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()