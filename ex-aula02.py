'''
EXERCÍCIO - AULA 2 - PYTHON BÁSICO - SOLYD TREINAMENTOS
Faça um formulário que pergunte o nome, cpf, endereço, idade, altura e telefone.
Exiba em um relatório organizado
'''

#receber dados
nome = input('Nome: ')
cpf = input('CPF: ')
endereco = input('Endereço: ')
idade = int(input('Idade: '))
altura = float(input('Altura: '))
telefone = input('Telefone: ')

#exibir relatório
print('Nome:', nome)
print('CPF:', cpf)
print('Endereço:', endereco)
print('Idade:', idade, '\tAltura:', altura)
print('Telefone:', telefone)
