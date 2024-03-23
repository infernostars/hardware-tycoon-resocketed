from enum import IntEnum


class ChipType(IntEnum):
    CPU = 0


class Chip:
    def __init__(self, ctype: ChipType):
        self.chip_type = ctype
