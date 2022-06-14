import itertools
from random import choice
from copy import deepcopy

def generate(numbers,operators):
    combo_ops = list(''.join(a) for a in itertools.product(operators,repeat=2))
    #combo_ops.remove("//")
    operators = operators[0:-1]
    print(combo_ops,operators)
    equals = ["=="]
    count = 1
    test = set()
    for numa in numbers[1:]:#first digit, no leading zero
        for terms in range(1,3):#There must be at least 1 digits but no more than 2 in positions 1-3 
            for a in sorted(list(set(itertools.product(numbers,repeat=terms)))):
                for ops in range(1,4):#At least 1 but no more than 2 operators:
                    for b in set(itertools.product(operators,repeat = 3-terms)):
                        for front in set(itertools.permutations(a+b)):
                            cont = True
                            for xx in combo_ops:
                                if xx in ''.join(front):
                                    #print(xx,''.join(front))
                                    #input("")
                                    cont = False
                                    break
                            if cont:
                                for terms2 in range(1,3):#there must be at least 1 digit but no more than 2 in positions 4-6
                                    for c in sorted(list(set(itertools.product(numbers,repeat=terms2)))):
                                        for d in sorted(list(set(itertools.product(operators,repeat = 2-terms2)))):#there can be only 1 operator in positions 4 - 6
                                            q = list(c)+list(d) + ['==']
                                            for back in set(itertools.permutations(q)):
                                                for numb in numbers:#last digit
                                                    e = [numa]+list(front)+list(back)+[numb]
                                                    cont2 = True
                                                    for yy in combo_ops:
                                                        if yy in ''.join(e):
                                                            cont2 = False
                                                            break
                                                    if cont2:
                                                        #print(e)
                                                        #input("")
                                                        if count % 150107 == 0:
                                                            print(count,''.join(e),len(''.join(e))-1,len(test))
                                                        count += 1
                                                        flag2 = True
                                                        j = e.index('==')                               
                                                        for g in range(j+1,8):
                                                            if e[g] not in numbers:
                                                                #print(j,g,e[g],e)
                                                                flag2 = False
                                                                break
                                                        if flag2:
                                                            f = ''.join(e)
                                                            #print(f)
                                                            if '00' not in f or '00' in f and '10' in f or '20' in f or '30' in f or '40' in f or '50' in f or '60' in f or '70' in f or '80' in f or '90' in f:
                                                                try:
                                                                    if eval(f):
                                                                        #print(f,len(test))
                                                                        test.add(f)
                                                                        #print(f)
                                                                except:
                                                                    pass
    with open('options.txt','a') as m:
        for n in test:
            m.write(n+'\n')

def guess(numbers,operators,known,pos,options):
    rem_options = deepcopy(options)
    for x in options:
        flag = True
        for y in range(8):
            if known[y] != x[y]:
                flag = False
                break
            if pos[y] not in x:
                flag = False
                break
        if not flag:
            rem_options.remove(x)
    return choice(rem_options)
    
numbers = ['0','1','2','3','4','5','6','7','8','9']
operators = ["+","-","*","/",'==']
#generate(numbers,operators)#skip once this has been done once
options = []
with open("sortedoptions.txt",'r') as f:
    options = f.read().split('\n')
options = [i for i in options if i]
#options = [sub.replace('//', '/') for sub in options]
#for a in options:
#    if not eval(a):
#        options.remove(a)
options = [sub.replace('==', '=') for sub in options]
known = ['','','','','','','','']
pos = [[],[],[],[],[],[],[],[]]
excluded = [[],[],[],[],[],[],[],[]]
total_exclude = []
#colors = ['','','','','','','','']
guess = choice(options)
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
            l = set(tuple(m) for m in pos)
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
    guess = choice(guesses)
    print(guess)
