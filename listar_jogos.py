import os

def listar_arquivos(diretorio):
    # Lista para armazenar os arquivos encontrados
    arquivos = []
    
    # Verifica se o diretório existe
    if os.path.exists(diretorio):
        # Itera pelos arquivos e subdiretórios do diretório
        for nome in os.listdir(diretorio):
            # Cria o caminho completo do arquivo
            caminho_completo = os.path.join(diretorio, nome)
            # Verifica se é um arquivo (não é um diretório)
            if os.path.isfile(caminho_completo):
                arquivos.append(nome)
    else:
        print(f"O diretório {diretorio} não existe.")
    
    return arquivos
