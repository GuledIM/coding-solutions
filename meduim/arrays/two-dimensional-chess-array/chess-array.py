board = []
 
for i in range(8): # create columns
    row = ['EMPTY' for i in range(8)] #create rows
    board.append(row)
    
# Adding pieces to array

#adding pawn files

board[1][0:7] = ['BLACK PAWN'] * 7 

board[6][0:7] = ['WHITE PAWN'] * 7 

#adding rooks

board[0][0] , board[0][7] = ['BLACK ROOK'] * 2 

board[7][0] , board[7][7] = ['WHITE ROOK'] * 2 

#adding knights

board[0][1] , board[0][6] = ['BLACK KNIGHT'] * 2 

board[7][1] , board[7][6] = ['WHITE KNIGHT'] * 2 

#adding bishops

board[0][2] , board[0][5] = ['BLACK BISHOP'] * 2 

board[7][2] , board[7][5] = ['WHITE BISHOP'] * 2 

board[0][3] , board[0][4] = 'BLACK QUEEN' , 'BLACK KING'

board[7][3] , board[7][4] = 'WHITE QUEEN' , 'WHITE KING'



print(board)


