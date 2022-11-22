N1 = int(input('Digite uma opção: '))
N2 = int(input('Digite uma opção: '))
print('\033[34m'+'opções:\n1 Soma\n2 Subtração\n3 Digiter novos numeros\n4 Sair do programa'+'\033[0;0m')
opcao = int(input('\033[32m'+'Escolha: '+'\033[0;0m'))

while opcao != 4:
    if opcao == 1:
       print(N1,'+',N2,'=',N1 + N2)
       opcao = int(input('\033[32m'+'Escolha: '+'\033[0;0m'))
    elif opcao == 2:
        print(N1, '-', N2, '=', N1 - N2)
        opcao = int(input('\033[32m'+'Escolha: '+'\033[0;0m'))
    elif opcao == 3:
        N1 = int(input('Digite uma opção: '))
        N2 = int(input('Digite uma opção: '))
        opcao = int(input('\033[32m'+'Escolha: '+'\033[0;0m'))
    else:
        print('Digite uma opção valida')
        print('\033[34m'+'opções:\n[1] Soma\n[2] Subtração\n[3] Digiter novos numeros\n[4] Sair do programa'+'\033[0;0m')
        opcao = int(input('Escolha: '))
print('\033[31m'+'Fim do programa'+'\033[0;0m')