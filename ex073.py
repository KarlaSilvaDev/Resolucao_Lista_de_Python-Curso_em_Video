"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Vasco da Gama."""


times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Atlético-MG', 'Cruzeiro', 'Flamengo',
         'Athletico-PR', 'São Paulo', 'Santos', 'Grêmio', 'Fortaleza', 'Bragantino', 'Bahia',
         'Cuiabá', 'Internacional', 'Goiás', 'Vasco da Gama', 'Corinthians', 'América-MG',
         'Coritiba')
print('-=-'*10, f'\nLista de times do brasileirão {times}')
print('-=-'*10, f'\nOs cinco primeiros são {times[:5]}')
print('-=-'*10, f'\nOs quatro últimos são {times[-4:]}')
print('-=-'*10, f'\nTimes em ordem alfabética: {sorted(times)}')
print('-=-'*10, f'\nO Vasco da Gama está na {times.index("Vasco da Gama")+1}ª posição')
#Se colocarmos Vasco da Gama entre aspas simples na linha anterior, o programa apresenta erro porque teremos uma
# aspas simples dentro de outra.
