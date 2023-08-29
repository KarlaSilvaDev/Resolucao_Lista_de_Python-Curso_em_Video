aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-'*30)
for k, v in aluno.items():
    print(f'- {k.title()} é igual a {v}')
