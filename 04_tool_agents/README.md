# Tool-Using Agents

This directory contains implementations of agents that can use custom tools to interact with external systems, APIs, and services.

## What are Tool-Using Agents?

Tool-using agents extend the capabilities of language models by giving them access to:
- External APIs (weather, news, search)
- Databases and file systems
- Computational tools (calculators, code interpreters)
- Custom business logic

## Examples in this Directory

- `custom_tools.py` - Creating custom tool implementations
- `api_tools_agent.py` - Agent with API integration tools
- `file_system_tools.py` - Agent with file system access
- `calculator_tools.py` - Mathematical and computational tools
- `web_scraping_tools.py` - Tools for web data extraction

## Tool Design Principles

1. **Single Purpose**: Each tool should do one thing well
2. **Clear Description**: LLM needs to understand when to use the tool
3. **Robust Error Handling**: Handle failures gracefully
4. **Type Safety**: Use Pydantic models for input validation
5. **Idempotency**: Tools should be safe to call multiple times

## Creating a Custom Tool

```python
from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    expression: str = Field(description="Mathematical expression to evaluate")

def calculator_tool(input: CalculatorInput) -> str:
    """Evaluates a mathematical expression."""
    try:
        result = eval(input.expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

## Tool Categories

### Information Retrieval
- Web search
- Database queries
- API calls

### Computation
- Mathematical calculations
- Data analysis
- Code execution

### Action Tools
- File operations
- Email sending
- System commands

### Data Tools
- Format conversion
- Validation
- Transformation

## Best Practices

- Always validate tool inputs
- Provide clear error messages
- Log tool usage for debugging
- Set appropriate timeouts
- Handle rate limits
- Secure API keys properly

## References

- [LangChain Tools](https://python.langchain.com/docs/modules/agents/tools/)
- [Function Calling Best Practices](https://platform.openai.com/docs/guides/function-calling)
