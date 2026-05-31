from random import randint
numeros = list()
def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        i = randint(1, 10)
        numeros.append(i)
    for c in numeros:
        print(c, end=' ')
    print('PRONTO!')

def somaPar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


#Programa Principal
sorteia(numeros)
somaPar(numeros)
