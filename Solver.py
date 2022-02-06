class Solver:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.filteredDict = dictionary[:]

    def solveNext(self, currentWord, alreadyGuessed):
        vowels = ['e', 'a', 'i', 'o', 'u', 'y'] #Sorted based on frequency in the English language
        potential_letters = []
        #Check if there hasn't been any correct guesses so far, in that case guess a vowel in order of frequency
        if not any(currentWord):
            vowelsLeft = [vowel for vowel in vowels if vowel not in alreadyGuessed]
            return (vowelsLeft[0], 1/(len(vowelsLeft)), vowelsLeft)

        for word in self.dictionary:
            if len(word) == len(currentWord):
               #Check if the word in question doesn't have any letters that don't match the current word
               if len([b[0] for a, b in list(enumerate(zip(word, currentWord))) if b[0] != b[1] and b[1] is not None]) == 0:
                   potential_letters.extend([letter for letter in word if not letter in alreadyGuessed])
        #Return the most frequent letter, along with accuracy
        letter = max(potential_letters, key = potential_letters.count)
        return (letter, potential_letters.count(letter)/len(potential_letters), potential_letters)


    def guess(self):
        pass

'''
    Jag vill hitta de ord som har bokstäver på samma ställen som det nuvarande ordet
    Sedan vill jag kunna se vilka bokstäver som vanligast förekommer bland de orden
    Koppla hashtabell med bokstäver?
    a b c d e
    '''

