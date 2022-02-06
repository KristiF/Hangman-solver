from random import choice
from Solver import Solver

class Game:
    def __init__(self, lives):
        self.words = self.loadWords()
        self.solver = Solver(self.words)
        self.lives = lives

    def init(self):
        self.randomWord()
        self.guessesleft = self.lives
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
        print('Already guessed: ', " ".join(self.guessedLetters))

    def guess(self, letter):
        self.guessedLetters.append(letter)
        indices = [i for i, x in enumerate(self.solution) if x == letter]
        if len(indices) > 0:
            for i in (indices):
                self.currentWord[i] = letter
            return True
        else:
            self.guessesleft -= 1

    def hasWon(self):
        return not None in self.currentWord

    def hasLost(self):
        return self.guessesleft == 0

    def isFinished(self):
        return self.hasWon() or self.hasLost()
