import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext, messagebox
import wikipedia
import threading
from PIL import Image, ImageTk


# Configurar modo escuro por padrão
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("dark-blue")  # "blue", "dark-blue", "green"

class WikipediaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurações da janela
        self.title("Wikipedia Pesquisa")
        self.geometry("1000x700-1920-0")
        self.minsize(800, 700)
        
        # Histórico em memória (quando fecha a aplicação, o histórico é perdido)
        self.historico = []
        
        # Variáveis de controle
        self.current_search = None
        self.is_searching = False
        
        # Criar interface
        self.load_images()
        self.create_interface()
       

    def load_images(self):
        try:
            # Carregar e redimensionar imagens
            logo_wikipedia= Image.open("imgs/wikipedia_logo.png")
            self.logo_photo = ctk.CTkImage(light_image=logo_wikipedia, dark_image=logo_wikipedia, size=(40, 40))

            busca_img = Image.open("imgs/icon_search.png")
            self.busca_foto= ctk.CTkImage(light_image=busca_img, dark_image=busca_img, size=(25, 25))
            
            history_img = Image.open("imgs/icon_history.png")
            self.history_photo = ctk.CTkImage(light_image=history_img, dark_image=history_img, size=(30, 30))
            
            settings_img = Image.open("imgs/icon_settings.png")
            self.settings_photo = ctk.CTkImage(light_image=settings_img, dark_image=settings_img, size=(30, 30))

        except Exception as nome:
            print(f"Erro ao carregar imagens: {nome}")
            self.busca_foto = None
            self.logo_photo = None
            self.history_photo = None
            self.settings_photo = None

    
        
    def create_interface(self):
        """Criar a interface da aplicação"""
        
        # Frame principal com abas
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)
        self.tabview._segmented_button.configure(font=("Segoe UI", 14, "bold"))
        
        # Aba 1: Busca
        self.busca_tab = self.tabview.add("🔍 Busca")
        self.create_busca_aba()
        
        # Aba 2: Histórico
        self.history_tab = self.tabview.add("📜 Histórico")
        ##self.create_historico_aba()
        
        # Aba 3: Configurações
        self.settings_tab = self.tabview.add("⚙️ Configurações")
        ##self.create_configuracoes_aba()
    
    def create_busca_aba(self):

        header_frame = ctk.CTkFrame(self.busca_tab, fg_color="transparent")
        header_frame.pack(fill="x", padx=15, pady=(15, 5))

        self.logo_photo = ctk.CTkLabel(header_frame, image=self.logo_photo, text="")

        self.logo_photo.pack(side="left", padx=(0, 10))

        # Título
        titulo = ctk.CTkLabel(
            header_frame, text="Busca Wikipédia", font=("Segoe UI", 24, "bold")
        )

        titulo.pack(side="left")

        busca_frame = ctk.CTkFrame(self.busca_tab)
        busca_frame.pack(
            fill="x", padx=10, pady=10
        )
        
        # Frame para entrada e botão
        input_frame = ctk.CTkFrame(busca_frame)
        input_frame.pack(fill="x", pady=5)
        
        self.campo_busca = ctk.CTkEntry(
            input_frame,
            placeholder_text="Pesquise algo na Wikipédia... (Ex: O palmeiras é o melhor time do mundo)",
            height=40,
            font=("Segoe UI", 12)
        )
        self.campo_busca.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.campo_busca.bind("<Return>", lambda e: self.search_wikipedia())
        
        # Botão de busca
        busca_btn = ctk.CTkButton(
            input_frame,
            text="Buscar",
            image=self.busca_foto,
            compound="left",
            width=100,
            height=40,
            font=("Segoe UI", 12, "bold")
        )
        busca_btn.pack(side="left")
        
        # Frame para sugestões de busca rápida
        frame_rapido = ctk.CTkFrame(busca_frame, fg_color="transparent")
        frame_rapido.pack(fill="x", pady=10)
        
        texto_rapido = ctk.CTkLabel(frame_rapido, text="Buscas Rápidas:", font=("Segoe UI", 12, "bold"))
        texto_rapido.pack(anchor="w", pady=(0, 5))
        
        botoes_rapidos_frame = ctk.CTkFrame(frame_rapido)
        botoes_rapidos_frame.pack(fill="x")
        
        busca_rapida = ["Python", "Inteligência Artificial", "Brasil", "Palmeiras", "História"]
        for nome_busca in busca_rapida:
            btn = ctk.CTkButton(
                botoes_rapidos_frame,
                text=nome_busca,
                height=32,
                corner_radius=12,
                font=("Arial", 11, "bold"),
                
                hover_color="#144870",
                border_width=1,
                border_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"]
            )

            btn.pack(side="left", padx=4, pady=5)
        
        # Frame para resultados
        resultado_frame = ctk.CTkFrame(self.busca_tab)
        resultado_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Texto de resultado
        self.resultado_texto = scrolledtext.ScrolledText(
            resultado_frame,
            wrap=tk.WORD,
            font=("Segoe UI", 12),
            bg="#1E1E1E",
            fg="#EAEAEA",
            height = 10,
            insertbackground="#FFFFFF", # cor do cursor da barinha de texto
            relief="flat",
            borderwidth=0,
            padx=15,
            pady=10,
            selectbackground="#2563EB", # cor de fundo do texto quando vc copia ele
            selectforeground="white", # cor do texto quando vc copia ele
            spacing1=2,
            spacing2=2,
            spacing3=4
        )

        self.resultado_texto.pack(
            fill="both",
            expand=True,
            
        )
        
        # Frame de botões inferiores
        btn_frame = ctk.CTkFrame(self.busca_tab)
        btn_frame.pack(fill="x", padx=10, pady=10 )
        
        # Botão para copiar
        copy_btn = ctk.CTkButton(
            btn_frame,
            text="📋 Copiar Texto",
            height=30,
            font=("Arial", 12, "bold")
        )
        copy_btn.pack(side="left", padx=5)
        
        # Botão para limpar
        clear_btn = ctk.CTkButton(
            btn_frame,
            text="🗑️ Limpar",
            height=30,
            font=("Arial", 12, "bold")
        )
        clear_btn.pack(side="left", padx=5)
    

if __name__ == "__main__":
    app = WikipediaApp()
    app.mainloop()
