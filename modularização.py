import fdescontos
func = str(input('Digite o nome do funcionario: '))
salario = float(int(input('Digite o valor do salario: ')))
descinss = fdescontos.inss(func, salario)
print(descinss)
descirpf = fdescontos.irpf(func, salario)
print(descirpf)
descvt = fdescontos.vt(func, salario)
print(descvt)
