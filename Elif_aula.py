print('Banco')
Casa = int(input("Digite o valor da Casa: "))
Salario = int(input("Digite o valor do Salario: "))
plm2e3 = 240
plm3e4 = 180
plm4 = 120
if Salario > 2000 or Salario < 3000:
    print(" Aprovado com o valor de: ", Casa/plm2e3)
elif Salario > 3000 or Salario < 4000:
    print(" Aprovado com o valor de: ", Casa/plm3e4)
elif Salario > 4000:
    print(" Aprovado com o valor de: ", Casa/plm4)
else:
    print("Emprestimo negado")

