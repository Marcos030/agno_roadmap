from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

msg = "Olá, meu nome é Marcos. Qual é o seu nome?"

response = model.invoke([HumanMessage(content=msg)])
print(response.content)
