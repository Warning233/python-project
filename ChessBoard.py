import pygame
from settings import Settings


class Board():
    def __init__(self):
        self.settings = Settings()
        self.chessPieces = {
             'wRook': self._load_image('pieces/white/rook.png'),
             'wBishop': self._load_image('pieces/white/bishop.png'),
             'wKnight': self._load_image('pieces/white/knight.png'),
             'wQueen': self._load_image('pieces/white/queen.png'),
             'wKing': self._load_image('pieces/white/king.png'),
             'wPawn': self._load_image('pieces/white/pawn.png'),
             ####################################################
             'bRook': self._load_image('pieces/black/rook.png'),
             'bBishop': self._load_image('pieces/black/bishop.png'),
             'bKnight': self._load_image('pieces/black/knight.png'),
             'bQueen': self._load_image('pieces/black/queen.png'),
             'bKing': self._load_image('pieces/black/king.png'),
             'bPawn': self._load_image('pieces/black/pawn.png')             
        }      

    def _drawBoard(self):
        for row in range(8):
                    for col in range(8):
                        if (row + col) % 2 == 0:
                            color = self.settings.whiteSquare
                        else:
                            color = self.settings.blackSquare                                                     
                        
                        pygame.draw.rect(self.settings.screen, color, [col*64, row*64, 64, 64])



    def _drawChessPieces(self):
         chessPositions = [
              ('bRook', 0, 0),
              ('bKnight', 1, 0),
              ('bBishop', 2, 0),
              ('bQueen', 3, 0),
              ('bKing', 4, 0),
              ('bBishop', 5, 0),
              ('bKnight', 6, 0),
              ('bRook', 7, 0),
              ('bPawn', 0, 1),
              ('bPawn', 1, 1),
              ('bPawn', 2, 1),
              ('bPawn', 3, 1),
              ('bPawn', 4, 1),
              ('bPawn', 5, 1),
              ('bPawn', 6, 1),
              ('bPawn', 7, 1),
              ####################
              ('wRook', 0, 7),
              ('wKnight', 1, 7),
              ('wBishop', 2, 7),
              ('wQueen', 3, 7),
              ('wKing', 4, 7),
              ('wBishop', 5, 7),
              ('wKnight', 6, 7),
              ('wRook', 7, 7),
              ('wPawn', 0, 6),
              ('wPawn', 1, 6),
              ('wPawn', 2, 6),
              ('wPawn', 3, 6),
              ('wPawn', 4, 6),
              ('wPawn', 5, 6),
              ('wPawn', 6, 6),
              ('wPawn', 7, 6)
            
         ]

         for piece, col, row in chessPositions:
              x = col * 64
              y = row * 64

              piece_image = self.chessPieces[piece]
              self.settings.screen.blit(piece_image, (x, y))


    def _load_image(self, image_path, width=64, height=64):
        try:
              image = pygame.image.load(image_path)
              image = pygame.transform.smoothscale(image, (width, height))

        except pygame.error as e:
             print(f"Error! {image_path}: {e}")
             return None
        return image

         
