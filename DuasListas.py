import pandas as pd
cidades = ['Maringá ', 'Itabira', 'Uberlandia']
populacao = [403.063, 120.904, 699.097]

populacao_cidades = dict(zip(cidades,populacao))

populacao_cidades['Vitória'] = 365.855
del populacao_cidades['Itabira']

print(populacao_cidades)