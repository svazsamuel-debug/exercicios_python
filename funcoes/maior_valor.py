#Programa cria uma função que identifica o maior valor

def maior(numeros):
    print('-' * 30)
    print('Analisando os valores passados...')
    print('-' * 30)
    if len(numeros) == 0:
        print('0 Foram analisados 0 números.')
        print('O maior número foi 0')
    elif len(numeros) == 1:
        for c in numeros:
            print(f'{c} ', end='')
            print(f'Foram analisados 1 números.')
            print(f'O maior valor foi {numeros[0]}')
    else:
        for c in range(0, len(numeros)):
            print(f'{numeros[c]} ', end='')
        print(f'Foram analisados {len(numeros)} valores')
        top = 0
        for c in range(0, len(numeros)):
            if numeros[c] >= top:
                top = numeros[c]
        print(f'O maior valor foi {top}')


#Programa Principal
numeros = 2, 4, 9, 5, 7, 1
maior(numeros)
numeros = 4, 7, 0
maior(numeros)
numeros = 1, 2
maior(numeros)
numeros = [6]
maior(numeros)
numeros = []
maior(numeros)
