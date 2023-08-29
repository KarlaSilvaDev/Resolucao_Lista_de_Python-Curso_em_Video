def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 70 > idade >= 18:
        r = 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        r = 'VOTO NEGADO'
    else:
        r = 'VOTO OPCIONAL'
    return f'Com {idade} anos: {r}.'


print('-'*30)
a = int(input('Em que ano você nasceu? '))
print(voto(a))
