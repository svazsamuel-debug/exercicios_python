"""
Desafio: Análise completa de números

Descrição:
O programa deve permitir que o usuário digite vários números até digitar 0.
Ao final, deve mostrar:

- Lista de números digitados
- Quantidade de números
- Maior número e suas posições
- Menor número e suas posições
- Média dos valores
- Lista de números pares
- Lista de números ímpares
"""

#Entrada de Dados
num = int(input('Digite um número: '))
if num != 0:
    numeros = []
    pares = []
    impares = []
    numeros.append(num)
    while num != 0:
        num = int(input('Digite um número ou 0 para sair: '))
        if num != 0:
            numeros.append(num)
    maior = menor = numeros[0]
    posmaior = []
    posmenor = []
    for c in numeros:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    for c, t in enumerate(numeros):
        if t == maior:
            posmaior.append(c)
        if t == menor:
            posmenor.append(c)
    for c in numeros:
        if c % 2 == 0:
            pares.append(c)
        else:
            impares.append(c)
          
    soma = sum(numeros)
    med = soma / len(numeros)

  #Saída de Dados
    print(f'Os números digitados foram {numeros}')
    print(f'Foram {len(numeros)} digitados.')
    print(f'O maior número foi {maior} na(s) posição(ões) {posmaior}.')
    print(f'O menor número foi {menor} na(s) posição(ões) {posmenor}.')
    print(f'A média dos números foi de {med}.')
    print(f'Os números pares são {pares}')
    print(f'Os números ímpares são {impares}')
else:
    print('Você digitou o 0 logo de primeira, não teve lista!')
