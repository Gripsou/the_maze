from labyrinthe import Labyrinthe

def creer_labyrinthe_depuis_chaine(chaine):
    """On converti notre chaine en objet labyrinthe"""
    laby = Labyrinthe("X", "O")
    laby.grille = chaine
    return laby

def init_game(cartes):
    """On génère un objet labyrinthe suivant le choix du joueur"""
    choix_partie = input("Sur quelle partie souhaitez vous jouer : ")
    try:
        choix_partie = int(choix_partie) - 1 #-1 pour decaller par rapport à l'index 0
        laby = creer_labyrinthe_depuis_chaine(cartes[choix_partie].chaine)
        if choix_partie < 0:
            raise ValueError("Veuillez entrer un nombre positif")
    while 
        print("Veuillez entrer une valeur numérique")
    except IndexError:
        print("Veuillez choisir une carte existante")
    except AttributeError:
        print("Veuillez entrer une carte existante")
    else:
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
        #On va checker la ligne correspondante soit la position_robor - largeur du tableau + 1 (pour le \n) * le nb de case que l'on veut monter
        while(i <= move_force):
            if listed_game[robot_position - largeur * i] == "O":
                return 1
            elif listed_game[robot_position - largeur * i] == "U":
                return 2
            elif listed_game[robot_position - largeur * i] == ".":
                return 3
            i += 1
    elif(user_input[0] == "S"):
        #Pareil que pour N sauf qu'on additionne à la largeur du tab pour regarder une case plus bas
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
        except ValueError:
            print("Vous n'avez pas entré un nombre en second argument")
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
        print("Déplacement impossible, vous heurtez un mur")
    else:
        ''' 
            On est sur l'arrivée ou sur une porte :
                Si arrivée :
                    On remplace le "U" par "X" et l'ancienne position du robot par " "
                    pattern : destination, robot = robot, " " 
                Si porte :
                    On remplace dans un premier temps par " " et on retiens -> is_a_door = 1
                    Au move suivant on replace le point grace à la position du robot
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
    print("\n")
    menu.upper()
    while(menu != 'Y' and menu != 'N'):
        menu = input("Please reply by tipping 'Y' or 'N'")
        menu.upper()
    
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
