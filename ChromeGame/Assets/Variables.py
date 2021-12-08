import pygame
import os


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


