import pygame
import sys
from settings import Settings


class Chess:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption("Chess")

    def RunGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            self._UpdateScreen()

    def _UpdateScreen(self):
        for row in range(8):
                for col in range(8):
                    if (row + col) % 2 == 0:
                        color = self.settings.whiteSquare
                    else:
                        color = self.settings.blackSquare
                    
                    pygame.draw.rect(self.screen, color, [col*63, row*63, 63, 63])

        pygame.display.flip()


if __name__ == '__main__':
    chess = Chess()
    chess.RunGame()




