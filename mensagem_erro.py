def soma (x, y):
    soma = x + y
    return soma
try:
    x = int(input('Digite um número: '))
    y = int(input('Digite um numero: '))
    print(soma(x, y))
except:
    print ('\033[31m'+'Erro. Digite um número!!'+'\033[0;0n]')