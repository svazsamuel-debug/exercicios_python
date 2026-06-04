def voto(ano):
    from datetime import date
    idade = (date.today().year - ano)
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade >= 65 or (16 <= idade < 18):
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#Programa Principal
ano = int(input('Ano de nascimento: '))
print(voto(ano))
