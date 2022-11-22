def dobro (teste):
    posicao = 0
    for x in range (1,7):
        teste[posicao] = teste[posicao]*2 #A quantidade de vezes que ele vai dobrar ta no 2
        posicao = posicao + 1
    return teste

a = [2,4,5,6,7]
a.append(int(input('Digite um numero: ')))
print(dobro(a))