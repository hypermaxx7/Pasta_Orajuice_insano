def remover_ultimos_caracteres(s,num):
    # Verifica se a string tem pelo menos 3 caracteres
    if len(s) >= num:
        return s[:-num]  # Retorna a string sem os 3 últimos caracteres
    else:
        return ""  # Retorna uma string vazia se a string tiver menos de 3 caracteres
