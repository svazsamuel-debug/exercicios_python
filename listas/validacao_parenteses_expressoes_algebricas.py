# Exercício: Analisar se a expressão foi escrita com os parênteses ordenadamente corretos
# Conceitos: Listas, Lógica, Matemática

parents = 0
expressao = str(input('Digite uma expressão: '))
frase = list(expressao)
correta = True
for c in frase:
    if c == '(':
        parents = parents + 1
    if c == ')':
        parents = parents - 1
        if parents < 0:
            correta = False
            break
if parents == 0 and correta:
    print('A sua expressão está certa!')
else:
    print('A sua expressão está incorreta!')
