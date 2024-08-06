from scene.default import *
import pygame
import config

class Scene2(Default):
    def __init__(self):
        self.scene_name = config.scene_scene2
    def print(self,dc):
        dc.fill((0,0,255))
    def trigger(self,events):
        for event in events:
            if pygame.MOUSEBUTTONDOWN == event.type:
                self.scene_name = config.scene_scene1
    def next(self):
        return self.scene_name