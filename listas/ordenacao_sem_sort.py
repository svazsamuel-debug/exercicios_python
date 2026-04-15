#Exercício: Ordenar 5 números sem usar o sorted
#Conteúdos: Listas, Inserção, Lógica

numeros = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if len(numeros) == 0:
        numeros.append(num)
    else:
        if num < numeros[0]:
            numeros.insert(0, num)
        elif num > numeros[-1]:
            numeros.insert(len(numeros), num)
        else:
            for i in range(len(numeros)):
                if num < numeros[i]:
                    numeros.insert(i, num)
                    break
print(numeros)
