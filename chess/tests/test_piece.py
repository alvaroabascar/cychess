import pytest

from ..piece import Piece
from ..piece_properties import COLOR_IDS, PIECE_TYPE_IDS
from ..errors import Errors


@pytest.mark.parametrize('color,piece_type', [
    (('WHITE', 'KNIGHT')),
    (('BLACK', 'KNIGHT')),
    (('BLACK', 'PAWN')),
    (('BLACK', 'QUEEN')),
    (('WHITE', 'BISHOP'))
])
def test_initialization(color, piece_type):
    piece = Piece(
        color=COLOR_IDS[color],
        piece_type=PIECE_TYPE_IDS[piece_type],
        position="A1"
    )
    assert piece.position_ == (0, 0)
    assert piece.type == PIECE_TYPE_IDS[piece_type]
    assert piece.color == COLOR_IDS[color]
    assert piece.eaten == False


@pytest.mark.parametrize('position_', [(1, 2)])
def test_set_position_(position_):
    piece = Piece(
        color=COLOR_IDS['WHITE'],
        piece_type=PIECE_TYPE_IDS['KNIGHT'],
        position="A1"
    )
    assert piece.position_ == (0, 0)
    piece.position_ = position_

    assert piece.position_ == position_


@pytest.mark.parametrize('position,position_', [
    ("B4", (1, 3)),
    ("C8", (2, 7)),
    ("H5", (7, 4))])
def test_set_position(position, position_):
    piece = Piece(
        color=COLOR_IDS['WHITE'],
        piece_type=PIECE_TYPE_IDS['KNIGHT'],
        position="A1"
    )
    assert piece.position_ == (0, 0)
    piece.position = position

    assert piece.position_ == position_


@pytest.mark.parametrize('position,name', [
    ((0, 0), "A1"),
    ((0, 1), "A2"),
    ((0, 2), "A3"),
    ((0, 3), "A4"),
    ((7, 7), "H8"),
])
def test_position_name(position, name):
    piece = Piece(
        color=COLOR_IDS['WHITE'],
        piece_type=PIECE_TYPE_IDS['KNIGHT'],
        position="A1"
    )
    assert piece.position_ == (0, 0)
    assert piece.position == "A1"
    piece.position = name
    assert piece.position_ == position
    assert piece.position == name


@pytest.mark.parametrize('bad_position', [
    "A9",
    "A10",
    "J8",
    "A0"
])
def test_wrong_position_raises_value_error(bad_position):
    piece = Piece(
        color=COLOR_IDS['WHITE'],
        piece_type=PIECE_TYPE_IDS['KNIGHT'],
        position="A1"
    )
    assert piece.position_ == (0, 0)
    assert piece.position == "A1"

    with pytest.raises(ValueError):
        print(dir(piece))
        piece.position = bad_position


def test_eat_piece():
    piece = Piece(
        color=COLOR_IDS['WHITE'],
        piece_type=PIECE_TYPE_IDS['KNIGHT'],
        position="A1"
    )
    assert piece.eaten == False
    assert piece.position == "A1"
    assert piece.position_ == (0, 0)

    piece.eaten = True
    assert piece.eaten == True
    assert piece.position == ""
    assert piece.position_ == (-1, -1)
