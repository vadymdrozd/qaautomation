from enum import Enum


class Discount(Enum):
    UP_TO_100 = 0.005
    UP_TO_250 = 0.015
    UP_TO_300 = 0.02
    MORE_THAN_300 = 0.03
