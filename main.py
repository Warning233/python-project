import pygame
import sys
from ChessBoard import Board
from settings import Settings

class Chess:
    def __init__(self):
        self.settings = Settings()
        self.board = Board()
        self.screen = self.settings.screen
        pygame.display.set_caption("Chess")


    def UpdateScreen(self):
            self.board._drawBoard()
            self.board._drawChessPieces()
            pygame.display.update()
            

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




