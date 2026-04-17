from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.anthropic import Claude
from agno.db.sqlite import SqliteDb

from dotenv import load_dotenv
load_dotenv()

db = SqliteDb(db_file="tmp/hello_claude_storage_1.db")

agent = Agent(
    name="HelloAgent",
    db=db,
    model=Claude(id="claude-sonnet-4-6"),
    tools=[TavilyTools()],
    add_history_to_context=True,
    num_history_runs=3
)

agent.print_response("Qual a temperatura atual em Salvador?")
agent.print_response("Qual a última cidade consultada?")

