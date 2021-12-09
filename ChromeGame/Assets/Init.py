import pygame
import os


SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELlOW = (255, 255, 0)

RUNNING = pygame.image.load(os.path.join("Assets/man", "Untitled.png"))

JUMPING = pygame.image.load(os.path.join("Assets/man", "Untitled.png"))

DUCKING = pygame.image.load(os.path.join("Assets/man", "Untitled1.png"))

OBS_AGE_18 = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "Boulder.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "Boulders.png"))]



OBS_AGE_19 = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
              pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

DRONE = [pygame.image.load(os.path.join("Assets/drone", "Drone.png")),
        pygame.image.load(os.path.join("Assets/drone", "DroneRed.png"))]

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

SHRINE = [pygame.image.load(os.path.join("Assets/Other", "Shrine.png"))]

SOVEREIGN = pygame.image.load(os.path.join("Assets/man", "Untitled2.png"))

#EYE = pygame.image.load(os.path.join("Assets/Enemy", somn.png))

BG2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", "BG3.jfif")), (SCREEN_WIDTH, SCREEN_HEIGHT + 100))

clock = pygame.time.Clock()