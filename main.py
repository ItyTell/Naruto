
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
        self.main_menu = Main_menu(self.screen)
        self.game_started = False

    def run(self):
        

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.main_menu.buttons:
                        if button.rect.collidepoint(event.pos):
                            self.game_started, self.running = button.click()

            self.main_menu.run()
            pygame.display.flip()
            self.clock.tick(self.fps)  

        pygame.quit()
Game().run()

