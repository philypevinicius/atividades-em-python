sa = float(input('Digite o salário: R$').replace(".","").replace(",","."))
por =  (sa*10/100) + (f'{sa:.2f}')
print(f'O salario co acréscimo de 10% é: R${por:.2f}')