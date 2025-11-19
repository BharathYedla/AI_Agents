"""
LlamaIndex Query Agent Implementation

This module demonstrates how to create a query agent using LlamaIndex.
Query agents can reason over your data and answer questions.
"""

import os
from typing import List, Optional
from pathlib import Path

# Note: These imports require llama-index to be installed
# Uncomment when running with proper environment setup
"""
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
    StorageContext,
)
from llama_index.llms import OpenAI
from llama_index.agent import OpenAIAgent
from llama_index.tools import QueryEngineTool, ToolMetadata
"""


class LlamaIndexQueryAgent:
    """
    Example class demonstrating LlamaIndex query agent setup.
    
    This agent can:
    1. Index documents from a directory
    2. Answer questions about the documents
    3. Use multiple query engines as tools
    """
    
    def __init__(self, data_path: Optional[str] = None, api_key: Optional[str] = None):
        """
        Initialize the LlamaIndex query agent.
        
        Args:
            data_path: Path to documents directory
            api_key: OpenAI API key (optional, can use environment variable)
        """
        self.data_path = data_path
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print("Warning: OPENAI_API_KEY not set. Agent will not function.")
    
    def load_documents(self, data_path: str):
        """
        Load documents from a directory.
        
        Args:
            data_path: Path to the directory containing documents
            
        Returns:
            List of loaded documents
        """
        # Uncomment when llama-index is properly set up
        """
        reader = SimpleDirectoryReader(data_path)
        documents = reader.load_data()
        return documents
        """
        print(f"Would load documents from: {data_path}")
        return []
    
    def create_index(self, documents):
        """
        Create a vector store index from documents.
        
        Args:
            documents: List of documents to index
            
        Returns:
            VectorStoreIndex
        """
        # Uncomment when llama-index is properly set up
        """
        llm = OpenAI(model="gpt-3.5-turbo", api_key=self.api_key)
        service_context = ServiceContext.from_defaults(llm=llm)
        
        index = VectorStoreIndex.from_documents(
            documents,
            service_context=service_context
        )
        return index
        """
        print("Would create index from documents")
        return None
    
    def create_query_agent(self, indices: List = None):
        """
        Create a query agent with multiple query engines as tools.
        
        Args:
            indices: List of indices to create query engines from
            
        Returns:
            OpenAIAgent
        """
        # Uncomment when llama-index is properly set up
        """
        tools = []
        
        for idx, index in enumerate(indices):
            query_engine = index.as_query_engine()
            
            tool = QueryEngineTool(
                query_engine=query_engine,
                metadata=ToolMetadata(
                    name=f"document_query_{idx}",
                    description=f"Useful for querying document set {idx}"
                )
            )
            tools.append(tool)
        
        llm = OpenAI(model="gpt-3.5-turbo", api_key=self.api_key)
        agent = OpenAIAgent.from_tools(tools, llm=llm, verbose=True)
        
        return agent
        """
        print("Would create query agent with tools")
        return None
    
    def query(self, question: str) -> str:
        """
        Query the agent with a question.
        
        Args:
            question: The question to ask
            
        Returns:
            Agent's response
        """
        if not self.data_path:
            return "No data path provided. Please provide a path to documents."
        
        # Full workflow (uncomment when properly set up):
        """
        documents = self.load_documents(self.data_path)
        index = self.create_index(documents)
        agent = self.create_query_agent([index])
        response = agent.query(question)
        return str(response)
        """
        
        return "Agent not initialized. Please set up LlamaIndex and OpenAI API key."


def example_basic_query():
    """
    Example of basic document querying with LlamaIndex.
    """
    print("="*70)
    print("LlamaIndex Query Agent Example")
    print("="*70)
    print()
    print("This is a template for creating LlamaIndex query agents.")
    print("To run this example:")
    print("1. Install required packages:")
    print("   pip install llama-index openai")
    print("2. Set your OpenAI API key:")
    print("   export OPENAI_API_KEY='your-api-key-here'")
    print("3. Prepare some documents in a directory")
    print("4. Uncomment the code in this file")
    print()
    print("Example usage:")
    print("agent = LlamaIndexQueryAgent(data_path='./documents')")
    print("response = agent.query('What are the main topics discussed?')")
    print()


def example_multi_document_agent():
    """
    Example of creating an agent that works with multiple document sets.
    """
    # Uncomment when llama-index is properly set up
    """
    # Load different document sets
    docs_1 = SimpleDirectoryReader("./documents/set1").load_data()
    docs_2 = SimpleDirectoryReader("./documents/set2").load_data()
    
    # Create indices
    index_1 = VectorStoreIndex.from_documents(docs_1)
    index_2 = VectorStoreIndex.from_documents(docs_2)
    
    # Create query engines as tools
    tool_1 = QueryEngineTool(
        query_engine=index_1.as_query_engine(),
        metadata=ToolMetadata(
            name="company_docs",
            description="Contains company policies and procedures"
        )
    )
    
    tool_2 = QueryEngineTool(
        query_engine=index_2.as_query_engine(),
        metadata=ToolMetadata(
            name="technical_docs",
            description="Contains technical documentation"
        )
    )
    
    # Create agent
    agent = OpenAIAgent.from_tools([tool_1, tool_2], verbose=True)
    
    # Query the agent
    response = agent.query("What is the vacation policy?")
    print(response)
    """
    print("Multi-document agent template - requires LlamaIndex setup")


if __name__ == "__main__":
    example_basic_query()
