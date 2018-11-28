from cliente import Cliente


class Conta(Cliente):

    def __init__(self, cliente, saldo, limite):
        Cliente.__init__(self, cliente.nome, cliente.cpf, cliente.idade)
        self.saldo = saldo
        self.limite = limite

    def sacar(self, qtSaque):
        if(self.saldo >= qtSaque):
            self.saldo -= qtSaque
        else:
            print('Saque indisponível')

    def depositar(self, vlDeposito):
        if(vlDeposito > 0):
            self.saldo += vlDeposito
        else:
            print('Quantia inválida')

    def consultar(self):
        return self.saldo
