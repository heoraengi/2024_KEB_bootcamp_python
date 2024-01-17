#8-1
e2f = dict(dog ='chien', cat='chat', walrus='morse')
print(e2f) # {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

#8-2
print(e2f['walrus']) # morse

#8-3
f2e = {f:e for e,f in e2f.items()}
print(f2e) # {'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}

#8-4
for e,f in e2f.items():
    if f == 'chien' :
        print(e) # dog

#8-5
print(e2f.keys()) # dict_keys(['dog', 'cat', 'walrus'])

#8-6
life ={
    'animals' : {'cats': 'Henri', 'octopi' : 'Grumpy', 'emus' :'Lucy'},
    'plants' : {},
    'other' : {}
}
print(life) # {'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, 'plants': {}, 'other': {}}

#8-7
print(life.keys()) # dict_keys(['animals', 'plants', 'other'])

#8-8
print(life['animals'].keys()) # dict_keys(['cats', 'octopi', 'emus'])

#8-9
print(life['animals']['cats']) # Henri

#8-10
squares = {i:i*i for i in range(10)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}