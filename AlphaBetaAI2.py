import chess
from math import inf
from IDSMinimaxAI import IDSMinimaxAI

class TranspositionTable:
    def __init__(self):
        self.table = {}

    def store(self, board, depth, value, node_type):
        board_hash = hash(str(board))
        self.table[board_hash] = (depth, value, node_type)

    def lookup(self, board):
        board_hash = hash(str(board))
        if board_hash in self.table:
            return self.table[board_hash]
        return None

class AlphaBetaAI2(IDSMinimaxAI):
    def __init__(self, depth):
        super().__init__(depth)
        self.transposition_table = TranspositionTable()

    def choose_move(self, board):
        best_move = None
        alpha = float("-inf")
        beta = float("inf")

        for current_depth in range(1, self.max_depth + 1):
            for move in self.order_moves(board.legal_moves, board):
                board.push(move)

                # Check the transposition table for cached values
                cached_entry = self.transposition_table.lookup(board)
                if cached_entry and cached_entry[0] >= current_depth:
                    value = cached_entry[1]
                else:
                    value = self.min_value(board, 1, current_depth, alpha, beta)
                    self.transposition_table.store(board, current_depth, value, "EXACT")

                board.pop()

                if value > alpha:
                    alpha = value
                    best_move = move

        print("Alpha-Beta AI-2 recommending move " + str(best_move))
        return best_move

    def min_value(self, board, depth, current_depth, alpha, beta):
        if self.cutoff_test(board, depth, current_depth):
            return self.evaluate(board)

        value = float("inf")
        for move in self.order_moves(board.legal_moves, board):
            board.push(move)
            value = min(value, self.max_value(board, depth + 1, current_depth, alpha, beta))
            board.pop()

            if value <= alpha:
                return value

            beta = min(beta, value)

        return value

    def max_value(self, board, depth, current_depth, alpha, beta):
        if self.cutoff_test(board, depth, current_depth):
            return self.evaluate(board)

        value = float("-inf")
        for move in self.order_moves(board.legal_moves, board):
            board.push(move)
            value = max(value, self.min_value(board, depth + 1, current_depth, alpha, beta))
            board.pop()

            if value >= beta:
                return value

            alpha = max(alpha, value)

        return value

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

