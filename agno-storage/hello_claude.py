from agno.agent import Agent
from agno.tools.tavily import TavilyTools
#from agno.models.groq import Groq
from agno.models.anthropic import Claude

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Claude(id="claude-sonnet-4-6"),
    tools=[TavilyTools()]
)

agent.print_response("Qual a temperatura atual em Salvador?")

