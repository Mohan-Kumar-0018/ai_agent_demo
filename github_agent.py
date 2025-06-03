import os
import logging
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.github import GithubTools

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables (for GITHUB_ACCESS_TOKEN)
load_dotenv()

# Define tool hooks for logging
def on_tool_start(tool_name, **kwargs):
    logger.info(f"Tool Call Started: {tool_name}")
    logger.info(f"Arguments: {kwargs}")

def on_tool_end(tool_name, result, **kwargs):
    logger.info(f"Tool Call Completed: {tool_name}")
    logger.info(f"Result: {result}")
    logger.info("---")

def on_tool_error(tool_name, error, **kwargs):
    logger.error(f"Tool Call Error in {tool_name}: {error}")
    logger.error("---")

# Initialize a single GitHub agent with all tools enabled
github_agent = Agent(
    name="GitHub Agent",
    role="Perform various GitHub operations like fetching pull requests, stars, issues, etc.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GithubTools(get_repository_stars=True, create_branch=True, get_pull_requests=True,get_pull_request_changes=True, get_pull_request_with_details=True, get_pull_request_comments=True)],
    instructions="Help with GitHub operations including fetching repository information, pull requests, issues, etc.",
    show_tool_calls=True,
    tool_hooks={
        "on_tool_start": on_tool_start,
        "on_tool_end": on_tool_end,
        "on_tool_error": on_tool_error
    },
)

def run_github_query(query):
    """
    Run a query against the GitHub agent.
    
    Args:
        query (str): The query to run
        
    Returns:
        str: The response content
    """
    logger.info(f"Running query: {query}")
    response = github_agent.run(query)
    logger.info(f"Query completed. Response length: {len(response.content)}")
    
    return response.content

# Example usage
if __name__ == "__main__":
    # Example repository
    repo = "shopuptech/warehouse_mgmt_service"
    # repo = "Mohan-Kumar-0018/rag-demo"
    
    # Example 1: 
    pr_query = f"What is the status of the PR 3870 in repo: {repo}"
    pr_result = run_github_query(pr_query)
    print(f"Branch created in {repo}: {pr_result}")
    

    
