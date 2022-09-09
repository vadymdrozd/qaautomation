from enum import Enum, auto, unique


@unique
class Gender(Enum):
    MALE = auto()
    FEMALE = auto()