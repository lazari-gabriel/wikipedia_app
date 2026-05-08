import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext, messagebox
import wikipedia
import threading
from PIL import Image, ImageTk


# Configurar modo escuro por padrão
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("dark-blue")  # "blue", "dark-blue", "green"
wikipedia.set_lang("pt")

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
        self.busca_atual = None
        self.buscando = False
        
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
        self.campo_busca.bind("<Return>", lambda e: self.busca_wikipedia())
        
        # Botão de busca
        busca_btn = ctk.CTkButton(
            input_frame,
            text="Buscar",
            image=self.busca_foto,
            compound="left",
            width=100,
            height=40,
            font=("Segoe UI", 12, "bold"),
            command=self.busca_wikipedia
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
                #command=lambda termo=nome_busca:,
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
        copiar_btn = ctk.CTkButton(
            btn_frame,
            text="📋 Copiar Texto",
            height=30,
            font=("Arial", 12, "bold")
        )
        copiar_btn.pack(side="left", padx=5)
        
        # Botão para limpar
        clear_btn = ctk.CTkButton(
            btn_frame,
            text="🗑️ Limpar",
            height=30,
            font=("Arial", 12, "bold")
        )
        clear_btn.pack(side="left", padx=5)
    

    def busca_wikipedia(self):
        """Buscar na Wikipédia"""
        texto_busca = self.campo_busca.get().strip()
        
        if not texto_busca:
            messagebox.showwarning("Aviso", "Digite um termo para buscar!")
            return
        
        if self.buscando:
            messagebox.showinfo("Aviso", "Uma busca já está em andamento...")
            return
        
        # Executar busca em thread separada para não congelar a UI
        thread = threading.Thread(target=self.realizar_busca, args=(texto_busca,))
        thread.daemon = True
        thread.start()

    def realizar_busca(self, busca_termo):
        """Realizar a busca (em thread separada)"""
        self.buscando = True
        self.resultado_texto.delete("1.0", tk.END)
        self.resultado_texto.insert("1.0", "🔄 Buscando...\n")
        
        try:
            # Buscar na Wikipédia
            resultados = wikipedia.search(busca_termo, results=5)
            
            if not resultados:
                self.resultado_texto.delete("1.0", tk.END)
                self.resultado_texto.insert("1.0", "❌ Nenhum resultado encontrado para: " + busca_termo)
                return
            
            # Obter o primeiro resultado
            page = wikipedia.page(resultado[0])
            
            # Adicionar ao histórico em teste
            #self.add_to_history(page.title)
            
            # Armazenar busca atual
            self.busca_atual = {
                "title": page.title,
                "url": page.url,
                "summary": page.summary
            }
            
            # Exibir resultado
            resultado_texto = f"📖 TÍTULO: {page.title}\n"
            resultado_texto += f"🔗 URL: {page.url}\n"
            resultado_texto += "=" * 80 + "\n\n"
            resultado_texto += f"RESUMO:\n{page.summary}\n\n"
            resultado_texto += "=" * 80 + "\n"
            resultado_texto += f"\n📚 Outros resultados encontrados:\n"
            
            contador = 1

            for resultado in resultados[1:]: 
                resultado_texto += f"{contador}. {resultado}\n"
                contador += 1

           # for i, result in enumerate(resultado[1:], 1): # Começa do segundo resultado, enumerate começa do 1
                #resultado_texto += f"{i}. {result}\n"
            
            self.resultado_texto.delete("1.0", tk.END)
            self.resultado_texto.insert("1.0", resultado_texto)
        
        except wikipedia.exceptions.PageError:
            self.resultado_texto.delete("1.0", tk.END)
            self.resultado_texto.insert("1.0", f"❌ Página não encontrada para: {busca_termo}")
        
        except Exception as e:
            self.resultado_texto.delete("1.0", tk.END)
            self.resultado_texto.insert("1.0", f"❌ Erro ao buscar: {str(e)}")
        
        finally:
            self.buscando = False  

    def copiar_texto(self):
    #     try:
    #         texto = self.resultado_texto.get("1.0", tk.END).strip()
    #         if texto:
                
    #         else:
               


if __name__ == "__main__":
    app = WikipediaApp()
    app.mainloop()
