matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
for a in range(0,3):
    for b in range(0,3):
        matriz[a][b] = int(input(f'Digite o valor da posição {a}{b}: '))
        resto = matriz[a][b] % 2
        if resto ==0:
            par = par+1
            print("par")

print('\033[31m'+'='*20+'\033[0;0m')
print('\033[34m'+ f'tem {par:^4}numeros Par',end = ''+'\033[0;0m')
print()
print('\033[31m'+'='*20+'\033[0;0m')