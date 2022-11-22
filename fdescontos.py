inss1 = 7/100
def inss(func,salario):
    inss2 = salario*inss1
    return (f'Desconto de R${inss2:.2f}'). replace(".",",")

irpf1 = 9/100
def irpf(func,salario):
    irpf2 = salario*irpf1
    return (f'Desconto de R${irpf2:.2f}'). replace(".",",")
vt1 = 6/100
def vt(func,salario):
    vt2 = salario*vt1
    return (f'Desconto de R${vt2:.2f}'). replace(".",",")
