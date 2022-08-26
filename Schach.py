'''

TODO Rulebook
    TODO Knight, Queen, King

'''

figures_list_p1 = [
    ["b", 0, 6], ["b", 1, 6], ["b", 2, 6], ["b", 3, 6], ["b", 4, 6], ["b", 5, 6], ["b", 6, 6], ["b", 7, 6],
    ["t", 0, 7], ["s", 1, 7], ["l", 2, 7], ["d", 3, 7], ["k", 4, 7], ["l", 5, 7], ["s", 6, 7], ["t", 7, 7],
]

figures_list_p2 = [
    ["B", 0, 1], ["B", 1, 1], ["B", 2, 1], ["B", 3, 1], ["B", 4, 1], ["B", 5, 1], ["B", 6, 1], ["B", 7, 1],
    ["T", 0, 0], ["S", 1, 0], ["L", 2, 0], ["K", 3, 0], ["D", 4, 0], ["L", 5, 0], ["S", 6, 0], ["T", 7, 0],
]

punished_figures_list_p1 = []
punished_figures_list_p2 = []

valid_moves_list_p1 = []
valid_moves_list_p2 = []

# Colors
BG_BLACK = "\033[40m"
FG_WHITE = "\033[37m"

BG_WHITE = "\033[47m"
FG_BLACK = "\033[30m"

gamefield = [
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
]

def update_gamefield():
    gamefield = [
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
    ]

    for i in range(len(figures_list_p1)):
        gamefield[figures_list_p1[i][2]][figures_list_p1[i][1]] = figures_list_p1[i][0]

    for i in range(len(figures_list_p2)):
        gamefield[figures_list_p2[i][2]][figures_list_p2[i][1]] = figures_list_p2[i][0]
    
    return gamefield

def print_gamefield(current_player):
    if current_player == "P1":
        backgroundcolor = "WHITE"

        print("        a    b    c    d    e    f    g    h  ")
        print("    ---------------------------------------------")
        for i in range(len(gamefield)):
            print(BG_BLACK, FG_WHITE, 8-i, end=" | ")

            for j in range(len(gamefield[i])):
                if backgroundcolor == "WHITE":
                    print(BG_WHITE, FG_BLACK, end="") # Background = WHITE
                    backgroundcolor = "BLACK"
                else:
                    print(BG_BLACK, FG_WHITE, end="") # Background = BLACK
                    backgroundcolor = "WHITE"
                if gamefield[i][j] == "":
                    print("  ", end="  ")
                else:
                    print("", gamefield[i][j], end="  ")
                    
            if backgroundcolor == "WHITE":
                backgroundcolor = "BLACK"
            else:
                backgroundcolor = "WHITE"

            print(BG_BLACK, FG_WHITE, "|", 8-i, end="")
            print()

        print("    ---------------------------------------------")
        print("        a    b    c    d    e    f    g    h  ")

    elif current_player == "P2":
        backgroundcolor = "WHITE"

        print("        h    g    f    e    d    c    b    a  ")
        print("    ---------------------------------------------")

        for i in range(len(gamefield)):
            print(BG_BLACK, FG_WHITE, i + 1, end=" | ")

            for j in range(len(gamefield[i])):
                if backgroundcolor == "WHITE":
                    print(BG_WHITE, FG_BLACK, end="") # Background = WHITE
                    backgroundcolor = "BLACK"
                else:
                    print(BG_BLACK, FG_WHITE, end="") # Background = BLACK
                    backgroundcolor = "WHITE"

                if gamefield[7-i][7-j] == "":
                    print("  ", end="  ")
                else:
                    print("", gamefield[7-i][7-j], end="  ")

            if backgroundcolor == "WHITE":
                backgroundcolor = "BLACK"
            else:
                backgroundcolor = "WHITE"

            print(BG_BLACK, FG_WHITE, "|", i + 1, end="")
            print()

        print("    ---------------------------------------------")
        print("        h    g    f    e    d    c    b    a  ")

# Nicht fertig
# Kompatibel für cp machen
def check_input(user_input, current_player):
    length = len(user_input)

    # For user 1 - 8 for python 0 - 7
    source_x = int(user_input[0]) -1
    source_y = 8 - int(user_input[1])

    destination_x = int(user_input[2]) -1
    destination_y = 8 - int(user_input[3])

    # Invalid values
    if length > 3 or length < 0:
        return False

    return True

