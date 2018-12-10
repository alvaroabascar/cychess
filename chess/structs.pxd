from libcpp cimport bool

from .piece_properties cimport piece_color, piece_type

cdef struct PieceC:
    char position_x
    char position_y
    piece_color color
    piece_type type
    bool eaten
