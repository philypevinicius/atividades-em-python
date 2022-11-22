class produto:

    def __init__(self):
        self.cod = input('Digite o Código: ')
        self.nome = input('Digite o Nome: ')
        self.preco = float(input('Digite o Preço: '))
        self.quantidade = int(input('Digite a quantidade: '))

    def alterar(self):
        print('Nome: (',self.nome,') ','Código: (',self.cod,')','preço: (',self.preco,') ','Quantidade: (',self.quantidade,')')
        opcao = int(input('Gostaria de alterar algo? se sim, digite 1, se não digite 2: '))
        while opcao != 2:
            o = int(input('O que você gostaria de alterar:\n1 - nome\n 2 - código\n 3 - preço\n 4 - quantidade: '))
            if o == 1:
                self.nome=input('Digite o nome do produto: ')
            elif o == 2:
                self.cod=int(input('Digite o nome do produto: '))
            elif o == 3:
                self.preco=float(input('digite o preço: '))
            elif o == 4:
                self.quantidade=int(input('digite a quantidade: '))
            opcao=int(input('gostaria de alterar algo? Se sim digite 1, se não digite 2: '))
        print('Feito!')

p1= produto()
p1.alterar()
print(f'Nome: ({p1.nome}) Codigo:({p1.cod}) Preço: ({p1.preco}) Quantidade: ({p1.quantidade})')










