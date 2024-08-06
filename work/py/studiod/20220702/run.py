import sys
import os
import  random
import pygame
import time
import random

import config
from scene.default import *
from scene.play import *

Background_x = 0
def main():
    pygame.font.init()
    pygame.mixer.init()
    pygame.init()
    pygame.display.set_caption("airplane2")
    dc = pygame.display.set_mode((config.map_width, config.map_height))
    clock = pygame.time.Clock()

    scene = Default()
    scene_type = config.scene_play
    while True:
        clock.tick(30)
        events = pygame.event.get()
        for event in events:
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.exit(1)
        if scene_type == config.scene_play:
            scene = Play()

        scene.trigger(events)
        scene.print(dc)
        scene_type=scene.next()
        pygame.display.update()
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()