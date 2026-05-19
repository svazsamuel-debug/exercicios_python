from time import sleep
dados = list()
pessoas = {}
total_idd = 0
mulheres = list()
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while pessoas['sexo'] not in 'MF':
        print('COMANDO INVÁLIDO!')
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    total_idd = total_idd + pessoas['idade']
    dados.append(pessoas.copy())
    esc = str(input('Quer continuar? [S/N]')).upper()
    while esc not in 'SN':
        print('COMANDO INVÁLIDO!')
        esc = str(input('Quer continuar? [S/N]')).upper()
    if esc == 'N':
        break
med = total_idd / len(dados)

print('=' * 60)
sleep(1)
print(len(dados), 'pessoas cadastradas.')
sleep(1)
print(f'A média de idades foi de {med:.2f} anos.')
sleep(1)
print('Mulheres na Lista: ')
for i in mulheres:
    print(f'{i}, ', end=' ')
sleep(1)
print('\n')
print('=' * 60)
print(f'Lista de pessoas com idade acima da média: {med}.'.center(60))
sleep(1)
for pessoa in dados:
    if pessoa['idade'] > med:
        print(f'Nome: {pessoa["nome"]}, Sexo: {pessoa["sexo"]}, Idade: {pessoa["idade"]}.')
print('=' * 60)
print('FIM DO PROGRAMA!'.center(60))
print('=' * 60)
