import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from datetime import datetime
import pytz
import sqlite3
import json
import os

# Banco de dados
def conectar_bd():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )""")
    conn.commit()
    return conn

# Função para salvar o usuário logado
def salvar_usuario_logado(usuario):
    with open("usuario_logado.json", "w") as file:
        json.dump({"usuario": usuario}, file)

# Função para carregar o usuário logado
def carregar_usuario_logado():
    if os.path.exists("usuario_logado.json"):
        with open("usuario_logado.json", "r") as file:
            return json.load(file).get("usuario")
    return None

# Função para limpar o usuário logado
def limpar_usuario_logado():
    if os.path.exists("usuario_logado.json"):
        os.remove("usuario_logado.json")

# Tela de login e cadastro
class LoginCadastro:
    def __init__(self, master, ao_logar):
        self.master = master
        self.ao_logar = ao_logar
        self.master.title("Login/Cadastro")
        self.master.configure(background="gray")
        self.master.geometry("500x400")
        self.master.resizable(False, False)
        self.exibir_tela_login()

    def exibir_tela_login(self):
        self.limpar_tela()
        Label(self.master, text="Login", font=("Arial", 18), bg="gray").place(relx=0.4, rely=0.1)
        Label(self.master, text="Usuário:", font=("Arial", 14), bg="gray").place(relx=0.2, rely=0.3)
        entrada_usuario = Entry(self.master, font=("Arial", 14))
        entrada_usuario.place(relx=0.4, rely=0.3)

        Label(self.master, text="Senha:", font=("Arial", 14), bg="gray").place(relx=0.2, rely=0.4)
        entrada_senha = Entry(self.master, font=("Arial", 14), show="*")
        entrada_senha.place(relx=0.4, rely=0.4)

        def realizar_login():
            usuario = entrada_usuario.get()
            senha = entrada_senha.get()
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
            if cursor.fetchone():
                salvar_usuario_logado(usuario)
                self.ao_logar(usuario)
            else:
                messagebox.showerror("Erro", "Usuário ou senha inválidos!")
            if not usuario or not senha:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

        Button(self.master, text="Login", bg="#FFA500", font=("Arial", 14), command=realizar_login).place(relx=0.4, rely=0.6)
        Button(self.master, text="Cadastrar", bg="#FFA500", font=("Arial", 14), command=self.exibir_tela_cadastro).place(relx=0.55, rely=0.6)

    def exibir_tela_cadastro(self):
        self.limpar_tela()
        Label(self.master, text="Cadastro", font=("Arial", 18), bg="gray").place(relx=0.4, rely=0.02)

        Label(self.master, text="Usuário:", font=("Arial", 14), bg="gray").place(relx=0.2, rely=0.1)
        entrada_usuario = Entry(self.master, font=("Arial", 14))
        entrada_usuario.place(relx=0.4, rely=0.1)

        Label(self.master, text="Email:", font=("Arial", 14), bg="gray").place(relx=0.2, rely=0.2)
        entrada_usuario = Entry(self.master, font=("Arial", 14))
        entrada_usuario.place(relx=0.4, rely=0.2)

        Label(self.master, text="Data de nascimento:", font=("Arial", 14), bg="gray").place(relx=0.045, rely=0.3)
        entrada_usuario = Entry(self.master, font=("Arial", 14))
        entrada_usuario.place(relx=0.4, rely=0.3)

        Label(self.master, text="Senha:", font=("Arial", 14), bg="gray").place(relx=0.2, rely=0.4)
        entrada_senha = Entry(self.master, font=("Arial", 14), show="*")
        entrada_senha.place(relx=0.4, rely=0.4)

        Label(self.master, text="Senha2:", font=("Arial", 14), bg="gray").place(relx=0.2, rely=0.5)
        entrada_senha_confirmacao = Entry(self.master, font=("Arial", 14), show="*")
        entrada_senha_confirmacao.place(relx=0.4, rely=0.5)

        def realizar_cadastro():
            usuario = entrada_usuario.get()
            senha = entrada_senha.get()
            senha_confirmacao = entrada_senha_confirmacao.get()
            qnt_senha = len(str(senha))
            ver_senha = str(senha)

            if not usuario or not senha or not senha_confirmacao:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

            if senha != senha_confirmacao:
                messagebox.showerror("Erro", "As senhas não coincidem!")
                return
            
            if qnt_senha < 6:
                messagebox.showerror("Erro", "Senha deve ter mais de 6 dígitos")
                return
            
            if ver_senha.isupper() or ver_senha.islower():
                messagebox.showerror("Erro", "Senha deve conter letras maiusculas e minusculas")
                return
            
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))

            if cursor.fetchone():
                messagebox.showerror("Erro", "Nome de usuário já está sendo usado!")
            else:
                cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                self.exibir_tela_login()
            conn.close()
        
        Button(self.master, text="Cadastrar", bg="#FFA500", font=("Arial", 14), command=realizar_cadastro).place(relx=0.4, rely=0.6)
        Button(self.master, text="Voltar", bg="#FFA500", font=("Arial", 14), command=self.exibir_tela_login).place(relx=0.55, rely=0.6)

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

#### TELA PRINCIPAL! ####
class Application:
    def __init__(self, usuario_logado):
        self.window = Tk()
        self.criar_gradiente_fundo()
        self.usuario_logado = usuario_logado
        self.tela()
        self.frames_da_tela()
        self.widgets()
        self.carregar_imagem_logo()
        self.carregar_imagem_wall()
        self.window.mainloop()

    def carregar_imagem_logo(self):
        # Caminho da imagem - ajuste conforme necessário
        self.image_path = "Imagens\Fruitger_logo.png"  # Substitua pelo caminho correto da imagem
        try:
            self.image = Image.open(self.image_path)  # Abre a imagem
            self.image = self.image.resize((115, 125))  # Ajuste o tamanho da imagem, se necessário
            self.logo_image = ImageTk.PhotoImage(self.image)  # Converte a imagem para formato Tkinter

            # Cria um Label no frameLogo para exibir a imagem
            self.label_logo = Label(self.frameLogo, image=self.logo_image)
            self.label_logo.place(relx=0.5, rely=0.19, anchor="center")  # Centraliza a imagem dentro do frameLogo
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            messagebox.showerror("Erro", "Não foi possível carregar a imagem do logo.")

    def carregar_imagem_wall(self):
        # Caminho da imagem - ajuste conforme necessário
        self.image_path = "Imagens\menu_background.png"  # Substitua pelo caminho correto da imagem
        try:
            self.image = Image.open(self.image_path)  # Abre a imagem
            self.image = self.image.resize((776, 80))  # Ajuste o tamanho da imagem, se necessário
            self.logo_wall = ImageTk.PhotoImage(self.image)  # Converte a imagem para formato Tkinter

            # Cria um Label no frameLogo para exibir a imagem
            self.label_wall = Label(self.frame1, image=self.logo_wall)
            self.label_wall.place(relx=0.51, rely=0.6, anchor="center")  # Centraliza a imagem dentro do frameLogo
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            messagebox.showerror("Erro", "Não foi possível carregar a imagem do logo.")
            
######## CRIAÇÃO DE MENUS, QUE É OS TRECOS QUE FICA QUASE NO FINAL DA TELA########
    def Menus(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        menubar.add_cascade(label="Opções", menu= filemenu)
        menubar.add_cascade(label="Outros", menu= filemenu2)

        filemenu.add_command(label="Customização")
        filemenu2.add_command(label="Sobre")
        self.Menus()

######## PARTE DA GRADIENTE DE FUNDO BACKGROUND ########
    def criar_gradiente_fundo(self):
        canvas = Canvas(self.window, width=900, height=650)
        canvas.place(relx=0, rely=0)

        # Definindo as cores do gradiente
        laranja_claro = "#FFA500"  # Laranja claro
        laranja_escuro = "#800000"  # Laranja escuro

        # Criando um gradiente vertical com retângulos de cor suave
        for i in range(650):
            color = self.interpolate_color(laranja_claro, laranja_escuro, i / 650)
            canvas.create_line(0, i, 900, i, fill=color)

    def interpolate_color(self, color1, color2, factor):
        """
        Função para interpolar entre duas cores (em formato hexadecimal).
        """
        rgb1 = [int(color1[i:i+2], 16) for i in (1, 3, 5)]
        rgb2 = [int(color2[i:i+2], 16) for i in (1, 3, 5)]
        interpolated_rgb = [int(rgb1[i] + (rgb2[i] - rgb1[i]) * factor) for i in range(3)]
        return f"#{interpolated_rgb[0]:02x}{interpolated_rgb[1]:02x}{interpolated_rgb[2]:02x}"
    
    def tela(self):
        self.window.title("Orange Juice")
        self.window.configure(background="#ec9825")
        self.window.geometry("900x650")
        self.window.resizable(False, False)
    
    def frames_da_tela(self):
        # Barra do topo
        self.frame1 = Frame(self.window, bd=4, bg="White", highlightbackground="Black", highlightthickness=3)
        self.frame1.place(relx=0.1, rely=0.02, relwidth=0.89, relheight=0.12)

        self.frameLogo = Frame(self.window, bd=4, bg="White", highlightbackground="Black", highlightthickness=3)
        self.frameLogo.place(relx=0.01, rely=0.02, relwidth=0.14, relheight=0.50)

        # frame para data e hora
        self.frametime = Frame(self.window, bd=4, bg="#dedada", highlightbackground="Black", highlightthickness=3)
        self.frametime.place(relx=0.15, rely=0.14, relwidth=0.17, relheight=0.07)

        # Frame para os botões de navegação
        self.opitions = Frame(self.window, bd=4, bg="#dedada", highlightbackground="Black", highlightthickness=3)
        self.opitions.place(relx=0.32, rely=0.14, relwidth=0.67, relheight=0.07)

        # Tela principal (onde as informações serão mostradas)
        self.frame2 = Frame(self.window, bd=4, bg="White", highlightbackground="Black", highlightthickness=3)
        self.frame2.place(relx=0.01, rely=0.21, relwidth=0.98, relheight=0.78)

    def widgets(self):
        # Botões de navegação
        Button(self.opitions, text="Conta", font=("Arial", 14), bg="#FF914B", command=self.mostrar_conta).place(relx=0, rely=0, relwidth=0.2, relheight=1)
        Button(self.opitions, text="Novidades", font=("Arial", 14), bg="#FF914B", command=self.mostrar_novidades).place(relx=0.2, rely=0, relwidth=0.2, relheight=1)
        Button(self.opitions, text="Navegação", font=("Arial", 14), bg="#FF914B", command=self.mostrar_navegacao).place(relx=0.4, rely=0, relwidth=0.2, relheight=1)
        Button(self.opitions, text="Biblioteca", font=("Arial", 14), bg="#FF914B", command=self.mostrar_biblioteca).place(relx=0.6, rely=0, relwidth=0.2, relheight=1)
        Button(self.opitions, text="Sair", font=("Arial", 14), bg="red", fg="white", command=self.sair).place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

        # Texto de boas-vindas
        Label(self.frame1, text=f"Bem-vindo(a), {self.usuario_logado}!", bg="White", font=("Arial")).place(relx=0.25, rely=0.025)

        # Conteúdo inicial no frame2
        Label(self.frame2, text="Bem vindo(a) ao site oficial da Orange Juice!", bg="White", font=("Arial", 14)).place(relx=0.3, rely=0.025)


    def mostrar_conta(self):
        self.limpar_frame2()
        Label(self.frame2, text="Sua conta", bg="White", font=("Arial", 16)).place(relx=0, rely=0)

        # FOTO DE PERFIL DO USUÁRIO
        self.image_path = "Profile\default_pfp.jpg"  # Substitua pelo caminho correto da imagem
        try:
            self.image = Image.open(self.image_path)  # Abre a imagem
            self.image = self.image.resize((300, 300))  # Ajuste o tamanho da imagem, se necessário
            self.logo_profile = ImageTk.PhotoImage(self.image)  # Converte a imagem para formato Tkinter

            # Cria um Label no frameLogo para exibir a imagem
            self.label_profile = Label(self.frame2, image=self.logo_profile, highlightbackground="Black", highlightthickness=3)
            self.label_profile.place(relx=0.2, rely=0.4, anchor="center")  # Centraliza a imagem dentro do frameLogo
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            messagebox.showerror("Erro", "Não foi possível carregar a imagem do logo.")
        
        # BOTÃO DE CONFIGURAÇÃO
        self.image_path = "Imagens\config_icon.png"  # Substitua pelo caminho correto da imagem
        self.image = Image.open(self.image_path)  # Abre a imagem
        self.image = self.image.resize((30, 30))  # Ajuste o tamanho da imagem, se necessário
        self.logo_config = ImageTk.PhotoImage(self.image)  # Converte a imagem para formato Tkinter

        # Cria um Label no frameLogo para exibir a imagem
        self.label_config = Button(self.frame2, image=self.logo_config, cursor="hand2")
        self.label_config.place(relx=0.03, rely=0.95, anchor="center")  # Centraliza a imagem dentro do frameLogo

        # NOME DO USUÁRIO APARECENDO NA TELA USUÁRIO
        Label(self.frame2, text=f"{self.usuario_logado}", bg="White", font=("Arial", 25)).place(relx=0.14, rely=0.75)

        # DESCRIÇÃO DO USUÁRIO
        Label(self.frame2, text="Descrição", bg="White", font=("Arial", 25)).place(relx=0.4, rely=0)
        Label(self.frame2, bg="Grey", font=("Arial", 25), highlightbackground="Black", highlightthickness=3).place(relx=0.4
                                                                                                                   , rely=0.1, relwidth=0.3, relheight=0.75)
    def mostrar_novidades(self):
        self.limpar_frame2()
        Label(self.frame2, text="Novidades", bg="White", font=("Arial", 16)).pack(pady=10)
        Label(self.frame2, text="Não há nenhuma novidade, volte mais tarde.",
                  font=("Arial", 12), fg="blue", bg="White").pack(pady=10)
        
    def mostrar_navegacao(self):
        self.limpar_frame2()
        Label(self.frame2, text="Navegação", bg="White", font=("Arial", 16)).place(relx=0,rely=0)
        Search = Entry(self.frame2, font=("Arial", 14))
        Search.place(relx=0,rely=0.1)
        Button(self.frame2, text="Buscar", font=("Arial", 14), bg="#FF914B", cursor="hand2").place(relx=0, rely=0.2)
        Button(self.frame2, text="Limpar", font=("Arial", 14), bg="#FF914B", cursor="hand2").place(relx=0.1, rely=0.2)

    def mostrar_biblioteca(self):
        self.limpar_frame2()
        Label(self.frame2, text="Sua biblioteca", bg="White", font=("Arial", 16)).pack(pady=10)
        Label(self.frame2, text="Você ainda não adquiriu nenhum de nossos produtos.", font=("Arial", 12), fg="blue", bg="White").pack(pady=10)


    def sair(self):
        if messagebox.askyesno("Confirmação", "Tem certeza que quer sair?"):
            limpar_usuario_logado()
            self.window.destroy()
            inicializar()
  
    def limpar_frame2(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

# Inicialização
def inicializar():
    usuario_logado = carregar_usuario_logado()
    if usuario_logado:
        Application(usuario_logado)
    else:
        root = Tk()
        LoginCadastro(root, ao_logar=lambda usuario: (root.destroy(), Application(usuario)))
        root.mainloop()

inicializar()