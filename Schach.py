'''

TODO übgültige Züge aussortieren (Regelwerk)
TODO Spielfeld schöner gestalten (pygame)

Noch nötig für 2P mode:
  Gewinnerlogik einbauen
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

valid_moves_list = []

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
        print("    a  b  c  d  e  f  g  h")
        print("   -------------------------")
        for i in range(len(gamefield)):
            print(8-i, end=" | ")
            for j in range(len(gamefield[i])):
                if gamefield[i][j] == "":
                    print(" ", end="  ")
                else:
                    print(gamefield[i][j], end="  ")
            print("|", 8-i, end="")
            print()
        print("   -------------------------")
        print("    a  b  c  d  e  f  g  h")

    elif current_player == "P2":
        print("    h  g  f  e  d  c  b  a")
        print("   -------------------------")
        for i in range(len(gamefield)):
            print(i + 1, end=" | ")
            for j in range(len(gamefield[i])):
                if gamefield[7-i][7-j] == "":
                    print(" ", end="  ")
                else:
                    print(gamefield[7-i][7-j], end="  ")
            print("|", i + 1, end="")
            print()
        print("   -------------------------")
        print("    h  g  f  e  d  c  b  a")

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