from scene.default import *
import pygame
import config

class Scene1(Default):
    def __init__(self):
        self.scene_name = config.scene_scene1
    def print(self,dc):
        dc.fill((255,0,0))
    def trigger(self,events):
        for event in events:
            if pygame.MOUSEBUTTONDOWN == event.type:
                self.scene_name = config.scene_scene2
    def next(self):
        return self.scene_name