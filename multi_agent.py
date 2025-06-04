from agno.agent import Agent
from agno.team.team import Team
from agno.tools.postgres import PostgresTools
from agno.tools.reasoning import ReasoningTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai import OpenAIChat

# Step 1: Initialize PostgresTools with your database connection info
postgres_tool = PostgresTools(
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432,
    db_name="stock_demo"
)

# Step 2: Define your stock agent
stock_agent = Agent(
    name="StockDemoAI",
    model=OpenAIChat(id="gpt-4o"),
    description="An AI agent that can query stock data and perform database operations.",
    tools=[postgres_tool],
    show_tool_calls=True,
)

# Step 3: Initialize DuckDuckGoTools for web searches
duckduckgo_tool = DuckDuckGoTools()

# Step 4: Define your web search agent
search_agent = Agent(
    name="WebSearchAI",
    model=OpenAIChat(id="gpt-4o"),
    description="An AI agent that can perform web searches using DuckDuckGo.",
    tools=[duckduckgo_tool],
    instructions="Perform web searches and extract relevant information from the results.",
    show_tool_calls=True,
)

reason_agent = Team(
    name="ProductReasoningAI",
    model=OpenAIChat(id="gpt-4.1"),  # Using GPT-4.1 as requested
    description="An AI agent that analyzes fast-selling products and finds potential sellers.",
    members=[stock_agent, search_agent],
    tools=[ReasoningTools(add_instructions=True)],
    instructions="""You are an AI assistant that helps find fast-selling products and potential sellers.    
    Follow these steps:
    1. Use the stock_query tool to identify fast-selling products from the inventory database.
    2. For each promising product, use the search_query tool to find potential sellers or suppliers.
    3. Analyze the combined data to provide insights about product performance and distribution opportunities.

    Provide clear, actionable insights based on the data from both sources.""",
    show_tool_calls=True,
)


if __name__ == "__main__":
    # query = "Show me the top 5 products with highest stock quantity."
    query = "What are top 2 products with highest orders count? Give me the warehouse name and the product name. Find the top seller in corresponding warehouse location for those products."
    reason_agent.print_response(query,
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
