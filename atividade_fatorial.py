def fat (n = 1):
    f = 1
    for x in range (1, n + 1):
        f = f * x
    return  f
a = (int(input('Digite um numero: ')))
fatorial = fat(a)
print(fatorial)