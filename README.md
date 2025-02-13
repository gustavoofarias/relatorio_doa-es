Relatório de Doações

Este projeto permite gerar relatórios personalizados com base em dados de doações, igrejas, saques e usuários. Ele oferece uma interface simples para escolher tabelas, colunas, filtros, ordenação e paginação.

## Requisitos
- Python 3.8 ou superior.
- Bibliotecas listadas no requirements.txt.
- Acesso a um banco de dados PostgreSQL com as tabelas necessárias.

## Instalação
### Clone o repositório:
```bash
git clone https://github.com/seu-usuario/relatorio-doacoes.git
cd relatorio-doacoes
```

### Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Configure o banco de dados:
Edite o arquivo `codigo_fonte/database.py` e insira as credenciais do seu banco de dados PostgreSQL.

## Como Usar
### Executando o Projeto
Execute o arquivo `main.py`:
```bash
python main.py
```

Siga as instruções no menu interativo:
1. Escolha a tabela para o relatório.
2. Selecione as colunas desejadas.
3. Aplique filtros personalizados.
4. Defina a ordenação e a paginação.
5. O relatório será salvo em um arquivo JSON no diretório raiz.

### Exemplo de Uso
#### Menu Inicial:
```
Escolha a tabela para o relatório:
1. Doações (donations)
2. Igrejas (churches)
3. Saques (withdrawals)
4. Usuários (users)
5. Sair
Digite o número da opção desejada: 1
```

#### Seleção de Colunas:
```
Colunas disponíveis para a tabela 'donations': id, amount, payment_method, status, created_at, user_id, church_id
Digite as colunas desejadas (separadas por vírgula): id, amount, status, created_at
```

#### Filtros Personalizados:
```
--- Filtros Personalizados ---
Digite o nome da coluna para filtrar (ou deixe em branco para parar): status
Digite o valor para filtrar na coluna 'status': approved
Digite o nome da coluna para filtrar (ou deixe em branco para parar):
```

#### Ordenação e Paginação:
```
Digite a coluna para ordenação (ex.: 'created_at DESC'): created_at DESC
Digite o número máximo de registros por página: 10
Digite o número de registros a ignorar (offset): 0
```

Saída:
```
O relatório será salvo em relatorio_donations.json.
```

## Estrutura do Projeto
```
relatorio_doacoes/
│── codigo_fonte/
│   ├── __init__.py
│   ├── database.py        # Configuração da conexão com o banco
│   ├── repository.py      # Funções de acesso ao banco de dados
│   ├── services.py        # Lógica de filtragem e paginação
│
│── testes/
│   ├── test_repository.py # Testes para consultas ao banco
│   ├── test_services.py   # Testes para lógica de filtragem
│
│── main.py                # Ponto de entrada do sistema
│── requirements.txt       # Dependências do projeto
│── README.md              # Documentação
│── .gitignore             # Arquivos ignorados pelo Git
```

## Tabelas e Colunas Disponíveis
### Doações (donations):
- id
- amount
- payment_method
- status
- created_at
- user_id
- church_id

### Igrejas (churches):
- id
- name
- cnpj
- manager_id
- created_at

### Saques (withdrawals):
- id
- amount
- status
- created_at
- manager_id

### Usuários (users):
- id
- full_name
- email
- created_at

## Personalização
### Adicionar Novos Relatórios
1. Crie uma nova função no `repository.py` para buscar os dados.
2. Adicione um novo método no `services.py` para processar os dados.
3. Atualize o menu no `main.py` para incluir a nova opção.

### Modificar Filtros
Edite o dicionário `filters` no `main.py` para adicionar ou remover filtros.

## Testes
Para executar os testes, use o comando:
```bash
python -m unittest discover testes
```

