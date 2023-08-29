def titulo(txt):
    l = len(txt.strip()) + 10 #pega o tamanho do texto e soma um espaço em branco de 5 caracteres em cada lado (total = 10)
    print('-' * l)
    print(f'{txt:^{l}}')
    print('-' * l)


titulo('Gustavo Guanabara')
titulo('Curso de Python no Youtube')
titulo('CeV')