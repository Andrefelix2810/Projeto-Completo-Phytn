import sqlite3
con = sqlite3.connect("rexon_metals.bd")
cur = con.cursor()
cur.execute("CREATE TABLE contato(nome, endereco, telefone)")
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
('contato',)
import panda as pd
series_obj = pd.Series([1,7,9,13,17,99])
series_obj