def follow_user_input(user_input, current_player):
    # For user 1 - 8 for python 0 - 7
    source_x = int(user_input[0]) -1
    source_y = 8 - int(user_input[1])

    destination_x = int(user_input[2]) -1
    destination_y = 8 - int(user_input[3])

    print(source_x, source_y, destination_x, destination_y)

    if current_player == "P1":
        for i in range(len(figures_list_p1)):
            if figures_list_p1[i][1] == source_x and figures_list_p1[i][2] == source_y:
                figures_list_p1[i][1] = destination_x
                figures_list_p1[i][2] = destination_y

                print(figures_list_p2)
                for i in range(len(figures_list_p2)):
                    if figures_list_p2[i][1] == destination_x and figures_list_p2[i][2] == destination_y:
                        punished_figures_list_p2.append(figures_list_p2[i])
                        del figures_list_p2[i]
                        print(punished_figures_list_p2)
                        break
                break
    elif current_player == "P2":
        for i in range(len(figures_list_p2)):
            if figures_list_p2[i][1] == source_x and figures_list_p2[i][2] == source_y:
                figures_list_p2[i][1] = destination_x
                figures_list_p2[i][2] = destination_y

                for i in range(len(figures_list_p1)):
                    if figures_list_p1[i][1] == destination_x and figures_list_p1[i][2] == destination_y:
                        punished_figures_list_p1.append(figures_list_p1[i])
                        del figures_list_p1[i]
                        print(punished_figures_list_p1)
                        break
                break

def letter_to_num(user_input):
    new_num = ""

    for i in range(len(user_input)):
        user_input = user_input.lower()

        if not user_input[i].isnumeric():
            num = ord(user_input[i]) - 96
            new_num += str(num)
        else:
            new_num += user_input[i]

    return new_num

def get_valid_moves(current_player):
    if current_player == "P1":
        for i in range(len(figures_list_p1)):
            if figures_list_p1[i][0] == "b":
                pass
            elif figures_list_p1[i][0] == "t":
                pass
            elif figures_list_p1[i][0] == "s":
                pass
            elif figures_list_p1[i][0] == "l":
                pass
            elif figures_list_p1[i][0] == "d":
                pass
            elif figures_list_p1[i][0] == "k":
                pass
    elif current_player == "P2":
        for i in range(len(figures_list_p2)):
            if figures_list_p2[i][0] == "b":
                pass
            elif figures_list_p2[i][0] == "t":
                pass
            elif figures_list_p2[i][0] == "s":
                pass
            elif figures_list_p2[i][0] == "l":
                pass
            elif figures_list_p2[i][0] == "d":
                pass
            elif figures_list_p2[i][0] == "k":
                pass

# Funktions which return valid moves of the figures
def pawn(x, y, player):
    if player == "P1":
        if gamefield[x][y+1] == "":
            valid_moves_list_p1.append([x, y+1])
    
        if gamefield[x][y+2] == "":
            valid_moves_list_p1.append([x, y+2])

        for i in range(len(figures_list_p2)):
            if x+1 == figures_list_p2[i][1] and y+1 == figures_list_p2[i][2]:
                if figures_list_p2[i][0] == "K":
                    print("SCHACH")
                valid_moves_list_p1.append([x+1, y+1])
            elif x-1 == figures_list_p2[i][1] and y+1 == figures_list_p2[i][2]:
                if figures_list_p2[i][0] == "K":
                    print("SCHACH")
                valid_moves_list_p1.append([x-1, y+1])
    elif player == "P2":
        if gamefield[x][y+1] == "":
            valid_moves_list_p2.append([x, y+1])
    
        if gamefield[x][y+2] == "":
            valid_moves_list_p2.append([x, y+2])

        for i in range(len(figures_list_p1)):
            if x+1 == figures_list_p1[i][1] and y+1 == figures_list_p1[i][2]:
                if figures_list_p1[i][0] == "k":
                    print("SCHACH")

                valid_moves_list_p2.append([x+1, y+1])
            elif x-1 == figures_list_p1[i][1] and y+1 == figures_list_p1[i][2]:
                if figures_list_p1[i][0] == "k":
                    print("SCHACH")
                    
                valid_moves_list_p2.append([x-1, y+1])

