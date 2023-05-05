from random import choice

file = open('data.txt')

bigramms = []
for i in file:
    
    i = str(i.rstrip())
    x = int(len(i))
    out1 = '^' + i[0]
    bigramms.append(out1)
    for j in range (0, len(i) - 1):
        out2 = i[j] + i[j + 1]
        bigramms.append(out2)
    out3 = i[x - 1] + '$'
    bigramms.append(out3)


bigramms.sort()



def show(bigramms):
    table = dict()
    i = 0
    while i < len(bigramms):
        cnt = 1
        j = i
        while j + 1 < len(bigramms) and bigramms[j] == bigramms[j + 1]:
            j += 1
            cnt += 1
        table[bigramms[i]] = cnt
        print("'",bigramms[i], "'", sep='', end=', ')
        i = j + 1
    # return table
        

def generate(bigramms):
    name = ''
    i =''
    while True:
        i = choice(bigramms)
        if i[0] == '^':
            name += i[1]
            break
    i = ''
    while True:
        i = choice(bigramms)
        if i[0] != '^' and i[1] != '$':
            name += i
        if i[1] == '$':
            name += i[0]
            break

    return name
    

# print(generate(bigramms))
print(show(bigramms))
