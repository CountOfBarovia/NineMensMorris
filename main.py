# Nine Men's Morris Digitalisation

# Initialising pygame
import pygame
pygame.init()

# Load modules
import globals, controls

while globals.game:
    # Update the mouse
    globals.mousecoll.topleft = pygame.mouse.get_pos()
    # Set the background
    pygame.draw.rect(globals.Screen, (255, 255, 255), globals.WhiteHalf)
    pygame.draw.rect(globals.Screen, (0, 0, 0), globals.BlackHalf)
    # Check if a row of three has just been made
    if globals.pos != None: globals.remove = globals.GameBoard.check(globals.pos)
    if not globals.remove:
            if globals.turn == 1: globals.turn = 2
            else: globals.turn = 1
    # Draw the tokens
    # The white side
    total = globals.Unplayed[0] + globals.Taken[0]
    for i in range(globals.Unplayed[0]):
        pygame.draw.circle(globals.Screen, (255, 248, 220), (25, (globals.ScreenH - (total - 1) * 50) / 2 + i * 50), 15)
    for i in range(globals.Taken[0]):
        pygame.draw.circle(globals.Screen, (77, 55, 55), (25, (globals.ScreenH - (total - 1) * 50) / 2 + (i + globals.Unplayed[0]) * 50), 15)
    # The black side
    total = globals.Unplayed[1] + globals.Taken[1]
    for i in range(globals.Unplayed[1]):
        pygame.draw.circle(globals.Screen, (77, 55, 55), (globals.ScreenW - 25, (globals.ScreenH - (total - 1) * 50) / 2 + i * 50), 15)
    for i in range(globals.Taken[1]):
        pygame.draw.circle(globals.Screen, (255, 248, 220), (globals.ScreenW - 25, (globals.ScreenH - (total - 1) * 50) / 2 + (i + globals.Unplayed[1]) * 50), 15)
    # Update the screen
    globals.GameBoard.display()
    pygame.display.update()
    # Make it possible to close the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            globals.game = False
    # Make a decision
    globals.pos = controls.select()

pygame.quit()