def bishop(x, y, player):
    if player == "P1":
        for i in range(len(gamefield)-x):
            if gamefield[x+i][y+i] == "":
                valid_moves_list_p1.append([x+i, y+i])
                break
            
            for j in range(len(figures_list_p1)):
                if x+i == figures_list_p1[i][1] and y+i == figures_list_p1[i][2]:
                    break

            for j in range(len(figures_list_p2)):
                if x+i == figures_list_p2[i][1] and y+i == figures_list_p2[i][2]:
                    if figures_list_p2[i][0] == "K":
                        print("SCHACH")

                    valid_moves_list_p1.append([x+i, y+i])
                    break

        # Same in the other direction
        for i in range(x):
            if gamefield[x-i][y-i] == "":
                valid_moves_list_p1.append([x-i, y-i])
                break
            
            for j in range(len(figures_list_p1)):
                if x-i == figures_list_p1[i][1] and y-i == figures_list_p1[i][2]:
                    break

            for j in range(len(figures_list_p2)):
                if x-i == figures_list_p2[i][1] and y-i == figures_list_p2[i][2]:
                    if figures_list_p2[i][0] == "K":
                        print("SCHACH")

                    valid_moves_list_p1.append([x-i, y-i])
                    break

    elif player == "P2":
        for i in range(len(gamefield)-x):
            if gamefield[x+i][y+i] == "":
                valid_moves_list_p2.append([x+i, y+i])
                break
            
            for j in range(len(figures_list_p2)):
                if x+i == figures_list_p2[i][1] and y+i == figures_list_p2[i][2]:
                    break

            for j in range(len(figures_list_p1)):
                if x+i == figures_list_p1[i][1] and y+i == figures_list_p1[i][2]:
                    if figures_list_p1[i][0] == "k":
                        print("SCHACH")

                    valid_moves_list_p2.append([x+i, y+i])
                    break 

        # Same in the other direction
        for i in range(len(gamefield)-x):
            if gamefield[x-i][y-i] == "":
                valid_moves_list_p2.append([x-i, y-i])
                break
            
            for j in range(len(figures_list_p2)):
                if x-i == figures_list_p2[i][1] and y-i == figures_list_p2[i][2]:
                    break

            for j in range(len(figures_list_p1)):
                if x-i == figures_list_p1[i][1] and y-i == figures_list_p1[i][2]:
                    if figures_list_p1[i][0] == "k":
                        print("SCHACH")

                    valid_moves_list_p2.append([x-i, y-i])
                    break 

