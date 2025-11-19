# Simple ReAct Agents

This directory contains implementations of basic ReAct (Reasoning and Acting) agents. ReAct is a paradigm that combines chain-of-thought reasoning with action execution.

## What is ReAct?

ReAct agents follow this pattern:
1. **Thought**: Reason about the current situation
2. **Action**: Decide what action to take
3. **Observation**: Observe the result of the action
4. Repeat until the task is complete

## Examples in this Directory

- `basic_react_agent.py` - A simple ReAct agent implementation from scratch
- `react_with_tools.py` - ReAct agent with custom tools
- `react_loop.py` - Understanding the ReAct loop

## Usage

```python
from basic_react_agent import SimpleReActAgent

agent = SimpleReActAgent()
result = agent.run("What is the weather in New York?")
print(result)
```

## Key Concepts

- **Zero-shot reasoning**: The agent reasons without specific examples
- **Tool use**: Agents can call functions to interact with the world
- **Iterative problem solving**: Breaking down complex tasks into steps

## References

- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- Original research by Yao et al., 2022
