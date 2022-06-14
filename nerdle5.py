import itertools
from random import choice, shuffle
from copy import deepcopy
    
numbers = ['0','1','2','3','4','5','6','7','8','9']
operators = ["+","-","*","/"]
options = []
with open("sortedoptions.txt",'r') as f:
    options = f.read().split('\n')
options = [i for i in options if i]
options = [sub.replace('==', '=') for sub in options]
known = ['','','','','','','','']
pos = [[],[],[],[],[],[],[],[]]
excluded = [[],[],[],[],[],[],[],[]]
total_exclude = []
best = 0
guess = ""
shuffle(options)
for a in options:
    if len(set(a)) > best:
        best = len(set(a))
        guess = a
print(guess)


while True:
    guesses = []
    colors = input("Enter colors, G for Green, P for Purple, B for Black: ")
    for x in range(8):
        if colors[x] == 'G':
            known[x] = guess[x]
        elif colors[x] == 'P':
            pos[x].append(guess[x])
        elif colors[x] == 'B':
            excluded[x].append(guess[x])
    for a in range(8):
        for x in excluded[a]:
            j = set(x)
            k = set(known)
            l = set(list(itertools.chain(*pos)))
            #print(j,k,l)
            if j.intersection(k) == set() and j.intersection(l) == set():
                total_exclude.extend(list(j))
        
    total_exclude = list(set(total_exclude))
    for opt in options:
        flag = True
        for b in total_exclude:
            if b  in opt:
                flag = False
                break
        if flag:
            for y in range(8):
                for j in range(len(excluded[y])):
                    if opt[y] in excluded[j]:
                        flag = False
                        break
                if known[y] != '' and known[y] != opt[y]:
                    #print("Known is wrong: ",opt)
                    flag = False
                    pass
                for z in range(len(pos[y])):
                    if pos[y][z] != '' and pos[y][z] not in opt:
                        #print("Pos is not in opt: ",opt)
                        flag = False
                        break
                for z in range(len(pos[y])):
                    if pos[y][z] == opt[y]:
                        #print("NO: ",opt)
                        flag = False
                        break
        if flag:
            #print("Possible: ",known,pos,opt)
            guesses.append(opt)
    best = 0
    guess = ""
    shuffle(guesses)
    for a in guesses:
        if len(set(a)) > best:
            best = len(set(a))
            guess = a
    print(guess)
