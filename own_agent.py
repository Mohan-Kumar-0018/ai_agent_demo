from datetime import date, timedelta
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.decorator import tool


# Tool 1: Get employee list
@tool(name="get_employees", description="Returns a list of employee names.")
def get_employees() -> list:
    return ["Alice", "Bob", "Charlie", "Diana", "Eve"]


# Tool 2: Get list of employees on leave in the upcoming week
@tool(name="get_upcoming_leaves", description="Returns a list of employees who have leaves in the next week.")
def get_upcoming_leaves() -> list:
    today = date.today()
    return [
        {"name": "Alice", "leave_date": str(today + timedelta(days=2))},
        {"name": "Eve", "leave_date": str(today + timedelta(days=5))},
    ]


# Create the agent with tools
agent = Agent(
    name="OnCallScheduleAgent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[get_employees, get_upcoming_leaves],
    description="Agent that generates an on-call employee schedule for next week considering leaves.",
    show_tool_calls=True,
    debug_mode=True,
)

# Run the agent
if __name__ == "__main__":
    query = "Generate the on-call schedule for next week considering employee leaves."
    response = agent.run(query)
    print("Response:\n", response.content)
