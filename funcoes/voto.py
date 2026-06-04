import datetime
def voto():
    ano = int(input('Ano que nasceu: '))
    idade = (datetime.date.today().year - ano)
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')
    elif idade >= 65 or (16 <= idade < 18):
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


#Programa Principal
voto()
