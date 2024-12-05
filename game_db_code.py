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
print(mygames.take_value("mygames",1,"User"))