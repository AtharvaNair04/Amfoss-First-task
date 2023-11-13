def isValidChessBoard(board):
    white_pieces={'pawn':0,'knight':0 ,'bishop':0,'rook':0,'queen':0,'king':0}
    black_pieces={'pawn':0,'knight':0 ,'bishop':0,'rook':0,'queen':0,'king':0}
    for position,piece in board.items():
        if not(position[0] in '12345678' and  position[1] in 'abcdegh'):
            return False
        if not(piece[0] in  'wb' and piece[1:] in white_pieces):
            return False
        if  piece[0]=='w':
            white_pieces[piece[1:]]+=1
        else:
            black_pieces[piece[1:]]+=1
    for play_piece in [white_pieces,black_pieces]:
        if sum(play_piece.values())>16 or play_piece['pawn']>8:
            return False
    if white_pieces['king']!=1 or black_pieces['king']!=1:
        return False
    return True
chess_board={'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}
print(isValidChessBoard(chess_board)) 
