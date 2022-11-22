import random
a = []
b = 0
while  len(a) < 5:
    sorteio = random.randint(1, 10)
    if sorteio not in a :
        a.append(sorteio)
print(a)