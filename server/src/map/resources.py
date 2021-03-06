from enum import Enum


class ResourceType(Enum):
    """
    Enumeration of all the possible types of tiles
    """
    NONE = 0
    WATER = 1
    IRON = 2
    COPPER = 3
    FOOD = 4
    WOOD = 5
    OIL = 6
    COAL = 7
    GOLD = 8
