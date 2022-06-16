import itertools
from random import choice, shuffle
from copy import deepcopy

def score(prop,guess):
    #test all possible guesses and see
    #which have the same color pattern as the guess
    ret = ""
    for a in range(8):
        if colors[a] == 'B' and guess[a] not in guess[0:a]:
            black.add(guess[a])
        if guess[a] == prop[a]:
            ret += 'G'
        elif guess[a] in prop:
            ret += 'P'
        else:
            ret += 'B'
    for b in range(8):
        if prop[b] in black:
            return False
    if ret == colors:
        return True
    return False    

#open and clean the potential guesses
with open("sortedoptions.txt",'r') as f:
    options = f.read().split('\n')
options = list(set(options))
options = [i for i in options if i]
options = [sub.replace('==', '=') for sub in options]


#initialize and select the first guess
best = 0
guess = ""
shuffle(options)
for a in options:
    if len(set(a)) > best:
        best = len(set(a))
        guess = a
print(guess)

purple = set()
black = set()
while True:
    best = 0
    guesses = []
    colors = input("Enter colors, G for Green, P for Purple, B for Black: ")
    for opt in options:
        #print(opt,guess,score(opt,guess))
        #input("")
        if score(opt, guess):
            guesses.append(opt)
    shuffle(guesses)
    for a in guesses:
        if len(set(a)) > best:
            best = len(set(a))
            guess = a
    print(guess,len(guesses),"Odds of guessing are : "+str(1/len(guesses)*100)[0:4]+"%")
    if input("Continue? (y/n): ").lower() == 'n':
        break
