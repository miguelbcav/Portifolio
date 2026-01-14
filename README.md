# Portfólio Flet

Este é um portfólio interativo desenvolvido utilizando **Flet**, uma biblioteca para criação de interfaces gráficas com **Python**. O portfólio apresenta uma estrutura responsiva que se adapta a diferentes tamanhos de tela (como dispositivos móveis e desktops). A interface conta com uma barra lateral para navegação e uma área principal para exibir o conteúdo.

## 🚀 Funcionalidades

- **Barra Lateral (Sidebar)**: Apresenta uma navegação responsiva para facilitar a experiência do usuário.
- **Conteúdo Responsivo**: A área principal é adaptável, mostrando conteúdo relevante do portfólio de acordo com a navegação.
- **Tema Escuro**: O aplicativo utiliza um tema escuro moderno, com cores de fundo e texto ajustadas para uma visualização agradável.
- **Responsividade**: O layout se ajusta de forma dinâmica a diferentes tamanhos de tela, oferecendo uma experiência consistente em dispositivos móveis e desktops.

## 📋 Pré-requisitos

Para rodar o projeto, você precisará do seguinte:

- **Python 3.8+**
- **Flet**: A biblioteca principal utilizada para criar a interface.

## 🛠️ Como rodar o projeto

### Passo 1: Clone o repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/portfolio-flet.git
cd portfolio-flet
Passo 2: Crie e ative um ambiente virtual (opcional, mas recomendado)
Crie um ambiente virtual para isolar as dependências do projeto:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

No Windows:
bash
Copiar código
.\venv\Scripts\activate
No Linux/MacOS:
bash
Copiar código
source venv/bin/activate
Passo 3: Instale as dependências
Instale o Flet (e outras dependências, se houver) utilizando o comando:

bash
Copiar código
pip install flet
Passo 4: Execute a aplicação
Para iniciar a aplicação, basta rodar o seguinte comando:

bash
Copiar código
python main.py
O aplicativo será aberto em seu navegador no endereço http://localhost:8501.

🖥️ Como funciona
A aplicação é composta por duas partes principais:

Sidebar: Uma barra lateral que pode conter links ou informações de navegação para diferentes seções do portfólio.
Conteúdo (Conteudo): A área principal que exibe as informações de acordo com a navegação feita pelo usuário.
Estrutura Responsiva
Desktop (>= 1024px): A barra lateral ocupa uma largura fixa enquanto o conteúdo se adapta ao restante da tela.
Móvel (<= 1024px): O layout se adapta para uma visão mais compacta, onde a barra lateral pode ser ocultada ou minimizada.
Tema Escuro
A aplicação usa o modo de tema escuro para uma melhor experiência visual, especialmente em ambientes com pouca luz. A configuração do tema é feita através da classe AppTheme.

🎨 Personalização
Você pode personalizar a aparência da aplicação modificando o tema na classe AppTheme. Para mudar as cores, fontes, ou qualquer outro estilo, altere os parâmetros dentro de AppTheme para se adequar à sua identidade visual.

Além disso, o conteúdo da aplicação (como a barra lateral e a área de conteúdo) pode ser facilmente modificado para incluir informações, projetos e links do seu portfólio.

📂 Estrutura do Projeto
A estrutura do projeto é a seguinte:

bash
Copiar código
portfolio-flet/
│
├── .github/                # Diretório para configurações de CI/CD
│   └── workflows/          # Arquivos de workflows do GitHub Actions
│       └── deploy-github-pages.yml  # Workflow de deploy para GitHub Pages
│
├── assets/                 # Recursos como imagens, ícones e outros
│   └── (Arquivos de imagem e recursos estáticos)
│
├── components/             # Componentes reutilizáveis ou módulos
│   └── (Arquivos de componentes adicionais)
│
├── dist/                   # Diretório para arquivos distribuídos ou gerados após build
│   └── dist web/           # Arquivos gerados para a versão web do projeto
│
├── partials/               # Arquivos de partes da interface (como sidebar e conteúdo)
│   └── (Arquivos do portfólio)
│
├── main.py                 # Código principal da aplicação Flet
│
├── requirements.txt        # Arquivo de dependências do Python
│
└── README.md               # Documentação do projeto

📝 Licença
Este projeto está licenciado sob a MIT License.

### Explicação das partes do código

- **Classe `AppTheme`**: Define o tema escuro da aplicação, com cores personalizadas para o fundo, texto e superfícies.
- **Classe `App`**: Cria a página principal, definindo a estrutura do layout com a barra lateral e a área de conteúdo. A responsividade é gerida por meio de uma `ResponsiveRow`, que ajusta os componentes conforme o tamanho da tela.
- **`Sidebar` e `Conteudo`**: São importados de arquivos separando a lógica de cada um desses componentes, permitindo uma maior modularização do código.

### Passos adicionais

- **Personalizar a Sidebar**: Você pode alterar a `Sidebar` para incluir links de navegação ou informações adicionais sobre seus projetos.
- **Alterar o Conteúdo**: A classe `Conteudo` pode ser editada para mostrar diferentes seções do seu portfólio, como projetos, habilidades, ou links para redes sociais.

Isso deverá te ajudar a configurar e personalizar o seu portfólio de forma fácil. Se tiver mais dúvidas ou quiser expandir o projeto, sinta-se à vontade para perguntar!

💬 Como Contribuir Faça um fork do repositório. Crie uma nova branch (git checkout -b minha-contribuicao). Faça suas modificações e commit. Push para a branch (git push origin minha-contribuicao). Abra uma pull request. 📚 Mais Informações 🎓 Curso FLET 360 Python: Aprofunde-se no Python e na construção de interfaces gráficas com o Flet! 👉 https://go.hotmart.com/J91353466S?dp=1
