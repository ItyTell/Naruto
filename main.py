
import pygame 
import json
from main_menu import *




class Game:

    def __init__(self) -> None:
        with open('settings.json') as file:
            settings = json.loads(file.read())
        pygame.init()
        self.screen = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))
        self.fps = settings["fps"]
        self.clock = pygame.time.Clock()
        self.running = True
        self.main_menu = MainMenu(self.screen)

    def run(self):
        

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("blue")
            self.main_menu.run(self.screen)
            pygame.display.flip()

        self.clock.tick(self.fps)  

        pygame.quit()
Game().run()

