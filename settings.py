import pygame

class Settings():
    def __init__(self):
        ##############
        self.screenWidth = 512
        self.screenHeight = 512

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

        self.blackSquare = (179,112,77)
        self.whiteSquare = (204,159,51)


        
        