import socket
import pygame
import sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
Audio = pygame.mixer.Sound("Assets/Audio/MahitoDomainExpansion.mp3")
Audio.play()

class UdpToPygame():

    def __init__(self):
        UDP_IP="127.0.0.1"
        UDP_PORT=15006
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(0)
        self.sock.bind((UDP_IP,UDP_PORT))

    def update(self):
        try:
            data, addr = self.sock.recvfrom(1024)
            ev = pygame.event.Event(pygame.USEREVENT, {'data': data, 'addr': addr})
            pygame.event.post(ev)
        except socket.error:
            pass

def main():
    dispatcher = UdpToPygame()
    screen = pygame.display.set_mode((800, 600))
    l = 0
    r = True
    while r:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                r = False
            if ev.type == pygame.USEREVENT:
                t = pygame.font.SysFont('', 40).render(ev.data, True, (255,255,255))
                screen.blit(t, (0, l*20))
                l += 1
        dispatcher.update()
        pygame.display.flip()

def test():


    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font_dialogue = pygame.font.Font('freesansbold.ttf', 20)
    def display_text_animation(string):
        text = ''
        for i in range(len(string)):
            DISPLAYSURF.fill(WHITE)
            text += string[i]
            text_surface = font_dialogue.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            DISPLAYSURF.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(175)

    def main():
        count = 0
        counting = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == pygame.KEYDOWN:
                    pygame.quit()
                    sys.exit()
            if count == 100:
                Audio.stop()

            if not pygame.mixer.get_busy():
                Audio.play()
            count += 1
            clock.tick(20)
            print(count)


    display_text_animation('Hello World!')
    main()


if __name__ == "__main__":
    test()
