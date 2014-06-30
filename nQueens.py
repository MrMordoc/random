"""
numQueens is a function to solve the n-queens problem of how many ways can you fill a 
chessboard with queens so that none can attack each other.
The board is represented by a list of numbers. Each index in the list represents a row on the
chessboard, and the value at that index represents the column.
This solution was coded by Ron Fenolio
"""

def attackDiagonal(board, idx):
	"""
	takes a board and an index, and returns true if the queen at that index can diagonally attack
	the most recently added queen, which is in the last position in the list
	"""
	return abs((len(board) - 1) - idx) == abs(board[-1] - board[idx])

def hasAttacks(board):
	"""
	Takes a board and returns true if the most recently added queen can attack any other queen on the baord
	"""
	boardSize = len(board)
	for i in range(boardSize-1):
		if board[i] == board[-1] or attackDiagonal(board, i):
			return True
	return False

def numQueens(numQueens):
	"""
	Takes an int which represents the board size, and adds queens to the board while discarding
	boards where queens can attack each other. Returns a list of boards of all of the possible solutions.
	"""
	boards = [[]]
	while len(boards) > 0 and len(boards[0]) < numQueens:	
		nextTest = boards.pop(0)
		for i in range(numQueens):
			nextBoard = nextTest + [i]
			if not hasAttacks(nextBoard):
				boards.append(nextBoard)
	return boards

print len(numQueens(12))