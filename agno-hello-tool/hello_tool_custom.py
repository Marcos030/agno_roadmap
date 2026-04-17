from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()


def cells_to_fahrenheit(celsius):
    """
    Converte Celsius para Fahrenheit.
    :param celsius: Temperatura em Celsius.
    :return: Temperatura em Fahrenheit.
    """
    return (celsius * 9/5) + 32



agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions="Você é um assistente útil e inteligente que responde perguntas sobre o clima usando a ferramenta Tavily. Use a função cells_to_fahrenheit para converter temperaturas de Celsius para Fahrenheit quando necessário. Devolva a  temperatura em Fahrenheit e em celcius.",
    tools=[
        TavilyTools(),
        cells_to_fahrenheit
        ],
        debug_mode=True
)

agent.print_response("Qual a temperatura atual em Salvador?")

