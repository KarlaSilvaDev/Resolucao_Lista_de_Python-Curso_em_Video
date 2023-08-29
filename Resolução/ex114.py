import urllib
import urllib.request

def acessível(nome, site):
    try:
        urllib.request.urlopen(site)
    except:
        print(f'\033[0;31mO site {nome} não está acessível.\033[m')
    else:
        print(f'\033[0;32mO site {nome} está acessível.\033[m')
       # print(site.read()) #exibe o código html do site

# Exemplo de uso
site = acessível('Pudim', 'http://www.pudim.com.br')