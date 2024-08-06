from scene.default import *
import config
import scene.play as play
import pygame

class End(Default):
    def __init__(self,dc,events):
        self.dc=dc
        self.events=events
        self.scene_name = config.scene_end
    def print(self):
        dc = self.dc
        dc.fill((0,0,0))
        font = pygame.font.Font(None, 100)
        text = font.render("GAME OVER", True, (255,0,0))
        dc.blit(text, (300,230))

    def trigger(self):
        events = self.events
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    self.init()
                    self.scene_name=config.scene_play
    def next(self):
        return self.scene_name
    def init(self):
        play.user_x = 30
        play.user_y = 0
        play.user_speed = 3
        
        play.bullet_list = []
        play.fireball_list = []
        play.fireball_get = 0

        play.bat_list = []
        play.bat_last_time = 0

        play.score = 0
        play.life = 3