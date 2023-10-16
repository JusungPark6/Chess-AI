# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from IDSMinimaxAI import IDSMinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from AlphaBetaAI2 import AlphaBetaAI2, TranspositionTable
from StockfishCopyAI import StockfishCopyAI


import sys

depth = int(input("What depth would you like to play at?"))
print("Choose the AI to play against: 1) RandomAI 2) MinimaxAI 3) IDSMinimaxAI 4) AlphaBetaAI1 5) AlphaBetaAI2 6) StockfishCopyAI")
ai_name = input()
match ai_name:
    case "RandomAI":
        player2 = RandomAI()

    case "MinimaxAI":
        player2 = MinimaxAI(depth)

    case "IDSMinimaxAI":
        player2 = IDSMinimaxAI(depth)

    case "AlphaBetaAI1":
        player2 = AlphaBetaAI(depth)

    case "AlphaBetaAI2":
        player2 = AlphaBetaAI2(depth)
    case "StockfishCopyAI":
        player2 = StockfishCopyAI(depth)

player1 = HumanPlayer()

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()


#print(hash(str(game.board)))
