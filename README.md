# Vitrine de Carros - Documentação

Este projeto é uma aplicação web básica construída com Flask, SQLAlchemy e WTForms para gerenciar uma vitrine de carros. Ele permite a exibição, adição, edição e exclusão de informações sobre carros.

## Funcionalidades Principais

### Listagem Paginada de Carros
- **Rota:** `/carros`
- **Descrição:** Exibe uma lista paginada de carros, permitindo navegar pelas diferentes páginas.

### Visualização Detalhada de Informações de um Carro Específico
- **Rota:** `/carro/<int:carro_id>`
- **Descrição:** Mostra informações detalhadas sobre um carro específico com base no seu ID.

### Adição de Novos Carros
- **Rota:** `/adicionar`
- **Descrição:** Permite adicionar novos carros ao banco de dados. Utiliza um formulário para inserir dados como marca, modelo, nome, ano, preço e URL da imagem.

### Edição de Informações de Carros Existentes
- **Rota:** `/editar/<int:carro_id>`
- **Descrição:** Permite a edição de informações de um carro existente. Utiliza um formulário preenchido com os dados atuais do carro.

### Exclusão de Carros do Banco de Dados
- **Rota:** `/deletar/<int:carro_id>`
- **Descrição:** Remove um carro específico do banco de dados.

## Estrutura do Projeto


## Requisitos do Sistema

- Python 3.x
- Flask
- Flask-WTF
- SQLAlchemy
- python-decouple

## Configuração do Ambiente

### Variáveis de Ambiente

- `SECRET_KEY`: Chave secreta para proteger a aplicação contra ataques.
- `SQLALCHEMY_DATABASE_URI`: URL do banco de dados para SQLAlchemy.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/vitrine-de-carros.git
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente.

6. Execute o aplicativo:

    ```bash
    python app.py
    ```

Acesse a aplicação em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Como Usar

1. Acesse a página inicial para visualizar a vitrine de carros.

2. Clique em "Adicionar Carro" para incluir um novo carro.

3. Explore as opções de edição e exclusão disponíveis para cada carro.

## Contribuição

Se desejar contribuir com melhorias ou correções, sinta-se à vontade para enviar um pull request. Consulte as diretrizes de contribuição no [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
