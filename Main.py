word = ['h', 'e', 'j', 's', 'a', 'n']
currentWord = ['h', None, None, None, None, None]

#print(set(list(enumerate(word))).intersection(list(enumerate(currentWord))))

print([e[1] for e in set(list(enumerate(currentWord))).intersection(list(enumerate(word)))])

#print()