from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="groq/llama-3.3-70b-versatile")

msg = "Olá, meu nome é Marcos. Qual é o seu nome?"

agent = Agent(
    role="Assistente",
    goal="Responder perguntas de forma clara e amigável",
    backstory="Você é um assistente prestativo e simpático.",
    llm=llm,
    verbose=False,
)

task = Task(
    description=msg,
    expected_output="Uma resposta amigável à mensagem recebida.",
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task], 
    verbose=False
)

result = crew.kickoff()
print(result)
