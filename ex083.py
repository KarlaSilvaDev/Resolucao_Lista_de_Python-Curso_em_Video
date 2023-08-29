
expr = str(input('Digite a expressão: ')).strip()
listaTeste = []

for l in expr:
    if l == '(':
        listaTeste.append(l)
    elif l == ')':
        if len(listaTeste) > 0: #Se eu tiver parênteses abertos na lista, eu removo o último, pois este faz par com o parêntese fechando
            listaTeste.pop() #remove o último item da lista
        else:
            listaTeste.append(l) #Adiciono o parêntese fechando à lista mesmo que ela não tenha um outro fazendo par, pois a validade da expressão será invalidada caso a lista não esteja vazia
            break

if len(listaTeste)==0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')