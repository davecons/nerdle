import itertools
from random import choice, shuffle
from copy import deepcopy

def score(prop,guess):
    #test all possible guesses and see
    #which have the same color pattern as the guess
    ret = ""
    for a in range(8):
        if guess[a] == prop[a]:
            ret += 'G'
        elif guess[a] in prop:
            ret += 'P'
        else:
            ret += 'B'
    return ret

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


while True:
    best = 0
    guesses = []
    colors = input("Enter colors, G for Green, P for Purple, B for Black: ")
    for opt in options:
        #print(opt,guess,score(opt,guess))
        #input("")
        if score(opt, guess) == colors:
            guesses.append(opt)
    shuffle(guesses)
    for a in guesses:
        if len(set(a)) > best:
            best = len(set(a))
            guess = a
    print(guess)
    if input("Continue? (y/n): ").lower() == 'n':
        break
