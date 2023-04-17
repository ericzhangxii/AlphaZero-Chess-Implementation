import chess

class Game():

    def getInitBoard(self):
        return chess.Board()
    
    def getBoardSize(self):
        return (8, 8)
    
    def getActionSize(self):
        return 4672
    
    def getNextState(self, board, player, action):
        assert player == 1 or player == -1
        board.push(action)
        return (board, -player)

    def getValidMoves(self, board, player):
        return board.legal_moves
    
    def getGameEnded(self, board, player):
        if board.is_game_over():
            if board.is_checkmate():
                return -player
            else:
                return 0
        return None
    
    def getCanonicalForm(self, board, player):
        return board