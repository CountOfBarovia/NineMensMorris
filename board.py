# Object to store the layout of the board

class board:
    def __init__(self):
        self.contents = [[0 for i in range(0, 9)] for i in range(0, 9)]