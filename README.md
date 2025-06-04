# AI Agent Demo

This project demonstrates how to build and use AI agents with the Agno framework, focusing on GitHub operations and tool calls.

## Overview

The AI Agent Demo provides examples of how to:
- Create and configure an AI agent with specific tools
- Implement GitHub operations using the OpenAI API
- Track and log tool calls made by the agent
- Execute queries against repositories and databases

## Components

### Main Components

- **github_agent.py**: GitHub-specific agent with tools for repository operations
- **agent_using_postgres.py**: PostgreSQL agent for database operations and queries
- **agent.py**: Simple AI agent implementation
- **agent_using_github.py**: Another GitHub agent implementation example
- **multi_agent.py**: Implementation of multiple agents working together
- **own_agent.py**: Custom agent implementation
- **requirements.txt**: Package dependencies
- **prompts.txt**: Example prompts for the agents

## Setup

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your API credentials:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GITHUB_ACCESS_TOKEN=your_github_token
   ```

## Usage

### GitHub Agent

The GitHub agent (`github_agent.py`) provides a specialized interface for GitHub repository operations, focusing on PR analysis:

- Fetch pull request details and changes
- Get repository stars and PR counts
- View pull request comments
- Extract test cases from pull requests
- Generate curl requests for APIs added or modified in a PR

The agent is implemented using the Agno framework and OpenAI's GPT-4o model with detailed tool logging.

Example usage in Python code:

```python
from github_agent import run_github_query

# Check status of a PR
pr_query = "What is the status of PR 3870 in repo: shopuptech/warehouse_mgmt_service"
result = run_github_query(pr_query)
print(result)
```

Command-line interface usage:

```bash
# For analyzing test cases in a PR
python github_agent.py --pr 3843 --repo shopuptech/warehouse_mgmt_service --type test_cases

# For generating curl requests from a PR
python github_agent.py --pr 1962 --repo shopuptech/sc2_admin --type curl
```

Note: The GitHub agent CLI has been simplified to include only two options: `test_cases` and `curl`, requiring three mandatory arguments: `--pr` (Pull Request ID), `--repo` (Repository name), and `--type` (with only "test_cases" and "curl" as valid choices).

#### Test Case Analysis

When using the `test_cases` option, the agent will analyze a PR and return structured information about added test cases including:
- File names with test additions
- Failure test cases with context and error expectations
- Success test cases with context and asserted fields

#### Curl Request Generation

When using the `curl` option, the agent will analyze API changes in a PR and generate sample curl commands with:
- Properly formatted curl syntax
- Appropriate headers and cookies
- Base URL and endpoint path
- Required parameters

### PostgreSQL Agent

The PostgreSQL agent can perform database operations and answer natural language queries about data:
- Query database tables
- Analyze stock data
- Generate insights from warehouse information
- Perform complex SQL operations through natural language

Example usage:

```python
# In agent_using_postgres.py
query = "What are top 2 warehouses with highest orders count?"
result = agent.run(query)
print(result.content)
```

### Multi-Agent Team

The `multi_agent.py` file demonstrates how to build a team of specialized agents working together to solve complex tasks. This implementation shows the power of combining multiple AI agents with different capabilities into a cohesive system.

#### Team Components

1. **StockDemoAI** - Database specialist that queries stock data
   - Uses PostgresTools to connect to a local PostgreSQL database
   - Specializes in inventory and warehouse data analysis

2. **WebSearchAI** - Search specialist using DuckDuckGo
   - Performs web searches to gather external information
   - Extracts relevant data from search results

3. **ProductReasoningAI** - Coordinating team agent
   - Combines insights from both specialized agents
   - Uses ReasoningTools for advanced analysis
   - Implemented with GPT-4.1 model for sophisticated reasoning

#### Example Usage

```python
# In multi_agent.py
query = "What are top 2 products with highest orders count? Give me the warehouse name and the product name. Find the top seller in corresponding warehouse location for those products."

reason_agent.print_response(query,
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
```

The multi-agent approach allows for complex queries that require both internal data analysis and external information gathering, providing more comprehensive insights than any single agent could deliver alone.

### Simple Agent

A basic agent for general AI tasks:

```python
from agent import agent

agent.print_response("Share a 2 sentence horror story")
```

## Tool Call Logging

The GitHub agent implementation includes comprehensive tool call logging through the built-in debug mode:

- Enabled with the `debug_mode=True` parameter in the Agent initialization
- Automatically logs tool invocations, inputs, and outputs
- Provides detailed information about tool execution flow
- Helps with debugging and understanding the agent's reasoning process

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

[Specify your license here]
