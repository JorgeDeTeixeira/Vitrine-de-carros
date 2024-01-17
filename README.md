# Vitrine-de-carros

Configuração
Variáveis de Ambiente
SECRET_KEY: Chave secreta para proteger a aplicação contra ataques.
SQLALCHEMY_DATABASE_URI: URL do banco de dados para SQLAlchemy.
Funções Auxiliares
handle_error_and_redirect(route, error_message, redirect_route='index', log_error=True)
Gestão de erros centralizada para redirecionamento e exibição de mensagens.

configure_logging()
Configuração do sistema de logging.

Rotas
Rota Principal (/)
Método: GET
Descrição: Rota principal que renderiza a página inicial.
Rota de Listagem de Carros (/carros)
Método: GET
Descrição: Lista os carros em páginas paginadas.
Parâmetros de Requisição:
pagina: Número da página a ser exibida.
Rota de Visualização de Carro (/carro/<int:carro_id>)
Método: GET
Descrição: Exibe detalhes de um carro específico.
Parâmetros de URL:
carro_id: ID do carro a ser visualizado.
Rota de Adição de Carro (/adicionar)
Métodos: GET, POST
Descrição: Permite a adição de um novo carro ao banco de dados.
Parâmetros de Requisição:
Dados do formulário: Marca, modelo, nome, ano, preço, URL da imagem.
Rota de Edição de Carro (/editar/<int:carro_id>)
Métodos: GET, POST
Descrição: Permite a edição de um carro existente no banco de dados.
Parâmetros de URL:
carro_id: ID do carro a ser editado.
Parâmetros de Requisição:
Dados do formulário: Marca, modelo, nome, ano, preço, URL da imagem.
Rota de Exclusão de Carro (/deletar/<int:carro_id>)
Método: GET
Descrição: Remove um carro do banco de dados.
Parâmetros de URL:
carro_id: ID do carro a ser deletado.
Configuração do Banco de Dados
O modelo de dados está definido em models.py. A tabela Carro possui os seguintes campos:

id: Chave primária.
nome, marca, modelo: Strings representando informações do carro.
ano: Ano de fabricação do carro.
preco: Preço do carro.
img: URL da imagem do carro.
Tratamento de Erros
O tratamento de erros é realizado pela função handle_error_and_redirect.

Execução do Aplicativo
O script app.py inicia o servidor Flask. Ao ser executado diretamente, ele verifica se **name** é igual a '**main**' e, se verdadeiro, inicia o servidor.
