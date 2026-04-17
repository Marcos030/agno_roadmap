from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.anthropic import Claude
from agno.db.sqlite import SqliteDb

from agno.vectordb.chroma import ChromaDb
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.semantic import SemanticChunking
from agno.knowledge.embedder.openai import OpenAIEmbedder

import os
from dotenv import load_dotenv
load_dotenv()

#Storage ==========
db = SqliteDb(db_file="tmp/hello_rag_1.db")

#RAG ==========
vector_db = ChromaDb(
    collection="hello_rag_collection", 
    path="tmp/chroma_db",
    embedder=OpenAIEmbedder(id="text-embedding-3-small", api_key=os.getenv("OPENAI_API_KEY")),
    persistent_client=True
)

#Base de conhecimento
knowledge = Knowledge( 
    vector_db=vector_db
)

knowledge.add_content (
    path="rag/analise_duop.pdf",
    reader=PDFReader(
        chunk_strategy=SemanticChunking()
    ),
    metadata={
        "company": "Duop",
        "type": "financial_analysis"        
    },
    skip_if_exists=True
)


#Agente ==========
agent = Agent(
    name="HelloRagAgent",
    db=db,
    model=Claude(id="claude-sonnet-4-6"),
    tools=[TavilyTools()],
    add_history_to_context=True,
    num_history_runs=3,
    enable_user_memories=True,
    add_memories_to_context=True,
    enable_agentic_memory=True,
    knowledge=knowledge,
    add_knowledge_to_context=True
)

agent.print_response("Qual a opinião da Duop sobre a recente trégua de 15 dias?", session_id="session_duop_1", user_id="user_duop")

agent.print_response("Qual a conclusão da Duop sobre o conflito?", session_id="session_duop_1", user_id="user_duop")

agent.print_response("Quem são os sócios fundadores da Duop?", session_id="session_duop_1", user_id="user_duop")
