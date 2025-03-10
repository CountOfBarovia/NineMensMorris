# All global variables
import pygame, board

# The display setting
ScreenW = 500
ScreenH = 500
Screen = pygame.display.set_mode((ScreenW, ScreenH))
WhiteHalf = pygame.rect.Rect(0, 0, ScreenW / 2, ScreenH)
BlackHalf = pygame.rect.Rect(ScreenW / 2, 0, ScreenW / 2, ScreenH)
mousecoll = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))

# The run variables
turn = 2
game = True
selected = None
remove = False
pos = None

# The board
GameBoard = board.board()

# The player tokens
Unplayed = [9, 9]
Taken = [0, 0]
Lost = [0, 0]