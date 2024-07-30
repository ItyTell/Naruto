
import pygame 
import json
from main_menu import *
from level import *




class Game:

    def __init__(self) -> None:
        with open('settings.json') as file:
            settings = json.loads(file.read())
        pygame.init()
        self.screen = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))
        self.fps = settings["fps"]
        self.clock = pygame.time.Clock()
        self.running = True
        self.main_menu = Main_menu(self.screen)
        self.game_started = False
        self.level = Level(self.screen)
    
    def keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.main_menu.running:
                    self.game_started, self.running = self.main_menu.button_check(pygame.mouse.get_pos())


    def run(self):

        while self.running:

            self.keys_pressed()

            if self.main_menu.running:
                self.main_menu.run()
            elif self.game_started:
                self.level.run()

            pygame.display.flip()
            self.clock.tick(self.fps)  

        pygame.quit()

if __name__ == "__main__":
    Game().run()

