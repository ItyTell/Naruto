import pygame

class Level:

    def __init__(self, screen) -> None:
        self.background = pygame.image.load("images\\backgrounds\\1.png")
        self.background = pygame.transform.scale(self.background.subsurface((1, 1, 515, 130)), (514 * 720/130, 720))
        self.screen = screen

    def run(self):

        self.screen.fill("white")
        self.screen.blit(self.background, (0, 0))
