# Object to store the layout of the board
import pygame, globals

class board:
    def __init__(self):
        self.contents = [[0 for i in range(0, 8)] for i in range(0, 3)]
        self.side = 400
        self.relpoints = [[(self.side / 14, self.side / 14), (self.side / 2, self.side / 14), (self.side / 14 * 13, self.side / 14),
                        (self.side / 14 * 13, self.side / 2),
                        (self.side / 14 * 13, self.side / 14 * 13), (self.side / 2, self.side / 14 * 13), (self.side / 14, self.side / 14 * 13),
                        (self.side / 14, self.side / 2)],
                        [(self.side / 14 * 3, self.side / 14 * 3), (self.side / 2, self.side / 14 * 3), (self.side / 14 * 11, self.side / 14 * 3),
                        (self.side / 14 * 11, self.side / 2),
                        (self.side / 14 * 11, self.side / 14 * 11), (self.side / 2, self.side / 14 * 11), (self.side / 14 * 3, self.side / 14 * 11),
                        (self.side / 14 * 3, self.side / 2)],
                        [(self.side / 14 * 5, self.side / 14 * 5), (self.side / 2, self.side / 14 * 5), (self.side / 14 * 9, self.side / 14 * 5),
                        (self.side / 14 * 9, self.side / 2),
                        (self.side / 14 * 9, self.side / 14 * 9), (self.side / 2, self.side / 14 * 9), (self.side / 14 * 5, self.side / 14 * 9),
                        (self.side / 14 * 5, self.side / 2)]]
        self.offset = (globals.ScreenW - self.side) / 2
        self.actualpoints = self.relpoints
        for square in range(len(self.actualpoints)):
            for point in range(len(self.actualpoints[square])):
                self.actualpoints[square][point] = (self.actualpoints[square][point][0] + self.offset, self.actualpoints[square][point][1] + self.offset)
        self.rect = pygame.rect.Rect(self.offset, self.offset, self.side, self.side)
        self.col = (255, 227, 191)
        self.pointcol = (71, 45, 18)
    
    def display(self):
        # The base rect
        pygame.draw.rect(globals.Screen, self.col, self.rect)
        # The concentric squares
        for square in self.actualpoints:
            pygame.draw.lines(globals.Screen, self.pointcol, True, square, 5)
        # The four linking lines
        pygame.draw.line(globals.Screen, self.pointcol, self.actualpoints[0][1], self.actualpoints[2][1], 5)
        pygame.draw.line(globals.Screen, self.pointcol, self.actualpoints[0][5], self.actualpoints[2][5], 5)
        pygame.draw.line(globals.Screen, self.pointcol, self.actualpoints[0][7], self.actualpoints[2][7], 5)
        pygame.draw.line(globals.Screen, self.pointcol, self.actualpoints[0][3], self.actualpoints[2][3], 5)
        for i in range(len(self.contents)):
            for j in range(len(self.contents[i])):
                if self.contents[i][j] == 1:
                    pygame.draw.circle(globals.Screen, (255, 255, 255), self.actualpoints[i][j], 15)
                if self.contents[i][j] == 2:
                    pygame.draw.circle(globals.Screen, (0, 0, 0), self.actualpoints[i][j], 15)