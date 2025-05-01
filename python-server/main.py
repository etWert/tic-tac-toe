from Game import Game
from Player import Player

board = [["" for _ in range(3)] for _ in range(3)]
count_players = input("enter 1 player or 2 players (1/2)")
if count_players == "1":
    name = input("enter your name")
    player1 = Player(name, 'x')
    player2 = Player("computer", 'o')
    players = {player1.name: player1.mark, player2.name: player2.mark}
else:
    name1 = input("player 1 enter your name")
    player1 = Player(name1, 'x')
    name2 = input("player 2 enter your name")
    player2 = Player(name2, 'o')
    players = {player1.mark: player1.name, player2.mark: player2.name}
current_player = "x"
moves = set()
winner = None
turn_count = 1
game = Game(board, players, current_player, moves, winner, turn_count)
game.play()
