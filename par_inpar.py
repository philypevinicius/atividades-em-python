par = 0
inpar = 0
n1 = int(input('digite o numero: '))
n2 = int(input('digite o numero: '))

for x in range (n1,n2+1):

    if x % 2 == 0:
        par += 1

    else:
        inpar += 1
print('Entre',n1,'e',n2,'tem',par,'numero pares e',inpar,'numeros impares.')

