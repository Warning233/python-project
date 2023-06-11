from settings import Settings
import pygame


class Piece:
    def __init__(self, color: str = None):
        self.color = color

    def move_to_cell(self, cell):
        self.rect = cell.rect.copy()
        self.field_name = cell.field_name

    def load_image(self, image_path, width=64, height=64):
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.smoothscale(image, (width, height))
        except pygame.error as e:
            print(f"Error! {image_path}: {e}")
            return None

        return image

    def image(self):
        raise NotImplementedError("Method 'image' must be implemented in subclasses.")

    @classmethod
    def create(cls, piece_name: str, color: str):
        if piece_name == 'Rook':
            return Rook(color).image()
        elif piece_name == 'Bishop':
            return Bishop(color).image()
        elif piece_name == 'Knight':
            return Knight(color).image()
        elif piece_name == 'Queen':
            return Queen(color).image()
        elif piece_name == 'King':
            return King(color).image()
        elif piece_name == 'Pawn':
            return Pawn(color).image()
        else:
            raise ValueError(f"Invalid piece name: {piece_name}")

    

class Pawn(Piece):
    def __init__(self, color):
       self.has_moved = False
       super().__init__(color)
       
    
    def _canAttack(self, target_row: int, target_col: int, current_row: int, current_col: int) -> bool:
        if abs(target_row - current_row) == 1 and abs(target_col - current_col) == 1:
            if self.color == 'white' and target_row < current_row:
                return True
            elif self.color == 'black' and target_row > current_row:
                return True
            
        return False
    
  
    
    def image(self):
        return self.load_image(f'pieces/{self.color}/pawn.png')

        
    #def _firstMove(self, current_row: int, current_col: int) -> None:
       # if not self.has_moved:
           # if current


class Rook(Piece):
    def __init__(self, color):
        self.has_moved = False
        super().__init__(color)

 
    
    def image(self):
        return self.load_image(f'pieces/{self.color}/rook.png')


    

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def image(self):
        return self.load_image(f'pieces/{self.color}/bishop.png')


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def image(self):
        return self.load_image(f'pieces/{self.color}/knight.png')

        

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    
    def image(self):
        return self.load_image(f'pieces/{self.color}/queen.png')


class King(Piece):
    def __init__(self, color):
        self.has_moved = False
        super().__init__(color)

    def image(self):
        return self.load_image(f'pieces/{self.color}/king.png')

