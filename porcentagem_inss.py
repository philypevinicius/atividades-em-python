def inss():
    salario = float(input('Digite o INSS: ').replace(".", "").replace(",", "."))
    inss2 =  salario - (salario*7.5/100)
    return inss2
print(f'O INSS com acréscimo de 7,5% é: R${inss():.2f}')