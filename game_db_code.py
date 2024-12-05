from class_version_sqlite import * 

mygames = Criar_Banco("mygames","mygames")
"""
at=[
    "ID INTEGER PRIMARY KEY AUTOINCREMENT",
    "Nome TEXT",
    "User Text"
]

mygames.create_table(at)
"""

import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('mygames.db')
cursor = conexao.cursor()

# Consultar o número de tabelas no banco de dados
cursor.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
numero_de_tabelas = cursor.fetchone()[0]
for x in range(numero_de_tabelas):
    print(mygames.take_value("mygames",numero_de_tabelas,"Nome"))
# Fechar a conexão
conexao.close()


