#TRATAMENTO DE ERROS
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

except(ValueError, TypeError):
    print('Infelizmente, tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError: #podemos ter o tratamento de cada classe de erro. O mesmo try pode ter vários excepts
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro: #Entra no bloco caso ocorra um erro em try. Podemos usar apenas o except, mas utilizando "Exception as erro" guardamos informações da exceção na variável erro, permitindo mostrar para o usuário
    print(f'Problema encontrado: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte sempre!')