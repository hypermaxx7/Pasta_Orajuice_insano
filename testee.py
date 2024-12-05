import tkinter as tk
from tkinter import ttk

class JanelaWindows7:
    def __init__(self, root):
        self.root = root
        self.root.title("Janela Estilo Windows 7")
        
        # Configurações para que a janela tenha tamanho fixo
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Alterar a cor de fundo para algo mais próximo do estilo Windows 7
        self.root.config(bg='#C0C0C0')  # Cor cinza-claro (padrão Windows 7)

        # Criando a barra de título customizada
        self.criar_barra_titulo()

        # Criando o botão de exemplo
        self.botao_exemplo = ttk.Button(self.root, text="Clique Aqui", command=self.exemplo_comando)
        self.botao_exemplo.place(relx=0.5, rely=0.5, anchor="center")

    def criar_barra_titulo(self):
        barra_titulo = tk.Frame(self.root, bg='#2B5797', height=30, relief='flat')
        barra_titulo.pack(fill=tk.X)

        # Adicionar título no canto esquerdo da barra
        titulo = tk.Label(barra_titulo, text="Janela Estilo Windows 7", fg='white', bg='#2B5797', font=("Arial", 10))
        titulo.pack(side=tk.LEFT, padx=10)

        # Botões de minimizar, maximizar e fechar (com comportamento básico)
        self.botao_fechar = tk.Button(barra_titulo, text='X', command=self.root.quit, relief='flat', bg='#2B5797', fg='white', font=("Arial", 10))
        self.botao_fechar.pack(side=tk.RIGHT, padx=5)
        
    def exemplo_comando(self):
        print("Botão clicado!")
    
if __name__ == "__main__":
    root = tk.Tk()
    janela = JanelaWindows7(root)
    root.mainloop()
