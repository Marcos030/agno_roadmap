from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")
msg = "Olá, meu nome é Marcos. Qual é o seu nome?"

agent = Agent(model=model)
agent.print_response(msg)