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

### Simple Agent

A basic agent for general AI tasks:

```python
from agent import agent

agent.print_response("Share a 2 sentence horror story")
```

## Tool Call Logging

The GitHub agent implementation includes comprehensive tool call logging through hooks:

- **on_tool_start**: Logs when a tool is invoked and its arguments
- **on_tool_end**: Logs when a tool execution completes and its results
- **on_tool_error**: Captures and logs any errors during tool execution

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

[Specify your license here]
