class Tile:

    def __init__(self, has_mine):
        self.has_mine = has_mine
        self.has_dug = False

    def dig(self):
        self.has_dug = True
