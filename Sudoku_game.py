def pre_board(level):
    # input: level of the board
    # output: board(9X9)
    if level == '2':
        board = [['.',8 ,'.','.','.','.','.','.','.'],\
        ['.',2 ,'.',1 ,'.','.','.','.','.'],\
        [5 ,6 ,'.','.','.',7 ,'.','.','.'],\
        ['.',5 ,'.','.','.',7 ,'.',9 ,'.'],\
        ['.',9 ,'.',8 ,'.','.','.',1 ,'.'],\
        [4 ,'.',8 ,'.','.',3 ,'.',5 ,'.'],\
        [2 ,'.',4 ,'.',6 ,'.','.','.','.'],\
        ['.','.','.','.',8 ,5 ,2 ,'.','.'],\
        [8 ,'.','.','.','.','.',1 ,'.','.']]
    
    else:
        board = [[9 ,'.','.',4 ,3 ,7,'.','.',5 ],\
        [3 ,'.','.',8 ,'.','.','.',2 ,'.'],\
        ['.',7 ,1 ,2 ,5 ,'.','.',4 ,9 ],\
        ['.',5 ,8 ,7 ,'.','.',2 ,9 ,'.'],\
        [4 ,'.',9 ,1 ,'.','.','.',3 ,'.'],\
        ['.',3 ,'.','.' ,9 ,8,'.','.',4],\
        ['.',8 ,'.',3 ,'.',4 ,1 ,'.','.'],\
        ['.',1 ,3 ,6 ,8 ,7 ,2 ,5 ,'.'],\
        ['.','.','.','.','.','.','.','.','.']]

    return (board)

def create_board():
    # input: False + None or True + pre_board
    # output: board(9X9)
    
    ########## create a board ##########    
    board = [['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.']]
 
    return(board)

def exp_fill():
    # input: None
    # output: print
    ########## explaination of the interface ##########   
    print(    
        "Fill the board in the following format:\n\n"
        "(BOX, CELL in box, VALUE of the clue)\n\n"
        "Use this illustration:\n"
        "\t -------------\n \
        | 1 | 2 | 3 |\n \
        -------------\n \
        | 4 | 5 | 6 |\n \
        -------------\n \
        | 7 | 8 | 9 |\n \
        -------------")

def change_board(board):
    # input: board(9X9)
    # output: changed board(9X9)
    
    ########## ask the player to enter the board ##########  
    ent = input('Fill:   #BOX --space-- #CELL --space-- #VALUE  ')
    while len(ent) != 0:
        if len(ent.split()) == 3:
            st = ent.split()
            if all([i.isnumeric() for i in st]):
                if all([int(j)>0 and int(j)<10 for j in st[0:2]]):
                    (box, cell, value) = ent.split()
                    board[int(box)-1][int(cell)-1] = int(value)
                    print("Please fill again. When you finish, please press ENTER")
                    ent = input('Fill:   #BOX --space-- #CELL --space-- #VALUE  ')
                    continue    
        
        print("Error! Please fill again. When you finish, please press ENTER")
        ent = input('Fill:   #BOX --space-- #CELL --space-- #VALUE  ')
    
    return(board)
    
def visual(board):
    # input: board(9X9)
    # output: print
    print("\n")
    ########## visualization of the board ##########   
    for i in range (3):
        for j in range(3):
            for k in range(3):          
                for m in range(3):
                    print(str(board[3*i+k][3*j+m]) + " ", end="" )
                if k == 2:
                    print("") 
                else:
                    print(" | ", end="")
        if i == 2:
            print("")
        else:
            print("------------------------")
    
def valid(board):
    # input: board(9X9)
    # output: tuple(Logic, [(Box, Cell, Value), (Box, Cell, Value)])
    
    ########## check duplication in the column ##########
    for box in range(9):
        his = {}
        for c in range(9):
            if board[box][c] != '.':
                if board[box][c] in his.keys():
                    his[ board[box][c] ].append((box,c,board[box][c]))
                    return False, (his[ board[box][c] ]) 
                else:
                    his[ board[box][c] ] = [(box,c,board[box][c])]

    ########## check duplication in the row ##########            
    for i in range (3):
        for j in range(3):
            his = {}
            for k in range(3):          
                for m in range(3):
                    box = 3*i+k
                    c = 3*j+m
                    if board[box][c] != '.':
                        if board[box][c] in his.keys():
                            his[ board[box][c] ].append((box,c,board[box][c]))
                            return False, (his[ board[box][c] ]) 
                        else:
                            his[ board[box][c] ] = [(box,c,board[box][c])]

    ########## check duplication in the col ##########
    for i in range (3):
        for j in range(3):
            his = {}
            for k in range(3):          
                for m in range(3):
                    box = 3*k+i
                    c = 3*m+j
                    if board[box][c] != '.':
                        if board[box][c] in his.keys():
                            his[ board[box][c] ].append((box,c,board[box][c]))
                            return False, (his[ board[box][c] ]) 
                        else:
                            his[ board[box][c] ] = [(box,c,board[box][c])]
    return True, ()
    
if __name__ == "__main__":
    ############################## Initialization ###############################
    # Welcome:
    print(
        "\n\n\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" 
        "\t\tWelcome to the Sudoku play!\n" 
        "\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")    
    
    # Choose wether to use a pre board or create a new one:
    choose = input("Do you want to choose a pre board table? y = Yes , n = No  ")
    # Input check: 
    while choose not in "yn" or choose == '':
        choose = input("Please choose again: y = Yes , n = No  ")
    
    if choose == 'y': 
        # Choose the level of pre board:
        level = input("Choose a level: 1 = easy , 2 = hard  ")
        # Input check: 
        while level not in "12" or level == '':
            level = input("Please choose again:  1 = easy , 2 = hard  ")

        board = pre_board(level)
        visual(board) 
    else:
        # Create a new board:
        board = create_board()
        visual(board)
        print("In order to start, please fill the clues which has been given to you.")
        exp_fill()
        board = change_board(board)
        visual(board)

    # Change the board:
    change = input("Do you want to change the board? y = Yes , n = No  ")

    while change != 'n': 
        # Input check:
        while change not in "yn" or change == '':
            change = input("Please choose again: y = Yes , n = No  ")
        
        if change == 'y':    
            board = change_board(board)
            visual(board)
            change = input("Do you want to change the board? y = Yes , n = No  ")

    ############################## Start to play! ###############################
    print(       
        "\n\n\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" 
        "\t\tNow we are ready! Let's Play!\n" 
        "\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")  
    exp_fill()
    print("Whenever your fill is not valid, we let you know\n")
    exit = 'n'
    while exit == 'n':
        v, pos = valid(board)
        if not(v):
            pos1 = list(pos[0][0:2])
            pos2 = list(pos[1][0:2])
            for j in range(2):
                pos1[j] += 1
                pos2[j] += 1
            print("Error in positions: [box,cell]={} , [box,cell]={}".format(pos1, pos2))
        
        board = change_board(board)
        visual(board)
        exit = input("Do you want to exit? y = Yes , n = No  ")
        while exit not in "yn" or level == '':
            exit = input("Please choose again: y = Yes , n = No  ")

    
