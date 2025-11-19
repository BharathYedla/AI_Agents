# LangChain Agents

This directory contains implementations of agents using the LangChain framework. LangChain provides a powerful abstraction for building LLM-powered applications.

## What is LangChain?

LangChain is a framework for developing applications powered by language models. It provides:
- Ready-to-use agent types
- Tool integration
- Memory management
- Chain composition

## Examples in this Directory

- `langchain_basic_agent.py` - Basic LangChain agent setup
- `langchain_tools_agent.py` - Agent with custom tools
- `langchain_conversational_agent.py` - Agent with memory
- `langchain_structured_output.py` - Agent with structured outputs

## Agent Types

LangChain supports several agent types:
- **Zero-shot ReAct**: Chooses tools based on their descriptions
- **Conversational ReAct**: Maintains conversation history
- **OpenAI Functions**: Uses OpenAI's function calling
- **Structured Chat**: For complex multi-input tools

## Usage

```python
from langchain_basic_agent import create_basic_agent

agent = create_basic_agent()
result = agent.run("What is the capital of France?")
print(result)
```

## Key Features

- **Tool Integration**: Easy integration with external tools and APIs
- **Memory**: Maintain conversation context across interactions
- **Callbacks**: Monitor and debug agent execution
- **Chains**: Compose multiple operations

## References

- [LangChain Documentation](https://python.langchain.com/docs/modules/agents/)
- [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/agent_types/)
