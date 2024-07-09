
import pygame
pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 100)

class Button:

    indantation = 0

    def __init__(self, text, function, cords) -> None:
        self.text = my_font.render(text, False, "white")
        self.function = function
        rect = self.text.get_rect()
        self.rect = pygame.Rect(cords[0] - 100 - rect.left, cords[1] + Button.indantation, rect.width, rect.height)
        Button.indantation += rect.height
    

    def draw(self, screen, cords):
        screen.blit(self.text, cords)


    def click(self):
        return self.function()



class Main_menu:
    
        def __init__(self, screen) -> None:
            self.buttons = [
                Button("Start", self.start_game, (screen.get_width() / 2, screen.get_height() / 4)),
                Button("Exit", self.exit, (screen.get_width() / 2, screen.get_height() / 4))
            ]
            self.running = True
            self.screen = screen
            self.width = screen.get_width()
            self.height = screen.get_height()
    
        def start_game(self):
            return True, True

        def exit(self):
            self.running = False
            return False, False
    
        def run(self):
            if self.running:
                self.screen.fill("blue")
                for button in self.buttons:
                    button.draw(self.screen, (button.rect.x, button.rect.y))

