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

STARTBG = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", "StartBG.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

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

#Guide
RUNGUIDE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Guide", "RunGuide.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
EYEATTACKSGUIDE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Guide", "EyeFightGuide.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
EYESHOOTGUIDE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Guide", "EyeShootGuide.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
BOSSATTACKGUIDE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Guide", "BossAttack.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

#Dialogues
INTRODIALOGUE = ["","The World was a peaceful place until"," one day Demons invaded. They spread chaos", " and man could only run away in fear."]
INTRODIALOGUEEND = "Escape at all costs"

FIELDDIALOGUE = ["", "After running for a long time you", "come across a Shrine which is radiant.", "An angel appears and says, \" Pitiful Man,", "You Who Have Suffered The Horrors" , "Now Become The Hero Of Mankind.", "Accept This Holy Axe Rhitta. Kill,", "Grow Stronger And Avenge The Fallen\"", "Magically an axe appears before you", "just before waves of demons surrond", "you from everywhere."]
FIELDDIALOGUEEND = "Kill the Field Boss to Escape"

EYEDIALOGUE = ["", "After beating the field boss Galand,", "bright balls float into Rhitta from", "the bodies of the dead demons. You feel", "power flowing into you as more light is absorbed.", "A different angel descends in front of you,", "saying \"Worthy One Who Wields Rhitta Blessed", "With The Power Of The Sun, Vanquish All", "Evil And Destroy The Darkness That Is", "Estarossa\". The angel waves her hand", "and a portal open in front of you where", "you see a Giant Eye guarding a dark gateway", "\" Defeat The Eye To Gain Access To", "Estarossa's Realm. Beat Him And Save Humanity\""]
EYEDIALOGUEEND = "Kill the Eye Monster"

BOSSDIALOGUE = ["", "You stare are the dark portal that", "leads to Estarossa. The leader of Darkness,", "he who has power over it. You", "step through the portal expecting a", "bleak landscape, instead you are at a river", "and Estarossa is there waiting for you."]
BOSSDIALOGUEEND = "Kill Estarossa and Save the World"