import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from agno.db.sqlite import SqliteDb
from agno.vectordb.chroma import ChromaDb
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.semantic import SemanticChunking
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.team.team import Team

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

load_dotenv()

# ==============================================================
# Storage & RAG
# ==============================================================
db = SqliteDb(db_file="tmp/hello_team.db")

vector_db = ChromaDb(
    collection="hello_rag_collection",
    path="tmp/chroma_db",
    embedder=OpenAIEmbedder(id="text-embedding-3-small", api_key=os.getenv("OPENAI_API_KEY")),
    persistent_client=True,
)

knowledge = Knowledge(vector_db=vector_db)
knowledge.add_content(
    path="rag/analise_duop.pdf",
    reader=PDFReader(chunk_strategy=SemanticChunking()),
    metadata={"company": "Duop", "type": "financial_analysis"},
    skip_if_exists=True,
)

# ==============================================================
# Agents
# ==============================================================
analista_relatorios_agent = Agent(
    name="analista_relatorios",
    model=Claude(id="claude-sonnet-4-6"),
    knowledge=knowledge,
    add_knowledge_to_context=True,
    instructions="Voce é um analista de relatorios.",
    markdown=True,
)

analista_cotacoes_agent = Agent(
    name="analista_cotacoes",
    model=OpenAIChat(id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[YFinanceTools()],
    instructions=[
        "Voce é um analista de cotacoes de empresas listadas na B3.",
        "Para buscar cotacoes de acoes brasileiras (B3), sempre adicione o sufixo '.SA' ao ticker. Exemplos: PETR3 -> PETR3.SA, PETR4 -> PETR4.SA, ITUB4 -> ITUB4.SA, BBDC4 -> BBDC4.SA.",
    ],
    markdown=True,
)

analista_noticias_agent = Agent(
    name="analista_noticias",
    model=Claude(id="claude-sonnet-4-6"),
    role="Voce é um pesquisador de noticias.",
    instructions=[
        "Use suas tools de busca web para encontrar informações e noticias sobre empresas listadas na B3.",
        "Ao buscar, use queries simples e curtas, como 'Petrobras 2026' ou 'Itau resultados 2026'.",
    ],
    tools=[DuckDuckGoTools(enable_search=True, enable_news=False)],
    markdown=True,
)

# ==============================================================
# Team
# ==============================================================
analista_team = Team(
    name="Team Analista",
    model=Claude(id="claude-sonnet-4-6"),
    members=[analista_noticias_agent, analista_cotacoes_agent, analista_relatorios_agent],
    instructions=[
        "Voce deve entender as informacoes solicitadas pelo usuario e fornecer uma resposta adequada.",
        "Para obter informacoes sobre a opnião da Duop, utilize o analista_relatorios.",
        "Para obter informacoes sobre cotacoes, utilize o analista_cotacoes.",
        "Para obter informacoes sobre noticias, utilize o analista_noticias.",
    ],
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    show_members_responses=True,
    get_member_information_tool=True,
    add_datetime_to_context=True,
    markdown=True,
    debug_mode=False
)

# ==============================================================
# FastAPI
# ==============================================================
app = FastAPI(title="Agno Team API")


class ChatRequest(BaseModel):
    message: str
    session_id: str = "api_session"
    user_id: str = "api_user"


@app.post("/chat")
def chat(request: ChatRequest):
    result = analista_team.run(
        request.message,
        session_id=request.session_id,
        user_id=request.user_id,
    )
    return {
        "response": result.get_content_as_string(),
        "session_id": request.session_id,
        "user_id": request.user_id,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#Para rodar a API:
#==> uv run python hello_agno_streamlite.py

