from Game import Game
from Solver import Solver
import timeit


def tester(lives, iterations):
    game = Game(lives)
    wins = losses = 0
    solver = Solver(game.words)
    for i in range(iterations):
        game.init()
        while not game.isFinished():
            game.guess(solver.solveNext(game.currentWord, game.guessedLetters)[0])
        if game.hasWon():
            wins += 1
        elif game.hasLost():
            losses += 1
    print(wins, losses)
start = timeit.default_timer()
tester(6, 1)
stop = timeit.default_timer()

print('Time: ', stop - start)