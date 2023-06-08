import pygame

class Settings():
    def __init__(self):
        ##############
        self.screenWidth = 600
        self.screenHeight = 600

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

        self.blackSquare = (179,112,77)
        self.whiteSquare = (204,159,51)


        
        