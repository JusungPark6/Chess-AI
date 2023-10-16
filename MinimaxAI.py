import chess

class MinimaxAI():
    def __init__(self, depth):
        self.max_depth = depth

    def choose_move(self, board):
        best_move = None
        best_value = float("-inf")

        for move in board.legal_moves:
            board.push(move)
            value = self.min_value(board, 1)
            board.pop()

            if value > best_value:
                best_value = value
                best_move = move

        print("Minimax AI recommending move " + str(best_move))
        return best_move

    def cutoff_test(self, board, depth):
        # Check if we've reached a terminal state (win or draw) or the maximum depth.
        return depth >= self.max_depth or board.is_game_over()

    def max_value(self, board, depth):
        if self.cutoff_test(board, depth):
            return self.evaluate(board)

        value = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            value = max(value, self.min_value(board, depth + 1))
            board.pop()

        return value

    def min_value(self, board, depth):
        if self.cutoff_test(board, depth):
            return self.evaluate(board)

        value = float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = min(value, self.max_value(board, depth + 1))
            board.pop()

        return value

    def evaluate(self, board):
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9
        }

        evaluation = 0

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                if piece.color == board.turn:
                    evaluation += piece_values.get(piece.piece_type, 0)
                else:  # Opponent's piece
                    evaluation -= piece_values.get(piece.piece_type, 0)

        return evaluation