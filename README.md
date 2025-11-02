# HomeHero - Backend Python

Backend do sistema HomeHero convertido de Java (Spring Boot) para Python (FastAPI).

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido para construção de APIs
- **SQLAlchemy**: ORM para Python
- **PyMySQL**: Driver MySQL para Python
- **Uvicorn**: Servidor ASGI para FastAPI

## Estrutura do Projeto

```
home-hero-python/
├── main.py              # Aplicação principal FastAPI
├── config.py             # Configurações do sistema
├── database.py           # Configuração do banco de dados
├── requirements.txt      # Dependências do projeto
├── models/              # Modelos SQLAlchemy
│   ├── __init__.py
│   ├── cliente.py
│   ├── prestador.py
│   ├── empresa.py
│   ├── servico.py
│   ├── agendamento_servico.py
│   └── ... (outros modelos)
└── README.md
```

## Instalação

1. **Instalar dependências:**

```bash
pip install -r requirements.txt
```

2. **Configurar banco de dados:**

Crie um arquivo `.env` na raiz do projeto (opcional, ou configure diretamente no `config.py`):

```env
DATABASE_URL=mysql+pymysql://root:senha@localhost:3306/HomeHero?charset=utf8mb4
```

3. **Executar a aplicação:**

```bash
python main.py
```

Ou usando uvicorn diretamente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. **Acessar a documentação da API:**

Após iniciar o servidor, acesse:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Modelos de Dados

O sistema possui os seguintes modelos principais:

- **Cliente**: Clientes do sistema
- **Prestador**: Prestadores de serviço
- **Empresa**: Empresas prestadoras
- **Servico**: Serviços oferecidos
- **AgendamentoServico**: Agendamentos de serviços
- **Avaliacao**: Avaliações dos serviços
- **Pagamento**: Pagamentos
- **Notificacao**: Notificações do sistema
- **Endereco**: Endereços
- E outros modelos relacionados

## Event Listeners

Os seguintes eventos foram convertidos dos listeners Java:

1. **AgendamentoServicoListener**: 
   - Cria histórico de status ao inserir novo agendamento
   - Registra mudanças de status do agendamento

2. **AvaliacaoListener**:
   - Cria notificação quando uma avaliação é registrada

## Conversão de Java para Python

### Principais mudanças:

- **JPA/Hibernate → SQLAlchemy**: Conversão dos modelos JPA para SQLAlchemy
- **Spring Boot → FastAPI**: Framework web convertido
- **@EntityListeners → @event.listens_for**: Event listeners convertidos para eventos SQLAlchemy
- **Repository Pattern**: Pode ser implementado conforme necessidade usando SQLAlchemy Sessions

## Banco de Dados

O sistema utiliza MySQL como banco de dados. Certifique-se de que:

1. O MySQL está instalado e rodando
2. O banco de dados `HomeHero` existe (ou será criado automaticamente se configurado)
3. As credenciais de acesso estão corretas no arquivo de configuração

## Desenvolvimento

Para adicionar novas rotas e endpoints, edite o arquivo `main.py` e crie os controllers conforme necessário.

## Observações

- Os listeners Java foram convertidos para eventos SQLAlchemy
- As relações JPA foram convertidas para relações SQLAlchemy
- O comportamento de cascade e lazy loading foi mantido onde possível

