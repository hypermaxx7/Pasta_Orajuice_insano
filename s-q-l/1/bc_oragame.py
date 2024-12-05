from class_version_sqlite import *
"""#noticias
noticias = Criar_Banco("noticias","noticias")

at_noticias = ["ID","Nome","Descrição"]
for x,y in enumerate(at_noticias):
    if y == "ID":
        at_noticias[x]+=" INTEGER PRIMARY KEY AUTOINCREMENT"
    if y == "Nome":
        at_noticias[x]+=" TEXT"
    if y == "Descrição":
        at_noticias[x]+=" TEXT"
noticias.create_table(at_noticias)
noticias.insert_table(["'Lançamento GTA 6'","'As expectativas dos fãs estão no topo'"])
noticias.show_table()
#cartão
Cartão = Criar_Banco("Cartão","Cartão")

at_Cartão = ["ID INTEGER PRIMARY KEY AUTOINCREMENT","Tipo TEXT","Validade TEXT","Codigo INTEGER"]

Cartão.create_table(at_Cartão)
Cartão.insert_table(["'Crédito'","'25/10/2008'",876789])
Cartão.show_table()
#Pix
Pix = Criar_Banco("Pix","Pix")

at_Pix = ["ID INTEGER PRIMARY KEY AUTOINCREMENT","Código TEXT","Valor INTEGER","QRCODE TEXT"]

Pix.create_table(at_Pix)
Pix.insert_table(["email",90,"dsadsadasd"])
Pix.show_table()
#criptomoedas
Criptomoeda = Criar_Banco("Criptomoedas", "Criptomoedas")
at_criptomoeda = [
    "ID INTEGER PRIMARY KEY AUTOINCREMENT",
    "Tipo TEXT",
    "Valor INTEGER",
    "Válido INTEGER",
    "QRCODE TEXT"
]

Criptomoeda.create_table(at_criptomoeda)

Criptomoeda.insert_table(["Bitcoin", 90, 1, "dsadasdasd"])

print("\nRegistros na tabela Criptomoedas:")
Criptomoeda.show_table()
#jogos

Games = Criar_Banco("Games", "Games")
at_games = [
    "ID INTEGER PRIMARY KEY AUTOINCREMENT",
    "Nome TEXT",
    "Genero Text",
    "Descrição INTEGER"
]

Games.create_table(at_games)

Games.insert_table(["Resident evil", "Survival Horror", "Explore uma mansão com monstros demoniacos"])

print("\nRegistros na tabela Criptomoedas:")
Games.show_table()
"""
#Usuario
Game = Criar_Banco("Game", "Game") 

at_game = [
    "ID INTEGER PRIMARY KEY AUTOINCREMENT",
    "Nome TEXT",
    "requisitos TEXT",
    "descrição TEXT",
    "Dir TEXT" 
]

Game.create_table(at_game)

Game.insert_table(["teste2","8gb RTX I5","esse é o exemplo de descrição do jogo","C:/Users/samuel_r_raulino/Documents/GitHub/Pasta_Orajuice_insano/games/teste2.zip"])


Game.show_table()