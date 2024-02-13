import pandas as pd

disciplinas = {'cursos' : ['Estatística', 'Economia', 'Cálculo', 'Geometria'],
               'créditos' : [90, 60, 90, 40],
               'requisito' : [True, False, True, False]}
data = pd.DataFrame(disciplinas)
print(data)