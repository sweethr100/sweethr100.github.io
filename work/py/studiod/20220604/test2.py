from cv2 import transform
import pygame
import sys
import time
import os
import random

MAP_WIDTH = 480
MAP_HEIGHT = 640

def main():
    pygame.font.init()
    pygame.init()
    pygame.display.set_caption("test")
    dc = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
    clock = pygame.time.Clock()
    time = pygame.time.get_ticks()

    for i in pygame.font.get_fonts():
        print(i)
    
    rol = 0
    rockImg = "resource/rock%02d.png"% random.randint(1, 30)
    while True:
        r = random.randint(280,310)
        rol+=random.randint(1,7)
        events = pygame.event.get()
        for event in events:
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.exit(1)

        dc.fill((255,255,255))

        font = pygame.font.SysFont("resource/Mabinogi_Classic_TTF.ttf",30,False,False)
        text = font.render("안녕aa!", True, (255,0,0))
        dc.blit(text,(100,100))

        img = pygame.image.load(rockImg)
        img = pygame.transform.scale(img,(r,r))
        img = pygame.transform.rotate(img,rol)
        dc.blit(img,(50,50))

        clock.tick(30)
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()