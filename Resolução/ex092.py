from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().title()
pessoa['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (digite 0 se não tiver): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
for k, v in pessoa.items():
    print(f'{k.title()} tem o valor {v}')