import pandas as pd
nome_cidade = pd.Series(['Maringá ', 'Itabira', 'Uberlandia'])
populacao = pd.Series([403.063, 120.904, 699.097])

pd.DataFrame({"Cidade" :nome_cidade, "População" : populacao})
