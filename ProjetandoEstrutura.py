import pandas as pd

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann' , 'João Guimarães Rosa']

Livro = ['A arte da Guerra', 'Poesias Selecionadas', 'A montanha mágica', 'Primeiras estórias']

Ano = [2000, 2004, 2015, 2017]

dados = {
    'Autor':Autor,
    'Livro':Livro,
    'Ano':Ano
}
autores = pd.read_csv('autores.csv', index_col=0)
print(autores)
df = pd.DataFrame(dados)
print(df)