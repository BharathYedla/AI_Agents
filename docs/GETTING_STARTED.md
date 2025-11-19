# Getting Started with AI Agents

This guide will help you get started with the AI Agents repository.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Your First Agent](#your-first-agent)
5. [Understanding ReAct](#understanding-react)
6. [Working with Tools](#working-with-tools)
7. [Next Steps](#next-steps)

## Introduction

AI Agents are autonomous systems that can:
- Perceive their environment
- Make decisions based on reasoning
- Take actions to achieve goals
- Learn from outcomes

This repository provides practical examples of different agent architectures and implementations.

## Prerequisites

Before getting started, ensure you have:
- Python 3.9 or higher installed
- Basic understanding of Python programming
- (Optional) OpenAI API key for LLM-based agents

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/BharathYedla/AI_Agents.git
cd AI_Agents
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

## Your First Agent

Let's start with a simple ReAct agent that doesn't require an API key:

```python
# Run the basic ReAct agent
cd 01_simple_react_agents
python basic_react_agent.py
```

This will demonstrate:
- How agents think about problems
- How they select actions
- How they observe results
- The iterative reasoning process

## Understanding ReAct

ReAct (Reasoning and Acting) is a fundamental pattern for AI agents:

1. **Thought**: The agent reasons about the current situation
2. **Action**: The agent decides what action to take
3. **Observation**: The agent observes the result
4. **Repeat**: Continue until the goal is achieved

Example from the code:
```python
agent = SimpleReActAgent()
result = agent.run("What is 2 + 2?")

# The agent will:
# 1. Think: "I need to perform a calculation"
# 2. Act: Use the calculator tool
# 3. Observe: Get the result "4"
# 4. Think: "I have the answer"
# 5. Act: Finish with the answer
```

## Working with Tools

Tools extend agent capabilities. Here's how to create a custom tool:

```python
from typing import Any

class CustomTool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def run(self, input_data: Any) -> str:
        # Your tool logic here
        return f"Tool {self.name} processed: {input_data}"

# Use the tool
tool = CustomTool("my_tool", "Does something useful")
result = tool.run("test input")
```

## Examples by Complexity

### Level 1: Beginner
- `01_simple_react_agents/basic_react_agent.py` - Start here!
- `04_tool_agents/custom_tools.py` - Learn about tools

### Level 2: Intermediate
- `02_langchain_agents/` - Framework-based agents
- `05_knowledge_graph_agents/simple_knowledge_graph.py` - Graph reasoning

### Level 3: Advanced
- `03_llamaindex_agents/` - Data-centric agents
- `06_multi_agent_systems/collaborative_agents.py` - Multi-agent systems

## Common Patterns

### 1. Zero-Shot Reasoning
The agent reasons without examples:
```python
agent.run("Solve this problem: ...")
```

### 2. Tool Selection
The agent chooses the right tool for the job:
```python
tools = [calculator, search, weather]
agent = Agent(tools=tools)
agent.run("What's the weather in New York?")  # Uses weather tool
```

### 3. Multi-Step Planning
The agent breaks down complex tasks:
```python
agent.run("Research AI agents and write a summary")
# Step 1: Research
# Step 2: Organize information
# Step 3: Write summary
```

## Working with LLMs

For examples that use LLMs (OpenAI, Anthropic):

1. **Get an API key:**
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic: https://console.anthropic.com/

2. **Set the environment variable:**
```bash
export OPENAI_API_KEY='your-key-here'
```

3. **Run LLM-based examples:**
```python
# These require API keys (commented out by default)
# Uncomment the code after setting up API keys
cd 02_langchain_agents
python langchain_basic_agent.py
```

## Debugging Tips

1. **Enable verbose mode:**
```python
agent = Agent(verbose=True)  # See detailed execution
```

2. **Check logs:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

3. **Limit iterations:**
```python
agent = Agent(max_iterations=3)  # Prevent infinite loops
```

## Next Steps

1. **Explore Examples**: Go through each directory in order
2. **Modify Code**: Change tools, prompts, and logic
3. **Build Your Own**: Create agents for your use cases
4. **Read Papers**: Check references in README files
5. **Join Community**: Contribute improvements!

## Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "API key not set" error
```bash
export OPENAI_API_KEY='your-key'
```

### Import errors
Make sure you're in the correct directory and virtual environment is activated.

## Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

## Contributing

Found a bug or have an improvement? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

Happy coding! Start with `01_simple_react_agents/basic_react_agent.py` and work your way up.
