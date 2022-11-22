class funcionario:
    def __init__(self):
        self.nome = input('Gigite o nome do funcionario: ')
        self.idade = int(input("Digite a idade: "))
class gerente(funcionario):
    pass
class recepcionista(funcionario):
    pass

h1 = funcionario
print(h1)