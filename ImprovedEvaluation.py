import chess

class ImprovedEvaluation:
    def __init__(self):
        self.piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 12
        }

        # Define weights for different evaluation factors
        self.material_weight = 1.0
        self.king_safety_weight = 0.8
        self.center_control_weight = 0.2
        self.piece_mobility_weight = 0.3

    def evaluate(self, board):
        # Material evaluation
        material_evaluation = self.evaluate_material(board)

        # King safety evaluation
        king_safety_evaluation = self.evaluate_king_safety(board)

        # Center control evaluation
        center_control_evaluation = self.evaluate_center_control(board)

        # Piece mobility evaluation
        piece_mobility_evaluation = self.evaluate_piece_mobility(board)

        # Combine the evaluations with weights
        evaluation = (
            self.material_weight * material_evaluation +
            self.king_safety_weight * king_safety_evaluation +
            self.center_control_weight * center_control_evaluation +
            self.piece_mobility_weight * piece_mobility_evaluation
        )

        return evaluation

    def evaluate_material(self, board):
        evaluation = 0

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                if piece.color == board.turn:
                    evaluation += self.piece_values.get(piece.piece_type, 0)
                else:  # Opponent's piece
                    evaluation -= self.piece_values.get(piece.piece_type, 0)
        return evaluation

    def evaluate_king_safety(self, board):
        # Implement king safety evaluation (e.g., evaluate king's position, pawn shelter, open files)
        # Return a value indicating king safety

        king_square = board.king(board.turn)
        king_safety_score = 0

        # Check if the king is castled
        if board.has_kingside_castling_rights(board.turn) or board.has_queenside_castling_rights(board.turn):
            king_safety_score+=5

        return king_safety_score

    def evaluate_center_control(self, board):
        # Implement center control evaluation (e.g., assess control of central squares)
        # Return a value indicating center control

        # Reward controlling central squares
        center_control_score = 0
        central_squares = [chess.D4, chess.E4, chess.D5, chess.E5]

        for square in central_squares:
            if board.piece_at(square) is not None and board.piece_at(square).color == board.turn:
                center_control_score += 1

        return center_control_score

    def evaluate_piece_mobility(self, board):
        # Implement piece mobility evaluation (e.g., assess the number of legal moves)
        # Return a value indicating piece mobility

        # Reward more legal moves
        piece_mobility_score = 0

        legal_moves = list(board.legal_moves)
        piece_mobility_score = len(legal_moves)

        return piece_mobility_score
