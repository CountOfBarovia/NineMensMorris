# Nine Men's Morris Digitalisation

# Initialising pygame
import pygame
pygame.init()

# Load modules
import globals

while globals.game:
    # Set the background
    pygame.draw.rect(globals.Screen, (255, 255, 255), globals.WhiteHalf)
    pygame.draw.rect(globals.Screen, (0, 0, 0), globals.BlackHalf)
    # Draw the tokens
    # The white side
    total = globals.WhiteUnplayed + globals.WhiteTaken
    for i in range(globals.WhiteUnplayed):
        pygame.draw.circle(globals.Screen, (255, 248, 220), (25, (globals.ScreenH - (total - 1) * 50) / 2 + i * 50), 15)
    for i in range(globals.WhiteTaken):
        pygame.draw.circle(globals.Screen, (77, 55, 55), (25, (globals.ScreenH - (total - 1) * 50) / 2 + (i + globals.WhiteUnplayed) * 50), 15)
    # The black side
    total = globals.BlackUnplayed + globals.BlackTaken
    for i in range(globals.BlackUnplayed):
        pygame.draw.circle(globals.Screen, (77, 55, 55), (globals.ScreenW - 25, (globals.ScreenH - (total - 1) * 50) / 2 + i * 50), 15)
    for i in range(globals.BlackTaken):
        pygame.draw.circle(globals.Screen, (255, 248, 220), (globals.ScreenW - 25, (globals.ScreenH - (total - 1) * 50) / 2 + (i + globals.BlackUnplayed) * 50), 15)
    globals.GameBoard.display()
    # Update the screen
    pygame.display.update()
    # Make it possible to close the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            globals.game = False

pygame.quit()