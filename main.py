import pygame
import sys
from settings import Settings

class Chess:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption("Chess")


    def UpdateScreen(self):
            figures = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
            for row in range(8):
                    for col in range(8):
                        if (row + col) % 2 == 0:
                            color = self.settings.whiteSquare
                        else:
                            color = self.settings.blackSquare
                        
                        if row == 0:
                            for figure in figures:
                                image = pygame.image.load(f'figures/white/{figure}.png').convert_alpha()
                                new_image = pygame.transform.scale(image, (48, 48))
                                rect = image.get_rect()
                                self.screen.blit(image, (0, 0)) # допиши этот код 
                                    
                            
                        
                        pygame.draw.rect(self.screen, color, [col*64, row*64, 64, 64])

            pygame.display.flip()

    def RunGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    print(f'x = {x_mouse}, y = {y_mouse}')
            self.UpdateScreen()

    

    

if __name__ == '__main__':
    chess = Chess()
    chess.RunGame()




