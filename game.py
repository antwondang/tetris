from grid import Grid
from blocks import *

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [iBlock(), JBlock(), LBlock(), oBlock(), tBlock(), sBlock(), zBlock()]
