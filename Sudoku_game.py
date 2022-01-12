def pre_board(level):
    # input: level of the board
    # output: board(9X9)
    if level == 2:
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

    ########## explaination of the interface ##########   
    print(    
        "In order to start, please fill the clues which has been given to you in the following format:\n\n"
        "(BOX, CELL in box, VALUE of the clue)\n\n"
        "Use this illustration:\n"
        "\t -------------\n \
        | 1 | 2 | 3 |\n \
        -------------\n \
        | 4 | 5 | 6 |\n \
        -------------\n \
        | 7 | 8 | 9 |\n \
        -------------")
    
    return(board)

def change_board(board):
    # input: board(9X9)
    # output: changed board(9X9)

    ########## ask the player to enter the board ##########  
    (box, cell, value) = input('Fill:   #BOX --space-- #CELL --space-- #VALUE --enter--  ').split()
    board[int(box)-1][int(cell)-1] = int(value)
    print("Contiue to add your clues. When you finish, please fill: - - -")
    while box != '-':
        (box, cell, value) = input('Fill:   #BOX --space-- #CELL --space-- #VALUE --enter--  ').split()
        if box == '-':
            break
        board[int(box)-1][int(cell)-1] = int(value)
    
    return(board)
    
def visual(board):
    # input: board(9X9)
    # output: non

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
# def mistake_inf(board):

# def draft():
    
if __name__ == "__main__":
    print(
        "\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" 
        "\t\t\t\tWelcome to the Sudoku play!\n" 
        "\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")    
    choose = input(print("Do you want to choose a pre board table? y = Yes, n = No")) 
    if choose == 'y': 
        level = input(print("Choose a level: 1 = easy / 2 = hard"))
        board = pre_board(level)
        visual(board) 
    else:
        board = create_board()
        visual(board)

    change = input(print("Do you want to change the board"))




         
    board = create_board()
    visual(board)
    mis, mis_loc = valid(board)
    print(mis, mis_loc)
    #draft()