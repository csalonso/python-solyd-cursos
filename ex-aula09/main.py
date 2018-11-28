'''
EXERCÍCIO - AULA 9 - PYTHON BÁSICO - SOLYD TREINAMENTOS
Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar_saldo
'''

from cliente import Cliente
from conta import Conta

nome = input('Nome: ')
cpf = input('CPF: ')
idade = input('Idade: ')

cliente1 = Cliente(nome, cpf, idade)

conta1 = Conta(cliente1, 500, 2000)

print(conta1.saldo)
conta1.sacar(1000)
print(conta1.consultar())
conta1.depositar(2000)
print(conta1.consultar())
conta1.sacar(750)
print(conta1.consultar())
