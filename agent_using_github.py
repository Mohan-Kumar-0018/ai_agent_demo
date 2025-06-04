
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.github import GithubTools

# Load environment variables (for GITHUB_ACCESS_TOKEN)
load_dotenv()

# Initialize a single GitHub agent with all tools enabled
github_agent = Agent(
    name="GitHub Agent",
    role="Perform various GitHub operations like fetching pull requests, stars, issues, etc.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GithubTools(
        get_repository_stars=True,
        get_pull_request_count=True,
        get_pull_requests=True,
        get_pull_request_changes=True,
        get_pull_request_with_details=True,
        get_pull_request_comments=True
    )],
    instructions="Help with GitHub operations including fetching repository information, pull requests, issues, etc.",
    show_tool_calls=True,
    debug_mode=True
)

if __name__ == "__main__":
    query = "How many stars does the repo: Mohan-Kumar-0018/rag-demo have?"
    result = github_agent.run(query)
    print(result.content)
