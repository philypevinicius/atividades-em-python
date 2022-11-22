class Funcionario():
    def __init__(self,nome,empresa,cargo):
        self.nome = nome
        self.empresa = empresa
        self.cargo = cargo

nome = input('O seu nome: ')
empresa = input('A empresa: ')
cargo = input('O cargo: ')
Funcionario = Funcionario(nome, empresa,cargo)
print(Funcionario)