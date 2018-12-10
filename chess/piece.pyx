# cython: language_level=3
from libc.stdlib cimport malloc, free
from .piece_properties cimport piece_color, piece_type
from .structs cimport PieceC
from .errors import Errors


cdef class Piece:
    def __cinit__(self,
                  piece_color color,
                  piece_type piece_type,
                  str position):
        
        self.c = <PieceC*>malloc(sizeof(PieceC))

    def __dalloc__(self):
        free(self.c)

    def __init__(self,
                 piece_color color,
                 piece_type piece_type,
                 str position):
        
        self.c[0].color = <piece_color>color
        self.c[0].type = piece_type
        self.c[0].eaten = False
        self.position = position

    @property
    def position_(self):
        return (self.c[0].position_x, self.c[0].position_y)

    @position_.setter
    def position_(self, value):
        x, y = value
        if (type(x) != int or type(y) != int or
            not 0 <= x <= 7 or not 0 <= y <= 7):
            raise ValueError(Errors.E003.format(position=value))
        
        self.c[0].position_x = x
        self.c[0].position_y = y
            


    @property
    def position(self):
        letters = 'ABCDEFGH'
        if self.c[0].position_x < 0 or self.c[0].position_y < 0:
            return ""
        
        x, y = self.c[0].position_x, self.c[0].position_y
        return '{}{}'.format(letters[x], y + 1)

    @position.setter
    def position(self, value):
        letters = 'ABCDEFGH'
        letter = value[0]
        try:
            assert type(value) == str
            assert len(value) == 2
            x = letters.index(letter)
            y = int(value[1]) - 1
            assert 0 <= y <= 7
        except Exception:
            raise ValueError(Errors.E003.format(position=value))
        self.position_ = (x, y)

    @property
    def type(self):
        return self.c[0].type

    @property
    def color(self):
        return self.c[0].color

    @property
    def eaten(self):
        return self.c[0].eaten

    @eaten.setter
    def eaten(self, value):
        """Sets eaten to True and position to (-1, -1)."""
        self.c[0].eaten = value
        if value:
            self.c[0].position_x = -1
            self.c[0].position_y = -1        