def rook(x, y, player):
    if player == "P1":
        # X-direction
        for i in range(len(gamefield)-x):
            if gamefield[x+i][y] == "":
                valid_moves_list_p1.append([x+i, y])
                break
            elif x+i == figures_list_p2[i][1] and y == figures_list_p2[i][2]:
                valid_moves_list_p1.append([x+i, y])

                if figures_list_p2[i][0] == "k":
                    print("SCHACH")
                break
            elif x+i == figures_list_p1[i][1] and y == figures_list_p1[i][2]:
                continue

        for i in range(x):
            if gamefield[x-i][y] == "":
                valid_moves_list_p1.append([x-i, y])
                break
            elif x-i == figures_list_p2[i][1] and y == figures_list_p2[i][2]:
                valid_moves_list_p1.append([x-i, y])

                if figures_list_p2[i][0] == "k":
                    print("SCHACH")
                break
            elif x-i == figures_list_p1[i][1] and y == figures_list_p1[i][2]:
                continue
        
        # Y-direction
        for i in range(len(gamefield)-y):
            if gamefield[x][y+i] == "":
                valid_moves_list_p1.append([x, y+i])
                break
            elif x == figures_list_p2[i][1] and y+i == figures_list_p2[i][2]:
                valid_moves_list_p1.append([x, y+i])

                if figures_list_p2[i][0] == "k":
                    print("SCHACH")
                break
            elif x == figures_list_p1[i][1] and y+i == figures_list_p1[i][2]:
                continue

        for i in range(y):
            if gamefield[x][y-i] == "":
                valid_moves_list_p1.append([x, y-i])
                break
            elif x == figures_list_p2[i][1] and y-i == figures_list_p2[i][2]:
                valid_moves_list_p1.append([x, y-i])

                if figures_list_p2[i][0] == "k":
                    print("SCHACH")
                break
            elif x == figures_list_p1[i][1] and y-i == figures_list_p1[i][2]:
                continue

    elif player == "P2":
        # X-direction
        for i in range(len(gamefield)-x):
            if gamefield[x+i][y] == "":
                valid_moves_list_p2.append([x+i, y])
                break
            elif x+i == figures_list_p1[i][1] and y == figures_list_p1[i][2]:
                valid_moves_list_p2.append([x+i, y])

                if figures_list_p1[i][0] == "K":
                    print("SCHACH")
                break
            elif x+i == figures_list_p2[i][1] and y == figures_list_p2[i][2]:
                continue

        for i in range(x):
            if gamefield[x-i][y] == "":
                valid_moves_list_p2.append([x-i, y])
                break
            elif x-i == figures_list_p1[i][1] and y == figures_list_p1[i][2]:
                valid_moves_list_p2.append([x-i, y])

                if figures_list_p1[i][0] == "K":
                    print("SCHACH")
                break
            elif x-i == figures_list_p2[i][1] and y == figures_list_p2[i][2]:
                continue
        
        # Y-direction
        for i in range(len(gamefield)-y):
            if gamefield[x][y+i] == "":
                valid_moves_list_p2.append([x, y+i])
                break
            elif x == figures_list_p1[i][1] and y+i == figures_list_p1[i][2]:
                valid_moves_list_p2.append([x, y+i])

                if figures_list_p1[i][0] == "K":
                    print("SCHACH")
                break
            elif x == figures_list_p2[i][1] and y+i == figures_list_p2[i][2]:
                continue

        for i in range(y):
            if gamefield[x][y-i] == "":
                valid_moves_list_p2.append([x, y-i])
                break
            elif x == figures_list_p1[i][1] and y-i == figures_list_p1[i][2]:
                valid_moves_list_p2.append([x, y-i])

                if figures_list_p1[i][0] == "K":
                    print("SCHACH")
                break
            elif x == figures_list_p2[i][1] and y-i == figures_list_p2[i][2]:
                continue

def knight(x, y, player):
    if player == "P1":
        # X-direction
        if gamefield[x+2][y+1] == "":
            pass
        
        if gamefield[x+2][y-1] == "":
            pass

        if gamefield[x-2][y+1] == "":
            pass

        if gamefield[x+2][y-1] == "":
            pass

        # Y-direction
        if gamefield[x+1][y+2] == "":
            pass

        if gamefield[x-1][y+2] == "":
            pass

        if gamefield[x+1][y-2] == "":
            pass

        if gamefield[x-1][y-2] == "":
            pass
    elif player == "P2":
        pass   

run = True
mode = "pp" # pp = Player vs Player | pc = Player vs Computer | cc = Computer vs Computer
current_player = "P1"
user_input = ""

# Nicht fertig
while run:
    gamefield = update_gamefield()

    print_gamefield(current_player)
    print()
    print("Input im Format 1234 mit 12=Quelle_x_y 34=Ziel_x_y")

    if current_player == "P1":
        print("Spieler 1 ist dran!")

        user_input = input("Eingabe: ")
        user_input = letter_to_num(user_input)

        follow_user_input(user_input, current_player)

        current_player = "P2"

    elif current_player == "P2":
        print("Spieler 2 ist dran!")

        user_input = input("Eingabe: ")
        user_input = letter_to_num(user_input)

        follow_user_input(user_input, current_player)
        
        current_player = "P1"

'''
a  b  c  d  e  f  g  h  = Schach
1  2  3  4  5  6  7  8  = user input
0  1  2  3  4  5  6  7  = j Python
T  S  L  D  K  L  S  T   0 8
B  B  B  B  B  B  B  B   1 7
                         2 6
                         3 5
                         4 4
                         5 3
b  b  b  b  b  b  b  b   6 2
t  s  l  d  k  l  s  t   7 1 --> user input
                         |-> i Python
'''