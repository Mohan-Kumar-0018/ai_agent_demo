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
)

# Step 3: Ask the agent a natural language question
if __name__ == "__main__":
    query = "What are the top 3 best-selling products by quantity in last 5 days?"
    result = agent.run(query)
    print(result.content)







# Create tables:
# 1. Warehouses:
#   - id
#   - name
#   - location

# 2. Products:
#   - id
#   - name
#   - price

# 3. Orders:
#   - id
#   - product_id
#   - quantity
#   - price
#   - warehouse_id
#   - order_date

# 4. Stock:
#     - id
#     - product_id
#     - warehouse_id
#     - quantity