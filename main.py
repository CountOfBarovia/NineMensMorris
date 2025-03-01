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
    # Update the screen
    pygame.display.update()
    # Make it possible to close the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            globals.game = False

pygame.quit()