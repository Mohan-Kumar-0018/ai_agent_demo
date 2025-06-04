from agno.agent import Agent
from agno.tools.postgres import PostgresTools
from agno.models.openai import OpenAIChat

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
    tools=[postgres_tool],
    show_tool_calls=True,
)

# Step 3: Ask the agent a natural language question
if __name__ == "__main__":
    # query = "Show me the top 5 products with highest stock quantity."
    query = "What are top 2 warehouses with highest orders count? Give me the warehouse name and the count of orders."
    result = agent.run(query)
    print(result.content)
