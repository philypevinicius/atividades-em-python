# resposta da atividade 01/06/2021
casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salario"))

print(casa)

if salario < 2000:
    print("Empréstimo negado")

elif salario > 2000 or salario < 3000:
    print("Empréstimo aprovado")
    print('Prestação no valor: ',casa/240)

elif salario > 3000 or salario < 4000:
    print("Empréstimo aprovado")
    print('Prestação no valor: ',casa/180)

elif salario >4000:
    print("Empréstimo aprovado")
    print('Prestação no valor: ',casa/120)
# (upeer) serve para por tudo maiuscula
# (for) uma quantidade de vez que faça
# (while) não informa quantas vezes ele faça a repetição
#(. capitalize()) a inicial maiscula