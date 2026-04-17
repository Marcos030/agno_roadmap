from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.anthropic import Claude
from agno.db.sqlite import SqliteDb

from dotenv import load_dotenv
load_dotenv()

db = SqliteDb(db_file="tmp/hello_claude_storage.db")

# agent = Agent(
#     name="HelloAgent",
#     db=db,
#     model=Claude(id="claude-sonnet-4-6"),
#     tools=[TavilyTools()],
#     add_history_to_context=True,
#     num_history_runs=3,
#     session_id="session_salvador",
#     user_id="user_salvador"
# )


agent = Agent(
    name="HelloAgent",
    db=db,
    model=Claude(id="claude-sonnet-4-6"),
    tools=[TavilyTools()],
    add_history_to_context=True,
    num_history_runs=3
)

agent.print_response("Qual a temperatura atual em Salvador?", session_id="session_salvador", user_id="user_salvador")
agent.print_response("Qual a última cidade consultada?", session_id="session_salvador", user_id="user_salvador")

agent.print_response("Qual a temperatura atual em Pelotas?", session_id="session_pelotas", user_id="user_pelotas")
agent.print_response("Qual a última cidade consultada?", session_id="session_pelotas", user_id="user_pelotas")

agent.print_response("Você já pesquisou sobre pelotas?", session_id="session_salvador", user_id="user_salvador")
