from block import Block
from position import Position

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {}
