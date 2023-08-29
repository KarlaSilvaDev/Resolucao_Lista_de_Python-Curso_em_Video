from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #read text, tenta abrir o arquivo em modo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt = write text o + serve para criar o arquivo caso ele não exista
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';') #divide os dados pelo separador ;
            dado[1] = dado[1].replace('\n', '') #tira o \n do final do dado 1, pois colocamos na parte de cadastro para pular a linha
            print(f'{dado[0]:<30}{dado[1]:<3} anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') #append text - adiciona mais texto ao arquivo
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade} \n') # o \n serve para ele pular para a próxima linha quando for cadastrar uma nova pessoa
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

