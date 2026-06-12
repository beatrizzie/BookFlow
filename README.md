📚 BookFlow

Descrição do Projeto

O BookFlow é um sistema de gerenciamento de biblioteca desenvolvido em Python com interface gráfica. O projeto foi criado com o objetivo de automatizar processos de controle de usuários, empréstimos e devoluções de livros, proporcionando maior organização e praticidade na administração de bibliotecas.

O sistema possui dois perfis de acesso: usuário e funcionário. Usuários podem consultar seu histórico de empréstimos, enquanto funcionários podem pesquisar livros, registrar empréstimos e registrar devoluções.

⸻

Funcionalidades

* Cadastro de usuários;
* Cadastro de funcionários;
* Login de usuários;
* Login de funcionários;
* Consulta de livros por meio da API Open Library;
* Pesquisa de livros por título ou palavra-chave;
* Visualização de informações dos livros;
* Registro de empréstimos;
* Registro de devoluções;
* Consulta do histórico de empréstimos;
* Controle de status dos empréstimos;
* Armazenamento dos dados em banco SQLite.

⸻

Tecnologias Utilizadas

* Python 3
* Tkinter
* SQLite
* Requests
* Open Library API
* Git
* GitHub

⸻

Estrutura do Projeto

BookFlow/
│
├── main.py
├── database.py
├── usuario.py
├── usuario_login.py
├── funcionario.py
├── funcionario_login.py
├── busca.py
├── bookflow.db
└── README.md

⸻

Banco de Dados

O sistema utiliza o SQLite como banco de dados local.

Tabelas

Users

* id
* username
* password

Funcionarios

* id
* username
* password

Emprestimos

* id
* usuario_id
* livro
* autor
* ano
* data_emprestimo
* data_entrega
* status

⸻

Requisitos para Execução

Antes de executar o sistema, é necessário possuir:

* Python 3.10 ou superior
* Biblioteca Requests instalada
* Conexão com a internet para consulta de livros na API Open Library

⸻

Instalação

1. Clonar o repositório

git clone https://github.com/beatrizzie/BookFlow.git

2. Entrar na pasta do projeto

cd BookFlow

3. Instalar as dependências

pip install requests

⸻

Execução

Execute o arquivo principal:

python main.py

Após a execução, a tela inicial do sistema será exibida, permitindo o acesso como usuário ou funcionário.

⸻

Metodologia de Desenvolvimento

O projeto foi desenvolvido utilizando a metodologia RAD (Rapid Application Development), baseada em ciclos curtos de planejamento, desenvolvimento e testes. Essa abordagem permitiu a implementação gradual das funcionalidades e a realização de melhorias contínuas ao longo do projeto.

⸻

Integrantes

* Ana Cecília Braz Mayer Magalhães
* Estephany Quirino Lima
* Lailla Beatriz Barros Freire
* Maria Letícia do Nascimento Santos
⸻

Licença

Projeto desenvolvido para fins acadêmicos.
