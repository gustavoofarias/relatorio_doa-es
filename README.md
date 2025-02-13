Relatório de Doações com Paginação e Filtros
Este projeto permite gerar relatórios de doações com base em filtros personalizados e paginação. Ele se conecta a um banco de dados PostgreSQL, consulta as doações associadas a um manager_id e retorna os resultados no formato JSON.

Requisitos
Python 3.8 ou superior.

Bibliotecas Python: psycopg2 e Flask (opcional para API).

Banco de dados PostgreSQL com as tabelas necessárias (donations, users, churches, managers).

Instalação
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/relatorio-doacoes.git
cd relatorio-doacoes
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o banco de dados:

Edite o arquivo `database.py` e atualize as credenciais do banco de dados:

```python
self.connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dbname="dizimei",
    user="gustavo",
    password="IlK5qZ54429Q",
    host="dizimei-dev.cbeoqj4emryb.us-east-1.rds.amazonaws.com",
    port=5432,
)
```

Como Usar
### 1. Interface de Linha de Comando (main.py)
Execute o script `main.py` para usar a interface de linha de comando:

```bash
python main.py
```

#### Passo a Passo
**Menu Inicial:**

```
--- Relatório de Doações ---
1. Buscar Doações
2. Sair
Digite o número da opção desejada:
```
Digite `1` e pressione Enter.

**Inserir o Manager ID:**

```
Digite o ID do manager:
```
Digite o ID do manager (ex.: 1) e pressione Enter.

**Inserir Filtros:**

```
--- Filtros Personalizados ---
Data inicial (YYYY-MM-DD, deixe em branco para ignorar):
```
Insira os filtros desejados ou deixe em branco para ignorar.

**Resultados:**

Os resultados serão exibidos no terminal no formato JSON.

Você pode optar por salvar os resultados em um arquivo JSON.

**Exemplo de Uso**

```
Digite o número da opção desejada: 1
Digite o ID do manager: 1

--- Filtros Personalizados ---
Data inicial (YYYY-MM-DD, deixe em branco para ignorar): 2023-01-01
Data final (YYYY-MM-DD, deixe em branco para ignorar): 2023-12-31
Método de pagamento (deixe em branco para ignorar): credit-card
Status (deixe em branco para ignorar): approved
Busca livre (nome, e-mail ou igreja, deixe em branco para ignorar): João
Número máximo de registros por página: 5
Número de registros a ignorar (offset): 0

--- Resultados ---
{
    "total": 18,
    "page": 1,
    "limit": 5,
    "donations": [
        {
            "id": 37,
            "createdAt": "2025-02-03T21:20:46.591Z",
            "netAmountChurch": "1.84",
            "status": "approved",
            "paymentMethod": "credit-card",
            "church": {
                "id": 1,
                "name": "Igreja Nova Missão",
                "username": "igreja-nova-esperanca"
            },
            "user": {
                "id": 2,
                "name": "Kalebe Almeida",
                "email": "kalebe.nathanael181@gmail.com"
            }
        }
    ]
}

Deseja salvar os resultados em um arquivo JSON? (s/n): s
Digite o nome do arquivo (ex.: relatorio.json): relatorio_doacoes.json
Relatório salvo em 'relatorio_doacoes.json'.
```

### 2. API RESTful (api.py)
Execute o script `api.py` para iniciar a API Flask:

```bash
python api.py
```

A API estará disponível em `http://localhost:5000`.

**Rotas Disponíveis**

`GET /donations`: Retorna as doações filtradas e paginadas.

**Parâmetros da Rota**

| Parâmetro        | Descrição |
|------------------|-------------|
| manager_id      | ID do manager (obrigatório). |
| start_date      | Data inicial no formato YYYY-MM-DD (opcional). |
| end_date        | Data final no formato YYYY-MM-DD (opcional). |
| payment_method  | Método de pagamento (ex.: credit-card, pix) (opcional). |
| status         | Status da doação (ex.: approved, pending, rejected) (opcional). |
| search_text     | Texto para busca livre (nome, e-mail ou igreja) (opcional). |
| limit          | Número máximo de registros por página (padrão: 10). |
| offset         | Número de registros a ignorar (padrão: 0). |

**Exemplo de Requisição**

```bash
curl "http://localhost:5000/donations?manager_id=1&start_date=2023-01-01&end_date=2023-12-31&payment_method=credit-card&status=approved&search_text=João&limit=5&offset=0"
```

**Resposta da API**

```json
{
    "total": 18,
    "page": 1,
    "limit": 5,
    "donations": [
        {
            "id": 37,
            "createdAt": "2025-02-03T21:20:46.591Z",
            "netAmountChurch": "1.84",
            "status": "approved",
            "paymentMethod": "credit-card",
            "church": {
                "id": 1,
                "name": "Igreja Nova Missão",
                "username": "igreja-nova-esperanca"
            },
            "user": {
                "id": 2,
                "name": "Kalebe Almeida",
                "email": "kalebe.nathanael181@gmail.com"
            }
        }
    ]
}
```

**Estrutura do Projeto**

```
relatorio_doacoes/
│── codigo_fonte/
│   ├── __init__.py
│   ├── database.py        # Configuração da conexão com o banco
│   ├── repository.py      # Funções de acesso ao banco de dados
│   ├── services.py        # Lógica de filtragem e paginação
│── testes/
│   ├── test_repository.py # Testes para consultas ao banco
│   ├── test_services.py   # Testes para lógica de filtragem
│── main.py                # Ponto de entrada do sistema (CLI)
│── api.py                 # Ponto de entrada da API
│── requirements.txt       # Dependências do projeto
│── README.md              # Documentação
│── .gitignore             # Arquivos ignorados pelo Git
```

