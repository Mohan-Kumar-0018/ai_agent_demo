from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage

storage = SqliteStorage(table_name="agent_memory", db_file ="/tmp/agent_memory.db")
agent = Agent(
  session_id="test_session-1",
  model=OpenAIChat(id="gpt-4o"),
  markdown=True,
  add_history_to_messages=True,
  storage=storage
)

# Print the response in the terminal
# agent.print_response("My name is Mohan")
agent.print_response("What is my name?")