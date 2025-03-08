# Subroutine to wait for a space to be selected
import globals

def select():
    clicked = False
    released = False
    while not clicked or not released:
        pos = globals.GameBoard.display()
        globals.pygame.display.update()
        for event in globals.pygame.event.get():
            if event.type == globals.pygame.QUIT:
                globals.game = False
                clicked = True
                released = True
            if event.type == globals.pygame.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == globals.pygame.MOUSEBUTTONUP and clicked and pos != None:
                if (globals.GameBoard.contents[pos[0]][pos[1]] == 0 and not globals.remove) or (globals.remove and globals.GameBoard.contents[pos[0]][pos[1]] != globals.turn and not globals.GameBoard.check(pos) and globals.GameBoard.contents[pos[0]][pos[1]] != 0) or (globals.selected == None and globals.GameBoard.contents[pos[0]][pos[1]] == globals.turn and globals.Unplayed[globals.turn - 1] == 0 and not globals.remove) or (globals.selected == pos):
                    if globals.remove:
                        print(globals.turn, globals.selected)
                        globals.GameBoard.contents[pos[0]][pos[1]] = 0
                        globals.Taken[globals.turn - 1] += 1
                        globals.remove = False
                        pos = None
                        released = True
                    elif globals.Unplayed[globals.turn - 1] > 0:
                        globals.GameBoard.contents[pos[0]][pos[1]] = globals.turn
                        globals.Unplayed[globals.turn - 1] -= 1
                        released = True
                    elif globals.selected == None:
                        if globals.GameBoard.contents[pos[0]][pos[1]] == globals.turn:
                            globals.selected = pos
                            released = True
                    elif globals.selected == pos:
                        globals.selected = None
                        released = True
                        if globals.turn == 1: globals.turn = 2
                        else: globals.turn = 1
                    elif (globals.selected[0] == pos[0] and (pos[1] == globals.selected[1] + 1 or pos[1] == globals.selected[1] - 1 or max(globals.selected[1], pos[1]), min(globals.selected[1], pos[1]) == (7, 0))) or (pos[1] % 2 == 1 and globals.selected[1] == pos[1]) or (globals.Lost[globals.turn - 1] == 6):
                        globals.GameBoard.contents[pos[0]][pos[1]] = globals.turn
                        globals.GameBoard.contents[globals.selected[0]][globals.selected[1]] = 0
                        globals.selected = None
                        released = True
    return pos
                    