# API de Gerenciamento de Tarefas

Uma API REST simples para gerenciamento de tarefas, construída com Flask e frontend em HTML/CSS/JavaScript.

## Estrutura do Projeto

```
api-tarefas/
├── src/
│   ├── backend/
│   │   ├── config/
│   │   │   └── config.py
│   │   ├── controllers/
│   │   │   └── tarefa_controller.py
│   │   ├── models/
│   │   │   └── tarefa.py
│   │   ├── routes/
│   │   │   └── tarefa_routes.py
│   │   └── app.py
│   └── frontend/
│       ├── static/
│       │   ├── css/
│       │   │   └── style.css
│       │   └── js/
│       │       └── main.js
│       └── templates/
│           └── index.html
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o Projeto

1. Inicie o servidor:
   ```bash
   python src/backend/app.py
   ```
2. Acesse a aplicação em `http://localhost:5000`

## Endpoints da API

- `GET /tarefas` - Lista todas as tarefas
- `POST /tarefas` - Cria uma nova tarefa
- `DELETE /tarefas/<id>` - Remove uma tarefa específica

## Tecnologias Utilizadas

- Backend:
  - Flask (Framework Python)
  - Flask-CORS (Cross-Origin Resource Sharing)
- Frontend:
  - HTML5
  - CSS3
  - JavaScript (Vanilla)
