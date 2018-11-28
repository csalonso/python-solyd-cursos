'''
EXERCÍCIOS - AULA 5 - PYTHON BÁSICO - SOLYD TREINAMENTOS
Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso, o porgrama irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
Após isso, irá imprimir os nomes da lista
'''

qtConvidados = int(input('Quantas pessoas serão convidadas? '))
lista = []

for i in range(qtConvidados):
    nome = input('Nome do convidado ' + str(i + 1) + ': ')
    lista.append(nome)

print('\nLista de Convidados:')
      
for i in range(qtConvidados):
    print(lista[i])
