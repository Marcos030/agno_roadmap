# Projetos de Agentes de IA

Coleção de projetos práticos explorando os principais frameworks de agentes de IA em Python: **Agno**, **CrewAI**, **LangChain** e **LangGraph**.

---

## Pré-requisitos

| Requisito | Versão mínima | Link |
|-----------|--------------|------|
| Python | 3.12+ | [python.org](https://python.org) |
| uv (gerenciador de pacotes) | latest | [docs.astral.sh/uv](https://docs.astral.sh/uv) |

### Instalando o uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Chaves de API necessárias

Cada projeto usa um arquivo `.env` na sua própria pasta. Crie o arquivo copiando o `.env.example` (quando disponível) ou crie manualmente com as chaves que o projeto exige.

| Chave | Onde obter | Projetos que usam |
|-------|-----------|-------------------|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) | agno-hello, agno-hello-tool, crewai-hello, langchain-hello, langgraph-hello |
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com) | agno-storage, agno-sonho |
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) | agno-storage (hello_claude.py) |
| `TAVILY_API_KEY` | [app.tavily.com](https://app.tavily.com) | agno-hello-tool, agno-storage |

Exemplo de `.env`:
```env
GROQ_API_KEY=gsk_...
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
```

---

## Estrutura dos projetos

```
projetos_apresentacao/
├── agno-hello/           # Introdução ao framework Agno
├── agno-hello-tool/      # Agentes com ferramentas (web search, finanças)
├── agno-storage/         # Storage, memória, RAG, multi-agentes, UI
├── agno-sonho/           # Multi-agentes avançado com RAG e memória
├── crewai-hello/         # Introdução ao framework CrewAI
├── langchain-hello/      # Introdução ao LangChain
├── langgraph-hello/      # Introdução ao LangGraph
└── utils/                # Materiais do curso Asimov Academy
```

---

## Como rodar cada projeto

O fluxo padrão é o mesmo para todos os projetos Python:

```bash
# 1. Entre na pasta do projeto
cd nome-do-projeto

# 2. Crie o ambiente virtual
uv venv

# 3. Ative o ambiente virtual
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 4. Instale as dependências
uv sync

# 5. Crie o arquivo .env com suas chaves (veja tabela acima)
# 6. Execute o script desejado
uv run nome-do-script.py
ou
python nome-do-script.py
```

---

## Descrição dos projetos

### `agno-hello` — Primeiro agente com Agno

Agente simples usando o modelo `llama-3.3-70b-versatile` via Groq.

**Chaves necessárias:** `GROQ_API_KEY`

```bash
cd agno-hello && uv sync
python hello-agno.py
```

---

### `agno-hello-tool` — Agentes com ferramentas

Demonstra o uso de ferramentas nativas e customizadas no Agno.

**Chaves necessárias:** `GROQ_API_KEY`, `TAVILY_API_KEY`

| Script | Descrição |
|--------|-----------|
| `hello_tool.py` | Busca na web com TavilyTools |
| `hello_tool_custom.py` | Ferramenta customizada (conversão Celsius → Fahrenheit) |
| `hello_tool_financeiro.py` | Preços de ações da B3 via YFinance |

```bash
cd agno-hello-tool && uv sync
python hello_tool.py
python hello_tool_custom.py
python hello_tool_financeiro.py
```

---

### `agno-storage` — Storage, memória, RAG e multi-agentes

Projeto completo com múltiplas funcionalidades avançadas.

**Chaves necessárias:** `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `TAVILY_API_KEY`

```bash
cd agno-storage && uv sync
```

| Script | Descrição |
|--------|-----------|
| `hello_storage_basic.py` | Agente com histórico persistido em SQLite |
| `hello_storage_memoria.py` | Memória de usuário entre sessões |
| `hello_storage_session.py` | Múltiplas sessões com preferências diferentes |
| `hello_storage_rag.py` | RAG com PDF usando ChromaDB |
| `hello_multiagent.py` | Time de 3 agentes especializados (analista, cotações, notícias) |
| `hello_claude.py` | Agente usando o modelo Claude (Anthropic) |
| `hello_agent_os.py` | Agente exposto como serviço web via AgentOS |
| `hello_agno_streamlite.py` | Backend FastAPI para o time de agentes |
| `hello_agno_streamlit_UI.py` | UI Streamlit conectada ao backend FastAPI |

**Para rodar a UI completa (FastAPI + Streamlit):**
```bash
# Terminal 1 — inicia o backend
python hello_agno_streamlite.py

# Terminal 2 — inicia a UI
streamlit run hello_agno_streamlit_UI.py
```

**Para rodar o frontend Next.js (agent-ui):**
```bash
cd agno-storage/agent-ui
npm install
npm run dev
# Acesse http://localhost:3000
```

---

### `agno-sonho` — Multi-agentes avançado

Time de agentes com RAG em PDF, memória e múltiplos provedores de LLM (Claude, OpenAI, Groq).

**Chaves necessárias:** `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GROQ_API_KEY`

```bash
cd agno-sonho && uv sync
python main.py
```

---

### `crewai-hello` — Primeiro agente com CrewAI

Introdução ao framework CrewAI com Groq como provedor de LLM.

**Chaves necessárias:** `GROQ_API_KEY`

```bash
cd crewai-hello && uv sync
python hello-crewai.py
```

---

### `langchain-hello` — Primeiro agente com LangChain

Exemplo mínimo de uso do LangChain com ChatGroq.

**Chaves necessárias:** `GROQ_API_KEY`

```bash
cd langchain-hello && uv sync
python hello-langchain.py
```

---

### `langgraph-hello` — Primeiro agente com LangGraph

Grafo de estado simples com um nó que invoca o modelo.

**Chaves necessárias:** `GROQ_API_KEY`

```bash
cd langgraph-hello && uv sync
python hello-langgraph.py
```

---

### `utils/` — Materiais do curso Asimov Academy

Exemplos numerados do curso **"Criando Agentes de IA com Agno"**, organizados em módulos. Úteis como referência e estudo progressivo.

**Chaves necessárias:** `OPENAI_API_KEY`

---

## Dicas

- **Nunca commite o arquivo `.env`** — ele já está no `.gitignore`.
- Se ao rodar `uv sync` aparecer erro de versão do Python, verifique com `python --version` e instale a versão correta.
- Os arquivos `tmp/` e bancos `.db` são criados em tempo de execução e também estão no `.gitignore`.
- Para projetos com ChromaDB (RAG), a primeira execução faz o download e indexação dos documentos — pode demorar alguns segundos.
