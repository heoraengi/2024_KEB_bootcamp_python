### dict comprehension
univ = 'inha university'
counts_alphabet = {letter:univ.count(letter) for letter in univ}
print(counts_alphabet)
# {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

univ = 'inha university'
counts_alphabet = dict()
for letter in univ :
    counts_alphabet[letter] = univ.count(letter)
print(counts_alphabet)
# {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

#8-10
squares = {i:i*i for i in range(10)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}