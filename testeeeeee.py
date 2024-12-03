import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Exemplo de Imagem com Pillow")

# Carregando a imagem com Pillow
image_path = "Imagens\image_background.png"  # Substitua pelo caminho da sua imagem
image = Image.open(image_path)

# Convertendo a imagem para o formato que o Tkinter pode entender
image_tk = ImageTk.PhotoImage(image)

# Criando um label para exibir a imagem
label = tk.Label(root, image=image_tk, height=250, width=500)
label.pack(pady=20, padx=15)

root.mainloop()