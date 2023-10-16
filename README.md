# Chess

This is my project for my class COSC 76: Artifical Intelligence where I used Minimax algorithms, Transpositional Tables, Alpha-Beta Pruning, Iterative Deepening Search, and tailored evaluation functions to create a high-functioning chess program.


### How to Play
When running test_chess.py, it will prompt the level of depth of which the AI will be functioning with. 

Then, there will be a list of AIs to choose from for the user to play against. Write the full name of the AI (case sensitive) to play.

- `test_chess.py`: contains the testing interface for the different chess AIs.
- `ChessGame.py`: contains implementation of the chess Model.
- `gui_chess.py`: contains the chess GUI.
- `HumanPlayer.py`: contains the implementation for the HumanPlayer, takes manual input from the user.
- `RandomAI.py`: Randomly generates moves from the list of legal moves available and plays it.
- `MinimaxAI.py`: Uses a minimax algorithm to choose a move.
- `IDSMinimaxAI.py`: Implements Iterative Deepening Search into the Minimax algorithm.
- `AlphaBetaAI.py`: Implements Alpha-Beta Pruning into the IDSMinimaxAI.
- `AlphaBetaAI2.py`: Implements a transposition table into the AlphaBetaAI.
- `ImprovedEvaluation.py`: Enhances the evaluation function so the AI can make smarter decisions.
- `StockfishCopyAI`: Implements ImprovedEvaluation.py to be the strongest AI.
