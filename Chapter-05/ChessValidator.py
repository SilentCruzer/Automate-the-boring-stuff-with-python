def ValidChessBoard(chess_board):
	if 'wking' not in chess_board.values() or 'bking' not in chess_board.values():
		return False

	black_pieces = 0
	white_pieces = 0
	for pieces in chess_board.values():
		if pieces[0] == 'b':
			black_pieces += 1
		elif pieces[0] == 'w':
			white_pieces += 1
		else:
			return False
	if black_pieces > 16 or white_pieces > 16:
		return False

	b_pawn = 0
	w_pawn = 0
	for pieces in chess_board.values():
		if pieces == 'bpawn':
			b_pawn +=1
		if pieces == 'wpawn':
			w_pawn +=1

	if b_pawn > 8 or w_pawn > 8:
		return False

	position_numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
	position_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

	for pieces in chess_board.keys():
	 	if pieces[0] not in position_numbers:
	 		return False
 		if pieces[1] not in position_letters:
	 		return False

	names = ['pawn', 'knight', 'bishop', 'rook', 'queen','king']
	for pieces in chess_board.values():
	 	if pieces[1:] not in names:
	 		return False

	return True

chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
valid_or_not = ValidChessBoard(chess_board)
if valid_or_not:
	print("This is a valid chessboard")
else:
	print("This is not a valid chessboard")



