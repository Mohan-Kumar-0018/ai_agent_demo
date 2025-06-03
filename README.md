# AI Agent Demo

This project demonstrates how to build and use AI agents with the Agno framework, focusing on GitHub operations and tool calls.

## Overview

The AI Agent Demo provides examples of how to:
- Create and configure an AI agent with specific tools
- Implement GitHub operations using the OpenAI API
- Track and log tool calls made by the agent
- Execute queries against repositories

## Components

### Main Components

- **github_agent.py**: GitHub-specific agent with tools for repository operations
- **postgres_agent.py**: PostgreSQL agent for database operations and queries
- **agent.py**: Simple AI agent implementation
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

The GitHub agent can perform various operations on GitHub repositories:
- Fetch pull request details
- Get repository stars
- Create branches
- View pull request changes and comments

Example usage:

```python
from github_agent import run_github_query

# Check status of a PR
pr_query = "What is the status of PR 3870 in repo: shopuptech/warehouse_mgmt_service"
result = run_github_query(pr_query)
print(result)
```

Command-line interface usage:

```bash
# Using default query
python github_agent.py

# Specifying a custom query
python github_agent.py --query="How many stars does the repo: Mohan-Kumar-0018/rag-demo have?"

# Using short form option
python github_agent.py -q="What are the changes in PR ID 3871 in repo: shopuptech/warehouse_mgmt_service?"
```

### PostgreSQL Agent

The PostgreSQL agent can perform database operations and answer natural language queries about data:
- Query database tables
- Analyze stock data
- Generate insights from warehouse information
- Perform complex SQL operations through natural language

Example usage:

```python
# In postgres_agent.py
query = "What are the top 3 best-selling products by quantity in last 5 days?"
result = agent.run(query)
print(result.content)
```

The PostgreSQL agent includes a modular run_postgres_query function and supports command-line execution for database operations and queries with detailed logging of all database operations.

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
