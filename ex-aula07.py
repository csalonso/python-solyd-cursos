'''
EXERCÍCIO - AULA 7 - PYTHON BÁSICO - SOLYD TREINAMENTOS
Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dentro dessa coleção.
Faça outra função que retorna o menor número dessa coleção.
'''

def maior(x):
    maior = x[0]
    for i in x:
        if i > maior:
            maior = i
    return maior

def menor(x):
    menor = x[0]
    for i in x:
        if i < menor:
            menor = i
    return menor
