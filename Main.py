from Game import Game
from Solver import Solver

def main():
    game = Game()
    solver = Solver(game.words)
    game.init()
    while not game.isFinished():
        game.show()
        user_input = input('Guess (+ for the solver to solve all, ? to solve for next letter): ')
        if user_input == '+':
            while not game.isFinished():
                game.guess(solver.solveNext(game.currentWord, game.guessedLetters)[0])
                print()
                game.show()
            return
        elif user_input == '?':
            letter, accuracy, potential_letters = solver.solveNext(game.currentWord, game.guessedLetters)
            print('The solver suggest {}, accuracy: {}% \nPotential letters: {}'.format(letter, round(100*accuracy, 3), " ".join(potential_letters)))
        else:
            if game.guess(user_input):
                print(user_input, 'was correct')
            else:
                print(user_input, 'was wrong')


if __name__ == '__main__':
    main()