def init_board(r,c):
	board = [' ']*r
	for i in range(r):
		board[i] = [' ']*c
	return board

def print_function(board):
	print("\n----------------------")
	for i in range(len(board)):
		for j in range(len(board[i])):
			print("|" + board[i][j] + "|", end = "")
			if board[i][j] == 'X':
				print("|X|", end="")
			elif board[i][j] == 'O':
				print("|O|", end="")
			else:
				print("| |", end="")
		print("\n--------------------")

def place_token(board, token,x,y):	
	x = int(input("Row position: "))
	y = int(input("Col position: "))
	if x == "1":
		x = int(x)-1
	elif x == "2":
		x = int(x)-1
	elif x == "3":
		x = int(x)-1
	else:
		print("invalid")
	if y == "1":
		y = int(y)-1
	elif y == "2":
		y = int(y)-1
	elif y == "3":
		y = int(y)-1
	else:
		print("invalid")

	if board[x][y] == ' ':
		board[x][y] == token
	else:
		print("invalid")
	
	board[x][y]
	return board

def get_input(dimS, dimN):
	x = input(dimS+" position (1-"+str(dimN)+"): ")
	while x < "1" or x > str(dimN):
		print("That was not a valid choice, try again.")
		x = input(dimS+" position (1-"+str(dimN)+"): ")
	return int(x)-1

def check_right(x,y,token,col,board):
	while board[x][y] == token:
		x += 1
		if x > col-1:
			return True
	return False
	
def check_left(x,y,token,col,board):
	while board[x][y] == token:
		x -= 1
		if x < 0:
			return True
	return False

def check_horizontal(x,y,token,col,board):
	if x+1 > col:
		res = check_left(x,y,token, col,board)
		if res == True:
			return True
	elif x == 0:
		res = check_right(x,y,token,col,board)
		if res == True:
			return True
	else:
		res1 = check_left(x,y,token,col,board)
		res2 = check_right(x,y,token,col,board)
		if res1 == True and res2 == True:
			return True
	return False

def check_up(x,y,token,row,board):
	while board[x][y] == token:
		y -= 1
		if y < 0:
			return True
	return False

def check_down(x,y,token,row,board):
	while board[x][y] == token:
		y += 1
		if y > row-1:
			return True
	return False

def check_vertical(x,y,token,row,board):
	res = False
	if y+1 > row:
		res = check_up(x,y,token,row,board)
	elif y == 0:
		res = check_down(x,y,token, row, board)
	else:
		res1 = check_up(x,y,token,row,board)
		res2 = check_down(x,y,token,row,board)
		if res1 == True and res2 == True:
			res = True
	return res

def check_win(x,y,token,row,board):
	res = False
	if check_horizontal(x,y,token,col,board):
		res = True


def main():
	row = int(input("How many rows? "))
	col = int(input("How many cols? "))
	board = init_board(row, col)
	print_function(board)
	current_player = 'X'
	win = False
	while win == False:
		x = get_input("Row", row)
		y = get_input("Col", col)
		while board[x][y] != ' ':
			print("That place is taken already.")
			x = get_input("Row", row)
			y = get_input("Col", col)
		board = place_token(board, current_player, x,y)
		print_function(board)
		res = check_horizontal(x,y,current_player,col,board)
		print(str(res))
main()
