#Contador de Gols e Partidas de Jogadores
dados = list()
tentos = list()

while True:
    jogador = dict()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    for c in range(0, jogador['Partidas']):
        tentos.append(int(input(f'Quantos gols fez na partida {c + 1}? ')))
    jogador['Gols'] = tentos.copy()
    jogador['Total'] = sum(tentos)
    dados.append(jogador.copy())
    tentos.clear()
    esc = str(input('Quer continuar? [S/N] ')).strip().upper()
    while esc not in 'SN':
        print('COMANDO INVÁLIDO!')
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
print('=' * 60)
print(f'{"COD":<4}{"JOGADOR":<20}{"Gols":<15}{"Total":<10}')
for c in range(len(dados)):
    print(f'{c:<4} {dados[c]["Nome"]:<20} {str(dados[c]["Gols"]):<15} {dados[c]["Total"]:<10}')

while True:
    detalhe = int(input('Indique o COD do jogador para detalhar ou 999 para sair: '))
    if detalhe == 999:
        print('Obrigado por usar o nosso programa!')
        break
    if detalhe >= len(dados):
        print('COMANDO INVÁLIDO! TENTE NOVAMENTE!')
        detalhe = int(input('Indique o COD do jogador para detalhar ou 999 para sair: '))
    for c in range(0, dados[detalhe]['Partidas']):
        print(f'Na partida {c + 1}, o jogador {dados[detalhe]["Nome"]} fez {dados[detalhe]["Gols"][c]} gols.')
