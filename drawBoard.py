import pygame
from settings import Settings

figures = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

def _UpdateScreen(self):
        for row in range(8):
                for col in range(8):
                    if (row + col) % 2 == 0:
                        color = self.settings.whiteSquare
                    else:
                        color = self.settings.blackSquare
                    
                    if row == 0 and col == 0:
                        for figure in figures:
                            image = pygame.image.load(f'figures/white/{figure}.png')
                            pygame.draw.rect((32, 32), 64, 64)
                                
                        
                    
                pygame.draw.rect(self.screen, color, [col*64, row*64, 64, 64])

        pygame.display.flip()