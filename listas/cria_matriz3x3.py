'''O programa pede ao usuário os valores para cada elemento da Matriz 3 x 3 e mostra:
- Matriz Completa
- Soma dos valores pares
- Soma dos valores da terceira coluna
- O maior valor da segunda linha'''

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

soma_par = 0
soma_terceira_coluna = 0
maior = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um número para a posição {l}, {c}: '))
        if c == 2:
            soma_terceira_coluna = soma_terceira_coluna + matriz[l][c]
        if matriz[l][c] % 2 == 0:
            soma_par = soma_par + matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] >= maior:
                    maior = matriz[l][c]

print('\nMatriz:')
for linha in matriz:
    print('[', end=' ')
    for valor in linha:
        print(f'{valor:^3}', end=' ')
    print(']')

print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior}.')
