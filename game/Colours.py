"""Import enum module."""
from enum import Enum


class col(Enum):
    """Emun to represent colours in RGB."""

    # define colours you want to use here.
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    DARKRED = (128, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 128, 0)
    BLUE = (0, 0, 255)

    # background colour
    BACKGROUND = (100, 100, 255)
