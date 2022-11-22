class conta:
    def __init__(self):
        self.titular = input('Nome do titular: ')
        self.cod = int(input('Código do titular: '))
        self.saldo = float(input('Saldo do titular: '))

    def debitar(self, valor):
        self.saldo = self.saldo - valor
        return self.saldo

    def creditar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
class Poupanca(conta):

    def __init__(self,credito):
        self.creito = credito
        return

    def debitarcredito(self, valor):
        self.credito = self.creito - valor
        return self.creito

cp = Poupanca(100000)
cp.saldo = 10000
print(cp.saldo + cp.creito)
# c1 = conta()
# print(c1.saldo)
# print(c1.debitar)
