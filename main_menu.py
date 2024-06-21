
import pygame
pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 30)

class Button:

    def __init__(self, text, function) -> None:
        self.text = my_font.render(text, False, "black")
        self.function = function
    

    def draw(self, screen, cords):
        screen.blit(self.text, cords)


    def click(self):
        self.function()



class MainMenu:
    
        def __init__(self, screen) -> None:
            self.buttons = [
                Button("Start", self.start_game),
                Button("Exit", self.exit)
            ]
            self.running = True
    
        def start_game(self):
            pass

        def exit(self):
            self.running = False
    
        def run(self, screen):
            for i, button in enumerate(self.buttons):
                button.draw(screen, (100, 100 + i * 50))

