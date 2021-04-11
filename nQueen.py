import random
import copy

#each object has the board state and the heuristic value of the board
class State:
    def __init__(self, state, heuristic):
        self.state = state
        self.heuristic = heuristic

array = [None] * 8

#initializes the board with a random configuration each time
def initialize():
    #board = copy.deepcopy(val)
    board = [
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8
    ]
    for x in range(8):
        position = random.randint(0, 7)
        board[position][x] = 'Q'

    return State(board, numAttacking(board))

#returns how many pairs of queens are attacking each other
def numAttacking(board):
    attacking = 0
    col = 0
    row = 0

    while(col <= 7):
        if(board[row][col] == 'Q'):
            attacking += up_right(board, row, col)
            attacking += right(board, row, col)
            attacking += down_right(board, row, col)         
            col += 1
            row = 0
        else:
            row += 1
    return attacking

#returns how many queens are in the line of attack to the up-right diagonal of a queen
def up_right(board, row, col):
    count = 0
    row -= 1
    col += 1 
    
    while(row >= 0 and col <= 7):
        if(board[row][col] == 'Q'):
            count += 1
        row -= 1
        col += 1
 
    return count

#returns how many queens are in the line of attack to the right  of a queen
def right(board, row, col):
    count = 0
    x = row
    y = col + 1 
    
    while(y <= 7):
        if(board[x][y] == 'Q'):
            count += 1
        y += 1
    
    return count

#returns how many queens are in the line of attack to the bottom-right diagonal of a queen
def down_right(board, row, col):
    count = 0
    x = row + 1
    y = col + 1
    
    while(x <= 7 and y <= 7):
        if(board[x][y] == 'Q'):
            count += 1 
        x += 1
        y += 1
 
    return count
 
#returns best position for the queen in the first column to move to
def moveFirst(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][0] = '_'
        board.state[x][0] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#returns best position for the queen in the second column to move to
def moveSecond(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][1] = '_'
        board.state[x][1] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#returns best position for the queen in the third column to move to
def moveThird(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][2] = '_'
        board.state[x][2] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#returns best position for the queen in the fourth column to move to
def moveFourth(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][3] = '_'
        board.state[x][3] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#returns best position for the queen in the fifth column to move to
def moveFifth(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][4] = '_'
        board.state[x][4] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#returns best position for the queen in the sixth column to move to
def moveSixth(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][5] = '_'
        board.state[x][5] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#returns best position for the queen in the seventh column to move to
def moveSeventh(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][6] = '_'
        board.state[x][6] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#returns best position for the queen in the eighth column to move to
def moveEighth(val):
    global array
    index = 0
    least = 100

    for x in range(8):
        board = copy.deepcopy(val)
        for i in range(8):
            board.state[i][7] = '_'
        board.state[x][7] = 'Q'
        board.heuristic = numAttacking(board.state)     
        array[x] = board

    for x in range(8):
        if(array[x].heuristic < least):
            least = array[x].heuristic
            index = x
    
    return array[index]

#prints board in an 8 x 8 configuration
def printBoard(board):
    for x in range(8):
        for i in range(8):
            print(board[x][i], end=' ')
        print()
 
currentState = initialize()
print("initial state:")
printBoard(currentState.state)

iterations = 0

#calls functions to move each queen one column at a time
while(currentState.heuristic != 0):
    currentState = moveFirst(currentState)
    currentState = moveSecond(currentState)
    currentState = moveThird(currentState)
    currentState = moveFourth(currentState)
    currentState = moveFifth(currentState)
    currentState = moveSixth(currentState)
    currentState = moveSeventh(currentState)
    iterations += 1
    #if algorithm gets stuck in local maxima, will reset board
    if(iterations > 10):
        print()
        print("stuck in local maxima, restarting initial state...")
        currentState = initialize()
        print("new initial state:")
        printBoard(currentState.state)
        iterations = 0

print()
print("solution:")
printBoard(currentState.state)
