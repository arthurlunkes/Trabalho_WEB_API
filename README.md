# Trabalho_WEB_API

## Descrição

Repositório que será utilizado para o Trabalho de WEB

## Integrantes do grupo

- Mateus Veroneze 

- Arthur lunkes

- Lucas Loeffler 

## Descrição do projeto

### MAIN:

Importa módulos e funções necessárias.
Define um gerenciador de contexto assíncrono (lifespan) para gerenciar o ciclo de vida do banco de dados.
Cria uma aplicação FastAPI (app) com o parâmetro lifespan.
Inclui dois roteadores (provas_router e resultados_router) usando app.include_router.
Define uma rota de verificação de status de saúde (/healthcheck).

### CONFIG:

Configura a conexão com o banco de dados usando sqlmodel e create_engine.
Define funções para criar o banco de dados e tabelas, obter o motor do banco de dados e criar uma sessão.

### PROVAS_ROUTES:

Importa módulos e modelos necessários.
Cria um roteador (provas_router) com o prefixo "/provas".
Define rotas para criar uma nova "Prova" e excluir uma "Prova" pelo ID.

### RESULTADOS_ROUTES:

Importa módulos, modelos necessários e logging.
Cria um roteador (resultados_router) com o prefixo "/resultados".
Define rotas para adicionar um novo "Resultado" a uma "Prova", obter resultados para uma "Prova" pelo ID e atualizar respostas para um resultado específico.
Em resumo, esse código define uma aplicação FastAPI com rotas para gerenciar provas (provas_router) e seus resultados (resultados_router). Ele utiliza um banco de dados PostgreSQL com sqlmodel para armazenamento e recuperação de dados. A aplicação segue os princípios RESTful API para criar, obter, atualizar e excluir recursos.