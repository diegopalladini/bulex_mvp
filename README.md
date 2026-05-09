# 💊 Bulex MVP

Protótipo funcional de um aplicativo de leitura de bulas de medicamentos via QR Code, desenvolvido como Prova de Conceito (PoC) para a disciplina de Projeto Integrador, do curso de Análise e Desenvolvimento de Sistemas.

---

## 🎯 Jornada do Usuário

**Persona:** Sr. João, 67 anos, hipertenso, dificuldade de leitura de textos pequenos.

**Problema:** Bulas de medicamentos são difíceis de ler — letra pequena, linguagem técnica, informações desorganizadas.

**Solução:** O usuário escaneia o QR Code da embalagem e recebe as informações do medicamento de forma clara, acessível e com tipografia ampliada.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|------------|
| Front-end | HTML5, CSS3, Jinja2 Templates |
| Back-end | Python 3, FastAPI |
| Banco de Dados | SQLite3 |
| Servidor | Uvicorn (ASGI) |

---

## 📁 Estrutura do Projeto

```
bulex_mvp/
├── main.py          # Aplicação FastAPI (rotas e lógica)
├── database.py      # Criação e seed do banco de dados
├── bulex.db         # Banco de dados SQLite (gerado automaticamente)
└── templates/
    ├── index.html   # Tela inicial (simulador de QR Code)
    └── bula.html    # Tela de exibição da bula
```

---

## ▶️ Como Rodar o Projeto

### Pré-requisitos

- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/bulex_mvp.git
cd bulex_mvp

# Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install fastapi uvicorn jinja2
```

### Executando

```bash
# 1. Crie o banco de dados com os dados iniciais
python database.py

# 2. Suba o servidor
uvicorn main:app --reload
```

Acesse no navegador: **http://127.0.0.1:8000**
ou na web: **https://bulex-mvp.onrender.com**

---

## 🗺️ Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Tela inicial (simulador de QR Code) |
| GET | `/medicamento/{id}` | Exibe a bula do medicamento pelo ID |

---

## 💾 Modelagem de Dados

**Tabela: `medicamentos`**

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | INTEGER (PK) | Identificador único |
| `nome` | TEXT | Nome do medicamento |
| `finalidade` | TEXT | Para que serve |
| `como_tomar` | TEXT | Posologia |
| `alerta` | TEXT | Sinais de alerta / efeitos colaterais |

**Dados de teste incluídos:**
- ID 1 → Losartana Potássica
- ID 2 → Amoxicilina
- ID 3 → Dipirona

---

## 📌 Observações

- Este é um protótipo funcional. A leitura de QR Code é simulada por um campo de entrada manual de ID.
- O banco de dados é criado automaticamente na primeira execução via `lifespan` do FastAPI.
- Fontes grandes e layout simplificado foram adotados intencionalmente para garantir acessibilidade (persona Sr. João).
