# All global variables
import pygame, board

# The display setting
ScreenW = 500
ScreenH = 500
Screen = pygame.display.set_mode((ScreenW, ScreenH))
WhiteHalf = pygame.rect.Rect(0, 0, ScreenW / 2, ScreenH)
BlackHalf = pygame.rect.Rect(ScreenW / 2, 0, ScreenW / 2, ScreenH)

# The run variables
turn = 0
game = True

# The board
GameBoard = board.board()