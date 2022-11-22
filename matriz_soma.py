matriz = [[0,0,0],[0,0,0]]
soma = 0
for a in range(0,2):
    for b in range(0,3):
        matriz[a][b] = input(f'Digite o valor das posições {a}{b}: ')
    soma = soma + matriz[a][b]
print(soma)

