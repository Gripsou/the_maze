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
        if choix_partie < 0:
            raise ValueError("Veuillez entrer un nombre positif")
    except ValueError:
        print("Veuillez entrer une valeur numérique")
    except IndexError:
        print("Veuillez choisir une carte existante")
    else:
        laby = creer_labyrinthe_depuis_chaine(cartes[choix_partie].chaine)
        return laby

def check_wall(listed_game, robot_position, move_force, user_input):
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
            if listed_game[robot_position - 11 * i] == "O":
                return 1
            elif listed_game[robot_position - 11 * i] == "U":
                return 2
            elif listed_game[robot_position - 11 * i] == ".":
                return 3
            i += 1
    elif(user_input[0] == "S"):
        #Pareil que pour N sauf qu'on additionne à la largeur du tab pour regarder une case plus bas
        while(i <= move_force):
            if listed_game[robot_position + 11 * i] == "O":
                return 1
            elif listed_game[robot_position + 11 * i] == "U":
                return 2
            elif listed_game[robot_position + 11 * i] == ".":
                return 3
            i += 1
    return 0

def move(user_input, listed_game):
    
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

    is_ok_move = check_wall(listed_game, robot_position, move_force, user_input)

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
                listed_game[robot_position - (11 * move_force)], listed_game[robot_position] = listed_game[robot_position], '.'
                is_a_door == 0
            else :
                listed_game[robot_position - (11 * move_force)], listed_game[robot_position] = listed_game[robot_position], ' '
        elif user_input[0] == "S":
            if is_a_door == 1:
                listed_game[robot_position + (11 * move_force)], listed_game[robot_position] = listed_game[robot_position], '.'
                is_a_door == 0
            else :
                listed_game[robot_position + (11 * move_force)], listed_game[robot_position] = listed_game[robot_position], ' '

    robot_position = 0
    i = 0
    while(listed_game[i] != 'X'):
        i += 1
    robot_position = i

    return listed_game