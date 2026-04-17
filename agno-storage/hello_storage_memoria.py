from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.anthropic import Claude
from agno.db.sqlite import SqliteDb

from dotenv import load_dotenv
load_dotenv()

db = SqliteDb(db_file="tmp/hello_claude_storage_2.db")

# agent = Agent(
#     name="HelloAgent",
#     db=db,
#     model=Claude(id="claude-sonnet-4-6"),
#     tools=[TavilyTools()],
#     add_history_to_context=True,
#     num_history_runs=3,
#     session_id="session_salvador",
#     user_id="user_salvador"
# )


agent = Agent(
    name="HelloAgent",
    db=db,
    model=Claude(id="claude-sonnet-4-6"),
    tools=[TavilyTools()],
    add_history_to_context=True,
    num_history_runs=3,
    enable_user_memories=True,
    add_memories_to_context=True,
)


#É possível usar gerenciador de memória específico. As vezes vc está usando um modelo grande para o agente, mas quer usar um modelo menor para criar as memórias, ou tem uma tarefa específica de criação de memórias e quer usar um modelo específico para isso. O MemoryManager é a forma mais flexível de lidar com isso, mas é possível também usar as memórias de usuário simples, que são criadas automaticamente a partir do histórico das conversas.
# memory_manager = MemoryManager(
#     db=db,
#     # Select the model used for memory creation and updates. If unset, the default model of the Agent is used.
#     model=OpenAIResponses(id="gpt-5.2"),
#     # You can also provide additional instructions
#     additional_instructions="Don't store the user's real name",
# )

#Criei outra session para que o agente não engabele e use a sessão como memória
agent.print_response("Eu prefiro respostas curtas e diretas.", session_id="session_salvador_1", user_id="user_salvador")
agent.print_response("Eu prefiro respostas detalhadas e informativas.", session_id="session_pelotas_1", user_id="user_pelotas")

agent.print_response("Qual a temperatura atual em Salvador?", session_id="session_salvador_2", user_id="user_salvador")
# agent.print_response("Qual a última cidade consultada?", session_id="session_salvador", user_id="user_salvador")

agent.print_response("Qual a temperatura atual em Pelotas?", session_id="session_pelotas_2", user_id="user_pelotas")    
# agent.print_response("Qual a última cidade consultada?", session_id="session_pelotas", user_id="user_pelotas")

# agent.print_response("Você já pesquisou sobre pelotas?", session_id="session_salvador", user_id="user_salvador")
