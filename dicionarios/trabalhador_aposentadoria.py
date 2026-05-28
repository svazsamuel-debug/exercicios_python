from datetime import datetime
dados = dict()
ano_atual = datetime.now().year

dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Número da CTPS (se não tiver, escreva 0): '))
dados['idade'] = (ano_atual - dados['nascimento'])

if dados['CTPS'] != 0:
    dados['ano_contrato'] = int(input('Ano da Contratação: '))
    dados['salario'] = float(input('Digite o seu salário: R$'))
    dados['aposentadoria'] = (dados['idade'] + (35 - (ano_atual - dados['ano_contrato'])))
    print('-=' * 30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    print('-=' * 30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')

print('-=' * 30)
