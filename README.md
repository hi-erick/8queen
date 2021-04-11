# 8queen

The n-queen problem is one which n-number of queens are placed on an n by n sized board. 
A queen is placed in each column of the board and the goal is for every queen to be on the board while not being attacked by any other queen. 

We use a random-restart hill climbing algorithm to find the best possible location for each queen on each column. Each iteration moves the queens where it determines that it will result in the least amount of pairs of queens attacking each other. If the algorithm gets stuck in a local maxima where it can't move any queen to get a better result (less queens attacking each other) then the algorithm will re-initialize the board to a new random initial state. The algorithm only tries to improve upon the current state of the board and does not keep a memory of the steps taken to reach the solution state.
