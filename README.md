# Hangman-solver
A hangman solver (and game) made in Python

# Strategy
It starts off by guessing a vowel, in order of most frequently used to least, until it guesses one correctly. Then it uses a probabilistic approach based on a given wordlist, by filtering out non-matching words and then gathering the letters of the remainding and returns the most common one.

# Performance
The time-complexity is O(n) where n is the number of entries in the dicitonary. Assuming 6 lives, it had a 90% win rate and took an average of 4.2 ms to solve a game.

# License
Released under Creative Commons Attribution 4.0 International Public License. [You can read it here.](https://creativecommons.org/licenses/by/4.0/legalcode)
