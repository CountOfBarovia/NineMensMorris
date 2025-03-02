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
    
    # Subroutine to display the board
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
        # Draw the counters
        for i in range(len(self.contents)):
            for j in range(len(self.contents[i])):
                if self.contents[i][j] == 1:
                    pygame.draw.circle(globals.Screen, (255, 248, 220), self.actualpoints[i][j], 15)
                if self.contents[i][j] == 2:
                    pygame.draw.circle(globals.Screen, (77, 55, 55), self.actualpoints[i][j], 15)
    
    # Subroutine to check for any rows of three after a token is moved
    def check(self, moved: tuple[int]) -> bool:
            if moved[1] == 0: return False
            if moved[1] % 2 != 0:
                if self.contents[0][moved[1]] == self.contents[1][moved[1]] and self.contents[0][moved[1]] == self.contents[2][moved[1]]:
                    return True
                if moved[1] != 7:
                    if self.contents[moved[0]][moved[1] - 1] == self.contents[moved[0]][moved[1]] and self.contents[moved[0]][moved[1]] == self.contents[moved[0]][moved[1] + 1]:
                        return True
                else:
                    if self.contents[moved[0]][moved[1] - 1] == self.contents[moved[0]][moved[1]] and self.contents[moved[0]][moved[1]] == self.contents[moved[0]][0]:
                        return True
            else:
                if moved[1] == 0:
                    if (self.contents[moved[0]][6] == self.contents[moved[0]][moved[1]] and self.contents[moved[0]][7] == self.contents[moved[0]][moved[1]]) or (self.contents[moved[0]][moved[1] + 2] == self.contents[moved[0]][moved[1]] and self.contents[moved[0]][moved[1] + 1] == self.contents[moved[0]][moved[1]]):
                        return True
                if moved[1] == 6:
                    if (self.contents[moved[0]][moved[1] - 2] == self.contents[moved[0]][moved[1]] and self.contents[moved[0]][moved[1] - 1] == self.contents[moved[0]][moved[1]]) or (self.contents[moved[0]][0] == self.contents[moved[0]][0] and self.contents[moved[0]][moved[1] + 1] == self.contents[moved[0]][moved[1]]):
                        return True
                else:
                    if (self.contents[moved[0]][moved[1] - 2] == self.contents[moved[0]][moved[1]] and self.contents[moved[0]][moved[1] - 1] == self.contents[moved[0]][moved[1]]) or (self.contents[moved[0]][moved[1] + 2] == self.contents[moved[0]][moved[1]] and self.contents[moved[0]][moved[1] + 1] == self.contents[moved[0]][moved[1]]):
                        return True
            return False