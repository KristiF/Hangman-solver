from random import choice
from Solver import Solver
class Game:
    def __init__(self):
        self.words = self.loadWords()
        self.guessesleft = 10
        self.solver = Solver(self.words)
        self.guessedLetters = []

    def loadWords(self):
        with open('Dictionary.txt') as file:
            return [list(row.strip()) for row in file]


    def randomWord(self):
        self.solution = choice(self.words)
        self.currentWord = [None][:] * len(self.solution)

    def show(self):
        for char in self.currentWord:
            if char: print (char, end=' ')
            else: print('_', end=' ')
        print('\nGuesses left:', self.guessesleft)

    def guess(self, letter):
        self.guessedLetters.append(letter)
        indices = [i for i, x in enumerate(self.solution) if x == letter]
        if len(indices) > 0:
            for i in (indices):
                self.currentWord[i] = letter
        else:
            self.guessesleft -= 1

    def handleInput(self):
        guess = input('Guess (+ for the solver to solve all, ? to solve for next letter): ')
        if guess == '?':
            letter, accuracy, potential_letters = self.solver.solveNext(self.currentWord, self.guessedLetters)
            print('The solver suggest {}, accuracy: {}% \nPotential letters: {}'.format(letter, round(100*accuracy, 3), " ".join(potential_letters)))
            return




    def play(self):
        self.randomWord()
        while True:
            self.show()
            self.handleInput()
            if any(self.currentWord) is None:
                print('You won!')
                break
            if self.guessesleft == 0:
                print('You lost :(, correct word was', "".join(self.solution))
                break

game = Game()
game.play()