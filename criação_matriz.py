def matriz():
    """
     esta função matriz recebe função 3 por 4!
     :param for: é o contador
     :param x: é a quantidade de linhas
     :param z: é a quantidade de colunas
     :return: retorna o valor da matriz
    """
    matriz = [[], [], []]
    for x in range (0, 3):
        for z in range (0, 4):
            matriz[x].insert(z, 0)
    return matriz

a = matriz()
for x in a:
    print(x)
help(matriz)
