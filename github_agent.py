import logging
import argparse
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.github import GithubTools

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

def get_test_cases_query(pr_id, repo):
    """
    Generate a query to get test cases added in a PR
    
    Args:
        pr_id (str): The PR ID
        repo (str): The repository name
        
    Returns:
        str: The formatted query
    """
    return f"""What are the test cases added in PR {pr_id} in repo : {repo} ?
    Give in Below format:
    File name: <file_name>
    Test cases added: 
     Failure cases:
      Context: <context>
      Error: <error>
     Success case:
      Context: <context>
      Asserted fields: <asserted_fields>"""

def get_curl_request_query(pr_id, repo):
    """
    Generate a query to get sample curl requests for APIs added/changed in a PR
    
    Args:
        pr_id (str): The PR ID
        repo (str): The repository name
        
    Returns:
        str: The formatted query
    """
    return f"""
    Give a sample curl request for the new API added/ existing API changed in PR {pr_id} in repo: {repo} ?

    Use BaseUrl: https://mokamap.shopups2.xyz/sc2_admin/ for all requests

    Identify the api routes and give in below format:

    Sample curl:
    curl --location 'https://mokamap.shopups2.xyz/sc2_admin/group_orders/list_orders?warehouse_id=871&id=69347' \
    --header 'Cookie: __st__2__=XXXXX'
    Return the curl request
    """

# Command line interface
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="GitHub Agent Query Interface")
    parser.add_argument("--pr", type=str, required=True, help="Pull Request ID")
    parser.add_argument("--repo", type=str, required=True, help="Repository name (format: owner/repo)")
    parser.add_argument("--type", type=str, choices=["test_cases", "curl"], required=True, 
                      help="Query type: 'test_cases' for test case analysis, 'curl' for curl request examples")
    
    args = parser.parse_args()
    
    # Build query based on type
    if args.type == "test_cases":
        query = get_test_cases_query(args.pr, args.repo)
    elif args.type == "curl":
        query = get_curl_request_query(args.pr, args.repo)
    
    print(f"Running query: {query}")
    result = run_github_query(query)
    print(f"Result:\n{result}")




# # To analyze test cases in PR 3843 for shopuptech/warehouse_mgmt_service
# python github_agent.py --pr 3843 --repo shopuptech/warehouse_mgmt_service --type test_cases

# # To get curl request examples from PR 1962 for shopuptech/sc2_admin
# python github_agent.py --pr 1962 --repo shopuptech/sc2_admin --type curl