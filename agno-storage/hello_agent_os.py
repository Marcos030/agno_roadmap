from agno.agent import Agent
from agno.tools.tavily import TavilyTools
#from agno.models.groq import Groq
from agno.models.anthropic import Claude
from agno.os import AgentOS

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    name="HelloAgentOS",
    model=Claude(id="claude-sonnet-4-6"),
    tools=[TavilyTools()]
)

agent_os = AgentOS(
    agents=[agent]
    )


app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="hello_agent_os:app", reload=True)

