matriz = [[0,0,0],[0,0,0]]
soma = 0
for a in range(0,len(matriz)):
    for b in range(0,len(matriz[0])):
        matriz[a][b] = int(input(f'Digite o valor das posições [{a}{b}]: '))
        if a == 0:
            soma = soma + matriz[a][b]
print('A soma é ',soma)
for a in range(0,len(matriz)):
    for b in range(0,len(matriz[0])):
        print(f'{matriz[a][b]:^4}', end='')
    print()