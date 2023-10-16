import chess

class IDSMinimaxAI():
    def __init__(self, depth):
        self.max_depth = depth

    def choose_move(self, board):
        best_move = None
        best_value = float("-inf")

        for current_depth in range(1, self.max_depth + 1):
            for move in board.legal_moves:
                board.push(move)
                value = self.min_value(board, 1, current_depth)
                board.pop()

                if value > best_value:
                    best_value = value
                    best_move = move
                    print("move:", best_move, "value", best_value)

        print("IDS Minimax AI recommending move " + str(best_move))
        return best_move

    def min_value(self, board, depth, current_depth):
        if self.cutoff_test(board, depth, current_depth):
            return self.evaluate(board)

        value = float("inf")
        for move in self.order_moves(board.legal_moves, board):
            board.push(move)
            value = min(value, self.max_value(board, depth + 1, current_depth))
            board.pop()

        return value

    def max_value(self, board, depth, current_depth):
        if self.cutoff_test(board, depth, current_depth):
            return self.evaluate(board)

        value = float("-inf")
        for move in self.order_moves(board.legal_moves, board):
            board.push(move)
            value = max(value, self.min_value(board, depth + 1, current_depth))
            board.pop()

        return value

    # Modify the cutoff_test function to consider the current depth
    def cutoff_test(self, board, depth, current_depth):
        return depth >= current_depth or board.is_game_over()

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

    def order_moves(self, moves, board):
        ordered_moves = []
        capturing_moves = []
        checking_moves = []

        for move in moves:
            if board.is_capture(move):
                capturing_moves.append(move)
            elif board.gives_check(move):
                checking_moves.append(move)
            else:
                ordered_moves.append(move)

        # Prioritize capturing moves and checks, followed by non-capturing moves
        ordered_moves = capturing_moves + checking_moves + ordered_moves

        return ordered_moves