from labyrinthe import Labyrinthe

def creer_labyrinthe_depuis_chaine(chaine):
    """We convert the str in labyrithe object"""
    laby = Labyrinthe("X", "O")
    laby.grille = chaine
    return laby

def init_game(cartes):
    """We generate the labyrithe game from the user choice"""
    choix_partie = input("Which map do you want to play ? ")
    while True:
        try:
            choix_partie = int(choix_partie) - 1 #-1 pour decaller par rapport à l'index 0
            laby = creer_labyrinthe_depuis_chaine(cartes[choix_partie].chaine)
            break
        except :
            choix_partie = input("Please type the number of an existing map : ")
        
    return laby

def check_wall(listed_game, robot_position, move_force, user_input, largeur):
    i = 1
    if(user_input[0] == "O"):
        while(i <= move_force):
            if listed_game[robot_position - i] == "O":
                return 1
            elif listed_game[robot_position - i] == "U":
                return 2
            elif listed_game[robot_position - i] == ".":
                return 3
            i += 1
    elif(user_input[0] == "E"):
        while(i <= move_force):
            if listed_game[robot_position + i] == "O":
                return 1
            if listed_game[robot_position + i] == "U":
                return 2
            if listed_game[robot_position + i] == ".":
                return 3
            i += 1
    elif(user_input[0] == "N"):
        """We check the related line who is position_robot - width + 1 (for the \\n) multiply by the number of case to climb"""
        while(i <= move_force):
            if listed_game[robot_position - largeur * i] == "O":
                return 1
            elif listed_game[robot_position - largeur * i] == "U":
                return 2
            elif listed_game[robot_position - largeur * i] == ".":
                return 3
            i += 1
    elif(user_input[0] == "S"):
        while(i <= move_force):
            if listed_game[robot_position + largeur * i] == "O":
                return 1
            elif listed_game[robot_position + largeur * i] == "U":
                return 2
            elif listed_game[robot_position + largeur * i] == ".":
                return 3
            i += 1
    return 0

def move(user_input, listed_game, largeur):
    
    listed_input = list(user_input)
    
    if len(listed_input) == 2 :
        try:
            move_force = int(user_input[1])
        except :
            print("Please type a valid number as second argument")
    else :
        move_force = 1

    robot_position = 0

    while(listed_game[robot_position] != 'X'):
        robot_position += 1

    is_ok_move = check_wall(listed_game, robot_position, move_force, user_input, largeur)

    if is_ok_move == 3 :
            is_a_door = 1
    else :
        is_a_door = 0

    if is_ok_move == 1:
        print("Impossible, you hurt a wall")
    else:
        ''' 
            We are on a special case:
                If arrival "U" :
                    We replace "U" by "X" and the old position by " "
                    pattern : destination, robot = robot, " "
                If door "." :
                    In a first time we replace by " " and we assign -> is_a_door = 1
                    On the next move suivant we replace "." at the old robot position
        '''
        
        if user_input[0] == "O":
            if is_a_door == 1 :
                listed_game[robot_position - move_force], listed_game[robot_position] = listed_game[robot_position], '.'
                is_a_door == 0
            else:
                listed_game[robot_position - move_force], listed_game[robot_position] = listed_game[robot_position], ' '
        elif user_input[0] == "E":
            if is_a_door == 1 :
                listed_game[robot_position + move_force], listed_game[robot_position] = listed_game[robot_position], '.'
                is_a_door == 0
            else :
                listed_game[robot_position + move_force], listed_game[robot_position] = listed_game[robot_position], ' '
        elif user_input[0] == "N":
            if is_a_door == 1:
                listed_game[robot_position - (largeur * move_force)], listed_game[robot_position] = listed_game[robot_position], '.'
                is_a_door == 0
            else :
                listed_game[robot_position - (largeur * move_force)], listed_game[robot_position] = listed_game[robot_position], ' '
        elif user_input[0] == "S":
            if is_a_door == 1:
                listed_game[robot_position + (largeur * move_force)], listed_game[robot_position] = listed_game[robot_position], '.'
                is_a_door == 0
            else :
                listed_game[robot_position + (largeur * move_force)], listed_game[robot_position] = listed_game[robot_position], ' '

    robot_position = 0
    i = 0
    while(listed_game[i] != 'X'):
        i += 1
    robot_position = i

    return listed_game

def affichage():
    '''Print the beggining of the game'''

    print("\t****************************************************")
    print("\t****************//////////+\\\\\\\\\\\\\\\\ ****************")
    print("\t****************|                  |****************")
    print("\t****************|     The Maze     |****************")
    print("\t****************|                  |****************")
    print("\t****************+\\\\\\\\\\\\\\\\+///////// ****************")
    print("\t****************************************************")

    menu = input("Welcome to the Maze, do you want to know the rules ? (Y) / (N) : ")
    menu = menu.upper()
    print("\n")
    
    while(menu != 'Y' and menu != 'N'):
        menu = input("Please reply by tipping 'Y' or 'N'")
        menu = menu.upper()
    
    if menu == 'Y':
            print("You are a little robot 'X' and your goal is to reach the end of the maze symbolized by the caracter 'U'.")
            print("You can't break through the wall 'O' but you can pass doors '.' !")
            print("To move across the maze : ")
            print("N > North")
            print("S > South")
            print("E > East")
            print("O > Ouest (sorry about the non french players)")

            print("Q > Quit the game")
            print()
            print('Good game ! ')
            print()
