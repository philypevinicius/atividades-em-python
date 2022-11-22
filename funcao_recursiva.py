from time import sleep

def contagem(n):
    if n == 0:
     print('fim')
    else:
        sleep(1.0)
        print(n)
        contagem(n - 1)
contagem(int(input('Digite um valor: ')))