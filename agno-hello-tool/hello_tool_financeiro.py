from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()]
)


# agent = Agent(
#     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
#     tools=[YFinanceTools()],
#     instructions="Retorne dados em formato de tabela, sem explicações adicionais."
# )

agent.print_response("Qual a cotação da Petrobras hoje?")

#agent.print_response("Me diga os principais acontecimentos da bolsa brasileira hoje. Faça um resumo de no maximo 10 linhas.", stream=True)

