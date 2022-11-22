par = 0
inpar = 0
N = int(input('Digite o numero: '))

while N != 0:

    if  N % 2 == 0:
        print('Seu numero é par')
        print('\033[31m'+'Caso queira parar, digite 0'+'\033[0;0m')
        par += 1

    else:
        print('seu numero é inpar')
        print('\033[31m'+'Caso queira parar, digite 0'+'\033[0;0m')
        inpar += 1
    N = int(input('Digite um numero:'))
print('\033[32m'+'Programa parado!!'+'\033[0;0m')
print('\033[34m'+'Tem'+'\033[0;0m',par,'\033[34m'+'numero pares e'+'\033[0;0m',inpar,'\033[34m'+'numeros impares no total tem'+'\033[0;0m',par+inpar,'\033[34m'+'numeros digitados :'+'\033[0;0m')