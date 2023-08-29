frase = 'Curso em Vídeo Python'
# Fatiamento de string
print(frase[3]) #imprime S
print(frase[3:13]) #imprime do 3 até o 12
print(frase[:13]) #imprime do ínicio (0) até o 12
print(frase[13:]) #imprime do 13 até o final
print(frase[1:15:2]) #imprime do 1 ao 14 pulando de 2 em 2
print(frase[1::2]) #imprime do 1 até o final pulando de 2 em 2
print(frase[::2]) #imprime do ínico até o final pulando de 2 em 2

# Análise de uma String
print(frase.count('o'))
print(len(frase)) #mostra o número de caracteres, contando os espaços na string
print(frase.strip()) #remove espaços indesejados no ínio e no final da string
print(frase.replace('Python', 'Android')) #troca as ocorrências "Python" para "android". Não muda o conteúdo da variável frase
#para mudar o conteúdo de frase, seria necessário digitar o seguinte: frase = frase.replace('Python', 'Android')
print('Curso' in frase) #verifica se a palavra curso está dentro da string frase e retorna True ou False
#No caso acima, se escrevermos 'curso' no comando, a resposta será False, pois o python diferencia maiúsculas de minúsculas
print(frase.upper())  #torna todos os caracteres maiúsculos
print(frase.title()) #torna apenas o primeiro caractere de cada palavra maiúsculo
print(frase.split()) #Cria uma lista transformando cada palavra da string em um elemento da lista



# Uso de três aspas duplas para poder utilizar apenas um comando print para imprimir um texto na tela
print("""isjiojsioJSIOJAiojsioJASOIJAIOSJoiajs
ioajsoiajsioajsiojaiosjioajsiojaiojsoiajs
ioasjoaijioajsoijoiajsioajiosjaiojsioajsoiaj""")
