from agno.agent import Agent
from agno.tools.postgres import PostgresTools
from agno.tools.thinking import ThinkingTools
from agno.models.openai import OpenAIChat

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Step 1: Initialize PostgresTools with your database connection info
postgres_tool = PostgresTools(
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432,
    db_name="stock_demo"
)

# Step 2: Define your agent
agent = Agent(
    name="StockDemoAI",
    model=OpenAIChat(id="gpt-4o"),
    description="An AI agent that can query stock data and perform database operations.",
    tools=[postgres_tool, ThinkingTools()],
    show_tool_calls=True,
)

# Step 3: Ask the agent a natural language question
if __name__ == "__main__":
    query = "What are the top 3 best-selling products by quantity in last 5 days?"
    # query = "Show me the top 5 products with highest stock quantity"
    # query = "Which warehouse needs to be restocked and which products? based on orders in that warehouse and current stock quantity"
    # query = "What work can be assigned to manager in BENGALURU warehouse?"
    result = agent.run(query)
    print(result.content)
