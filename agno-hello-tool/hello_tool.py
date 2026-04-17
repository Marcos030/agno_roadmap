from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),
    tools=[TavilyTools()]
)

agent.print_response("Qual a temperatura atual em Salvador?")

