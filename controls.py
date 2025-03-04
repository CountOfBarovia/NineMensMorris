# Subroutine to wait for a space to be selected
import globals

def select():
    clicked = False
    released = False
    while not clicked or not released:
        for event in globals.pygame.event.get():
            if event.type == globals.pygame.QUIT:
                globals.game = False
                clicked = True
                released = True
            if event.type == globals.pygame.MOUSEBUTTONDOWN:
                pos = globals.GameBoard.display()
                if globals.GameBoard.contents[pos[0]][pos[1]] == 0 or globals.remove:
                    if globals.remove:
                        globals.GameBoard.contents[pos[0]][pos[1]] = 0
                        globals.Taken[globals.turn - 1] += 1
                        globals.remove = False
                        pos = None
                        clicked = True
                    elif globals.Unplayed[globals.turn - 1] > 0:
                        globals.GameBoard.contents[pos[0]][pos[1]] = globals.turn
                        globals.Unplayed[globals.turn - 1] -= 1
                        clicked = True
                    elif globals.selected == None:
                        if globals.GameBoard.contents[pos[0]][pos[1]] == globals.turn:
                            globals.selected = pos
                            clicked = True
                    elif globals.selected == pos:
                        globals.selected = None
                        clicked = True
                    elif (globals.selected[0] == pos[0] and (pos[1] == globals.selected[1] + 1 or pos[1] == globals.selected[1] - 1 or max(globals.selected[1], pos[1]), min(globals.selected[1], pos[1]) == (7, 0))) or (pos[1] % 2 == 1 and globals.selected[1] == pos[1]):
                        globals.GameBoard.contents[pos[0]][pos[1]] = globals.turn
                        globals.GameBoard.contents[globals.selected[0]][globals.selected[1]] = 0
                        globals.selected = None
                        clicked = True
            if event.type == globals.pygame.MOUSEBUTTONUP and clicked:
                released = True
    return pos
                    