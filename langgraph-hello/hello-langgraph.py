from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

def call_model(state: MessagesState):
    return {"messages": [model.invoke(state["messages"])]}

graph = StateGraph(MessagesState)
graph.add_node("agent", call_model)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)

agent = graph.compile()

msg = "Olá, meu nome é Marcos. Qual é o seu nome?"

response = agent.invoke({"messages": [{"role": "user", "content": msg}]})
print(response["messages"][-1].content)
