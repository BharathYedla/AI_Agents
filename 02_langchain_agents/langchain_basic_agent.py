"""
LangChain Basic Agent Implementation

This module demonstrates how to create a basic agent using LangChain.
Note: Requires OpenAI API key to be set in environment variables.
"""

import os
from typing import List, Optional

# Note: These imports require langchain to be installed
# Uncomment when running with proper environment setup
"""
from langchain.agents import AgentType, initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
"""


class LangChainAgentExample:
    """
    Example class demonstrating LangChain agent setup and usage.
    
    This is a template that shows the structure of a LangChain agent.
    To use it, you need to:
    1. Install langchain and langchain-openai packages
    2. Set OPENAI_API_KEY environment variable
    3. Uncomment the imports above
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the LangChain agent.
        
        Args:
            api_key: OpenAI API key (optional, can use environment variable)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print("Warning: OPENAI_API_KEY not set. Agent will not function.")
        
    def create_tools(self) -> List:
        """
        Create a list of tools for the agent to use.
        
        Returns:
            List of Tool objects
        """
        # Example tool definitions
        # Uncomment when langchain is properly set up
        """
        tools = [
            Tool(
                name="Calculator",
                func=lambda x: str(eval(x)),
                description="Useful for math calculations. Input should be a math expression."
            ),
            Tool(
                name="Search",
                func=lambda x: f"Mock search result for: {x}",
                description="Useful for searching information. Input should be a search query."
            ),
        ]
        return tools
        """
        return []
    
    def create_agent(self):
        """
        Create and configure the LangChain agent.
        
        Returns:
            Configured agent executor
        """
        # Uncomment when langchain is properly set up
        """
        # Initialize the LLM
        llm = ChatOpenAI(
            temperature=0,
            model="gpt-3.5-turbo",
            openai_api_key=self.api_key
        )
        
        # Get tools
        tools = self.create_tools()
        
        # Initialize the agent
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            max_iterations=3,
            early_stopping_method="generate"
        )
        
        return agent
        """
        print("Agent creation template - requires LangChain setup")
        return None
    
    def run(self, query: str) -> str:
        """
        Run the agent with a query.
        
        Args:
            query: The question or task for the agent
            
        Returns:
            Agent's response
        """
        agent = self.create_agent()
        if agent:
            return agent.run(query)
        else:
            return "Agent not initialized. Please set up LangChain and OpenAI API key."


def example_usage():
    """
    Example demonstrating how to use the LangChain agent.
    """
    print("="*70)
    print("LangChain Agent Example")
    print("="*70)
    print()
    print("This is a template for creating LangChain agents.")
    print("To run this example:")
    print("1. Install required packages:")
    print("   pip install langchain langchain-openai openai")
    print("2. Set your OpenAI API key:")
    print("   export OPENAI_API_KEY='your-api-key-here'")
    print("3. Uncomment the code in this file")
    print()
    print("Example queries you could run:")
    print("- 'What is 25 * 4?'")
    print("- 'Search for information about AI agents'")
    print("- 'Calculate the square root of 144'")
    print()
    
    # Example instantiation (won't work without setup)
    agent_example = LangChainAgentExample()
    
    # This would work once properly configured:
    # result = agent_example.run("What is 25 * 4?")
    # print(f"Result: {result}")


def create_conversational_agent():
    """
    Example of creating a conversational agent with memory.
    This maintains context across multiple interactions.
    """
    # Uncomment when langchain is properly set up
    """
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    tools = [
        Tool(
            name="Calculator",
            func=lambda x: str(eval(x)),
            description="Useful for math calculations."
        )
    ]
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )
    
    return agent
    """
    print("Conversational agent template - requires LangChain setup")
    return None


if __name__ == "__main__":
    example_usage()
