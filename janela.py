from extrair import extrair
from listar_jogos import listar_arquivos
from remover_str import remover_ultimos_caracteres
import tkinter as tk
from tkinter import ttk
import os
import threading
import time

# Função para simular extração e atualizar o progresso
def extrair_com_progresso(caminho, diretorio, progresso):
    print(f"Extraindo: {caminho} para {diretorio}")
    total_steps = 100  # Simula progresso em 100 etapas
    for step in range(1, total_steps + 1):
        time.sleep(0.05)  # Simula tempo de execução
        progresso.set(step)  # Atualiza a barra de progresso
    extrair(caminho, diretorio)  # Chama a função real (se necessário)

# Janela principal
janela = tk.Tk()
janela.geometry("640x480")
arquivos = listar_arquivos("games")

# Variável global para a barra de progresso
progresso = tk.IntVar()

# Cria os botões e barra de progresso
for arquivo in arquivos:
    dir = "saida/" + remover_ultimos_caracteres(arquivo, 4)
    os.makedirs(dir, exist_ok=True)

    # Função para iniciar a extração em uma thread separada
    def iniciar_extracao(arquivo=arquivo, dir=dir):
        progresso.set(0)  # Reseta a barra de progresso
        threading.Thread(target=extrair_com_progresso, args=("games/" + arquivo, dir, progresso)).start()

    # Botão para o arquivo
    bot = tk.Button(
        text=remover_ultimos_caracteres(arquivo, 4),
        command=iniciar_extracao
    )
    bot.pack()

# Barra de progresso na parte inferior
barra_progresso = ttk.Progressbar(janela, variable=progresso, maximum=100)
barra_progresso.pack(fill=tk.X, pady=10)

janela.mainloop()
