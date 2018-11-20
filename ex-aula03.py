'''
EXERCÍCIO - AULA 3 - PYTHON BÁSICO - SOLYD TREINAMENTOS
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide  se ela está apta a ser do exército.
Para entrar no exército é preciso ter mais de 18 anos, pesar mais ou igual a 60 kilos e medir mais ou igual 1,70
'''

idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))

if(idade >= 18 and peso >= 60 and altura >= 1.70):
    print('Está apto a ser do exército')
else:
    print('Não está apto a ser do exército')
