import sqlite3

class Criar_Banco:
    def __init__(self, nome_arquivo, nome):
        self.nome = nome
        self.banco = sqlite3.connect(nome_arquivo + ".db")
        self.cursor = self.banco.cursor()

    def create_table(self, lista):
        query = "CREATE TABLE IF NOT EXISTS " + str(self.nome) + " ("
        for x, y in enumerate(lista):
            query += y
            if x != len(lista) - 1:
                query += ","
        query += ")"
        self.cursor.execute(query)

    def insert_table(self, valores):
        placeholders = ", ".join(["?" for _ in valores])  # Cria placeholders para os valores
        campos = ", ".join([f for f in self.get_columns() if f != "ID"])  # Exclui o campo ID
        query = f"INSERT INTO {self.nome} ({campos}) VALUES ({placeholders})"
        self.cursor.execute(query, valores)
        self.banco.commit()

    def get_columns(self):
        """Retorna os nomes das colunas da tabela."""
        self.cursor.execute(f"PRAGMA table_info({self.nome})")
        return [col[1] for col in self.cursor.fetchall()]

    def show_table(self):
        self.cursor.execute(f"SELECT * FROM {self.nome}")
        registros = self.cursor.fetchall()
        for registro in registros:
            print(registro)
    
    def conectar_bancos(self, db_arquivo_secundario, nome_secundario, tabela_secundaria, campo_chave):
        """Conectar a um banco de dados secundário e realizar consulta entre as tabelas."""
        # Anexar o banco de dados secundário
        self.cursor.execute(f"ATTACH DATABASE '{db_arquivo_secundario}' AS {nome_secundario}")
        
        # Exemplo de consulta para buscar dados de ambas as tabelas, relacionadas pela chave primária/estrangeira
        query = f"""
        SELECT {self.nome}.ID, {self.nome}.Nome, {nome_secundario}.{tabela_secundaria}.Valor
        FROM {self.nome}
        JOIN {nome_secundario}.{tabela_secundaria} ON {self.nome}.ID = {nome_secundario}.{tabela_secundaria}.{campo_chave}
        """
        
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        for registro in registros:
            print(registro)

