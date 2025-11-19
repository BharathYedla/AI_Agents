# AI Agents - Complete Learning Repository

This repository contains comprehensive examples and implementations of various AI agent concepts, architectures, and frameworks. It serves as a practical guide for building intelligent agents using LLMs, Knowledge Graphs, and other advanced techniques.

## 🎯 Overview

AI Agents are autonomous systems that can perceive their environment, make decisions, and take actions to achieve specific goals. This repository covers:

- **ReAct Agents**: Reasoning and Acting agents that combine chain-of-thought reasoning with action execution
- **LangChain Agents**: Implementations using the LangChain framework
- **LlamaIndex Agents**: Query and data agents built with LlamaIndex
- **Tool-Using Agents**: Agents that can leverage external tools and APIs
- **Knowledge Graph Agents**: Agents that reason over structured knowledge
- **Multi-Agent Systems**: Collaborative agent architectures

## 📁 Repository Structure

```
AI_Agents/
├── 01_simple_react_agents/      # Basic ReAct pattern implementations
├── 02_langchain_agents/         # LangChain-based agents
├── 03_llamaindex_agents/        # LlamaIndex query and data agents
├── 04_tool_agents/              # Agents with custom tools
├── 05_knowledge_graph_agents/   # Graph-based reasoning agents
├── 06_multi_agent_systems/      # Collaborative agent systems
├── utils/                       # Shared utilities and helpers
├── notebooks/                   # Jupyter notebooks with examples
└── docs/                        # Additional documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip or conda for package management
- OpenAI API key (for LLM-based agents)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/BharathYedla/AI_Agents.git
cd AI_Agents
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

## 📚 Learning Path

Each directory contains examples progressing from basic to advanced:

1. **Start with Simple ReAct Agents** - Understand the fundamentals
2. **Explore LangChain Agents** - Learn framework-based development
3. **Try LlamaIndex Agents** - Work with data-centric agents
4. **Build Tool Agents** - Integrate external capabilities
5. **Experiment with Knowledge Graphs** - Add structured reasoning
6. **Create Multi-Agent Systems** - Design collaborative architectures

## 🛠️ Technologies Used

- **LLM Providers**: OpenAI, Anthropic
- **Agent Frameworks**: LangChain, LlamaIndex
- **Knowledge Graphs**: Neo4j, NetworkX, RDFLib
- **Vector Stores**: ChromaDB, FAISS
- **Development**: Python, Jupyter, pytest

## 📖 Documentation

Detailed documentation for each concept is available in the respective directories. Each example includes:

- Implementation code
- Explanation of concepts
- Usage examples
- Best practices

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Add new agent implementations
- Improve existing examples
- Fix bugs or issues
- Enhance documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

## ⚠️ Important Notes

- Always secure your API keys and never commit them to the repository
- Start with smaller, simpler agents before building complex systems
- Test agents thoroughly in development before production use
- Monitor API usage and costs when working with LLM providers 
