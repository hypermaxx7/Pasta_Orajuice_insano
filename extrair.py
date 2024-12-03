import zipfile

def extrair(caminho,destino):
    with zipfile.ZipFile(caminho, 'r') as zip_ref:
        zip_ref.extractall(destino)
        print(f"Arquivos extraídos para {destino}")

