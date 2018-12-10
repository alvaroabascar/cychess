from .structs cimport PieceC
from .piece_properties import piece_color, piece_type

cdef class Piece:
    cdef PieceC* c
