cadastro ={'philype': 'Drogafonte',
'glescio': 'Drogafonte',
'carol': 'Drogafonte',
'pedro': 'Senior' }

nome = input('Digite o nome do aluno: ')
empresa = input('nome da empresa: ')

if cadastro.get(nome):
    cadastro[nome] = cadastro
    print('ja existe o aluno',nome)

else:
    cadastro[nome] = empresa
print('cadastro feito',cadastro)

