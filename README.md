# 📚 Wikipedia Search Desktop App

Um aplicativo de desktop moderno e intuitivo para buscar informações na Wikipédia, desenvolvido com **Python**, **CustomTkinter** e **Wikipedia API**.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)![License](https://img.shields.io/badge/License-MIT-green.svg)![Status](https://img.shields.io/badge/Status-Ativo-brightgreen.svg)

---

## 🎯 Características Principais

✨ **Busca Rápida** - Busque artigos da Wikipédia em tempo real📜 **Histórico** - Acompanhe todas as suas buscas anteriores🎨 **Interface Moderna** - Design limpo com CustomTkinter🌙 **Tema Escuro/Claro** - Alterne entre temas conforme preferência🎭 **Múltiplas Cores** - Escolha entre 5 cores de tema diferentes⚡ **Ícones Renderizados** - Ícones bonitos gerados com PIL🔍 **Buscas Rápidas** - Botões de atalho para termos populares📋 **Copiar Texto** - Copie facilmente os resultados para a área de transferência

---

## 📋 Requisitos

- **Python 3.7+**

- **pip** (gerenciador de pacotes Python)

- **Conexão com Internet** (para buscar na Wikipédia)

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/wikipedia-search-app.git
cd wikipedia-search-app
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install customtkinter wikipedia pillow
```

---

## 💻 Como Usar

### Executar o aplicativo

```bash
python wikipedia_app.py
```

Ou com Python 3.11+:

```bash
python3 wikipedia_app.py
```

### Interface

O aplicativo possui **3 abas principais**:

#### 🔍 **Aba Busca**

- Digite um termo na caixa de entrada

- Clique em "🔍 Buscar" ou pressione **Enter**

- Veja o resumo do artigo da Wikipédia

- Use os botões de **Buscas Rápidas** para termos populares

- Copie o texto com o botão "📋 Copiar Texto"

#### 📜 **Aba Histórico**

- Veja todas as suas buscas anteriores

- Clique em "🔍" para refazer uma busca

- Limpe o histórico com o botão "🗑️ Limpar Histórico"

#### ⚙️ **Aba Configurações**

- Altere o **Tema** (Escuro, Claro, Sistema )

- Escolha a **Cor do Tema** (Azul, Verde, Vermelho, Roxo, Laranja)

- Veja informações sobre o aplicativo

---

## 📁 Estrutura do Projeto

```
wikipedia-search-app/
├── wikipedia_app.py          # Arquivo principal do aplicativo
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
├── LICENSE                   # Licença MIT
├── .gitignore                # Arquivos ignorados no Git
├── CONTRIBUTING.md           # Guia de contribuição
└── imgs/                     # Pasta com ícones
    ├── search.png            # Ícone de busca
    ├── history.png           # Ícone de histórico
    └── settings.png          # Ícone de configurações
```

---

## 🔧 Dependências

| Pacote | Versão | Descrição |
| --- | --- | --- |
| **customtkinter** | 5.0+ | Interface gráfica moderna |
| **wikipedia** | 1.4+ | API da Wikipédia |
| **pillow** | 9.0+ | Processamento de imagens |

---

## 📖 Guia Detalhado

### Buscar um Artigo

1. Abra a aba **"🔍 Busca"**

1. Digite um termo (ex: "Python", "Inteligência Artificial")

1. Clique em "🔍 Buscar" ou pressione **Enter**

1. O resumo do artigo aparecerá abaixo

### Usar Buscas Rápidas

Clique em um dos botões pré-configurados:

- 🐍 **Python** - Linguagem de programação

- 🤖 **Inteligência Artificial** - IA e Machine Learning

- 🇧🇷 **Brasil** - País e história

- Palmeiras - O melhor time

- 📚 **História** - Ciência histórica

### Gerenciar Histórico

1. Abra a aba **"📜 Histórico"**

1. Veja todas as suas buscas anteriores

1. Clique em "🔍" para refazer uma busca

1. Use "🗑️ Limpar Histórico" para apagar tudo

### Personalizar Tema

1. Abra a aba **"⚙️ Configurações"**

1. Selecione o **Tema**: Dark, Light ou System

1. Escolha a **Cor**: Blue, Green, Red, Purple ou Orange

1. As mudanças são aplicadas imediatamente

---

## 🎨 Ícones da Pasta `imgs/`

O aplicativo carrega ícones PNG da pasta `imgs/`:

| Arquivo | Descrição | Tamanho Recomendado |
| --- | --- | --- |
| `search.png` | Ícone de Busca (Lupa) | 60x60px ou maior |
| `history.png` | Ícone de Histórico (Livro) | 60x60px ou maior |
| `settings.png` | Ícone de Configurações (Engrenagem) | 60x60px ou maior |

**Nota:** Os ícones são redimensionados automaticamente para 60x60px. Use imagens com fundo transparente para melhor resultado!

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'customtkinter'"

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Erro: "No module named 'wikipedia'"

Instale o pacote wikipedia:

```bash
pip install wikipedia
```

### Erro: "No module named 'PIL'"

Instale o Pillow:

```bash
pip install pillow
```

### A interface não aparece

Verifique se você tem uma versão compatível do Python:

```bash
python --version
```

Deve ser **Python 3.7+**

### Erro de conexão com Wikipédia

- Verifique sua **conexão com Internet**

- A Wikipédia pode estar temporariamente indisponível

- Tente novamente em alguns momentos

---

## 💡 Exemplos de Uso

### Buscar sobre Python

```
1. Digite "Python" na caixa de entrada
2. Clique em "🔍 Buscar"
3. Veja o resumo sobre a linguagem Python
4. Copie o texto se necessário
```

### Explorar o Histórico

```
1. Vá para a aba "📜 Histórico"
2. Veja todas as suas buscas anteriores
3. Clique em "🔍" para refazer uma busca
4. Use "🗑️ Limpar Histórico" para começar do zero
```

### Personalizar Aparência

```
1. Abra "⚙️ Configurações"
2. Mude para "Light" para tema claro
3. Escolha "Purple" para cor roxa
4. Aproveite a nova aparência!
```

---

## 🔐 Privacidade

- ✅ **Sem rastreamento** - O aplicativo não coleta dados

- ✅ **Sem conexões externas** - Apenas busca na Wikipédia

- ✅ **Histórico local** - Dados armazenados apenas em memória

- ✅ **Open Source** - Código aberto para inspeção

---

## 📝 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🐛 Reportar Bugs

Se encontrar um bug, por favor abra uma **Issue** no GitHub com:

- Descrição do problema

- Passos para reproduzir

- Versão do Python

- Sistema operacional

- Screenshot (se aplicável)

## 📚 Recursos Úteis

- [CustomTkinter Docs](https://github.com/TomSchimansky/CustomTkinter)

- [Wikipedia API Docs](https://wikipedia.readthedocs.io/)

- [Pillow Docs](https://pillow.readthedocs.io/)

- [Python Docs](https://docs.python.org/3/)

---

## 👨‍💻 Autor

Desenvolvido lazari usando Python

---

## 📞 Suporte

Se tiver dúvidas ou sugestões:

1. Abra uma **Issue** no GitHub

1. Deixe um **comentário** em uma Pull Request

1. Verifique a seção **Troubleshooting** acima

---

## 🎉 Agradecimentos

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Interface moderna

- [Wikipedia](https://www.wikipedia.org/) - Fonte de conhecimento

- [Python Community](https://www.python.org/) - Comunidade incrível

---

## 📊 Estatísticas

- **Linhas de Código**: ~400

- **Dependências**: 3

- **Versão**: 5.0

- **Status**: ✅ Ativo e Mantido

---

## 🌟 Se Gostou, Deixe uma Star ⭐

Se este projeto foi útil para você, considere deixar uma **star** no GitHub! Isso ajuda a projeto a crescer e alcançar mais pessoas.

---

**Desenvolvido com Python 🐍 | CustomTkinter 🎨 | Wikipedia API 📚**

