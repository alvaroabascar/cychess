class Errors:
    E001 = ("Invalid movement. A {piece_type} cannot move from "
            "{letter_start}{number_start} to {letter_destiny}{number_destiny}.")

    E002 = ("Position {position} is invalid. Position must be (x, y), where "
            "x in [0, 7] and y in [0,7].")

    E003 = ("Position {position} does not exist.")
