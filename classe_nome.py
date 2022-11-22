class carro:   #cabeçalho da classe
    """Docstrings """
    def __init__(self,modelo,cor,ano):    #método construtor
        self.modelo = input('Didite o modelo: ')     #atributo de instancia
        self.cor = input('Digite a cor: ')  #atributo de instancia
        self.ano = input('Digite o ano: ')
    def nome1 (self):
        nome = self.modelo + self.cor + self.ano
        #soma = self.x + self.y + self.dado  #operação com variaveis globais
        return (nome)     #retorno do método
nome = carro(0,0,0)    #objeto instanciado
print(f'Modelo: {nome.modelo} ',end=" " )    #mostra o resultado do metodo soma
print(f'Cor: {nome.cor} ',end=" " )
print(f'Ano: {nome.ano} ')

class carro1:
    """Docstrings """

    def __init__(self,modelo1,cor1,ano1):  # método construtor
        self.modelo1 = input('Didite o modelo: ')  # atributo de instancia
        self.cor1 = input('Digite a cor: ')  # atributo de instancia
        self.ano1 = input('Digite o ano: ')

    def nome2(self):
        nome2 = self.modelo1 + self.cor1 + self.ano1
        # soma = self.x + self.y + self.dado  #operação com variaveis globais
        return (nome2)  # retorno do método


nome2 = carro1(0, 0, 0)  # objeto instanciado
print(f'Modelo: {nome.modelo1} ',end=" " )    #mostra o resultado do metodo soma
print(f'Cor: {nome.cor1} ',end=" " )
print(f'Ano: {nome.ano1} ')
