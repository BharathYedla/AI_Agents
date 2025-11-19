# LlamaIndex Agents

This directory contains implementations of agents using LlamaIndex (formerly GPT Index). LlamaIndex specializes in building agents that work with your own data.

## What is LlamaIndex?

LlamaIndex is a data framework for LLM applications. It provides:
- Data connectors to various sources
- Index structures for efficient retrieval
- Query engines and agents
- Integration with vector stores

## Examples in this Directory

- `llamaindex_query_agent.py` - Agent for querying indexed data
- `llamaindex_data_agent.py` - Agent with custom data sources
- `llamaindex_multi_doc_agent.py` - Agent working with multiple documents
- `llamaindex_tool_agent.py` - Agent with query engine tools

## Key Concepts

### Query Engines
Query engines allow you to ask questions about your data:
- **Vector Store Index**: For semantic search
- **List Index**: For comprehensive retrieval
- **Tree Index**: For hierarchical data

### Data Agents
Agents that can reason over your data and use tools to answer questions.

## Usage

```python
from llamaindex_query_agent import create_query_agent

agent = create_query_agent(data_path="./documents")
response = agent.query("What are the key findings?")
print(response)
```

## Features

- **Data Ingestion**: Load data from files, databases, APIs
- **Indexing**: Create efficient search structures
- **Querying**: Natural language queries over your data
- **Agent Tools**: Query engines as agent tools
- **Memory**: Maintain conversation context

## References

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [LlamaIndex Agents Guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
