from agno.agent import Agent
from agno.team.team import Team
from agno.tools.postgres import PostgresTools
from agno.tools.thinking import ThinkingTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai import OpenAIChat

# Step 1: Initialize PostgresTools with your database connection info
postgres_tool = PostgresTools(
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432,
    db_name="agent_demo"
)

# Step 2: Define your stock agent
stock_agent = Agent(
    name="StockDemoAI",
    model=OpenAIChat(id="gpt-4o"),
    description="An AI agent that can query stock data and perform database operations.",
    tools=[postgres_tool],
    show_tool_calls=True,
    debug_mode=True,
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
    debug_mode=True,
)

team = Team(
    name="ProductReasoningAI",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4.1"),  # Using GPT-4.1 as requested
    description="An AI agent that analyzes warehouse products data and finds relevant info from web.",
    members=[stock_agent, search_agent],
    tools=[ThinkingTools(add_instructions=True)],
    instructions="""You are an AI assistant that helps in getting sales related data from database and do web searches.    
    Follow these steps:
    1. Use the stock_agent tool to get stock , products , warehouses, orders related info from the inventory database.
    2. Use the search_agent tool to do web searches.
    Provide clear, actionable insights based on the data from both sources.""",
    show_tool_calls=True,
    debug_mode=True,
)


if __name__ == "__main__":
    # query = "Show me the top 5 products with highest stock quantity."
    query = "Which warehouse got least orders count ? What is least sold product in that warehouse? Find me the top rated brand showroom of the product in that warehouse location. Return the showroom name, address and phone number"
    team.print_response(query,
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
