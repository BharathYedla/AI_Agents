"""
Simple ReAct Agent Implementation

This module demonstrates a basic ReAct (Reasoning and Acting) agent
that can reason about problems and take actions to solve them.
"""

from typing import List, Dict, Any, Optional
import json


class SimpleReActAgent:
    """
    A basic ReAct agent that follows the Thought-Action-Observation pattern.
    
    The agent:
    1. Receives a question/task
    2. Thinks about what to do (Thought)
    3. Takes an action (Action)
    4. Observes the result (Observation)
    5. Repeats until the task is complete
    """
    
    def __init__(self, max_iterations: int = 5):
        """
        Initialize the ReAct agent.
        
        Args:
            max_iterations: Maximum number of reasoning iterations
        """
        self.max_iterations = max_iterations
        self.tools = self._initialize_tools()
        
    def _initialize_tools(self) -> Dict[str, callable]:
        """Initialize available tools for the agent."""
        return {
            "calculator": self._calculator_tool,
            "search": self._search_tool,
            "finish": self._finish_tool,
        }
    
    def _calculator_tool(self, expression: str) -> str:
        """
        Simple calculator tool.
        
        Args:
            expression: Mathematical expression to evaluate
            
        Returns:
            Result of the calculation
        """
        try:
            # Safe evaluation of basic math expressions
            result = eval(expression, {"__builtins__": {}}, {})
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _search_tool(self, query: str) -> str:
        """
        Mock search tool (would connect to real search API in production).
        
        Args:
            query: Search query
            
        Returns:
            Mock search results
        """
        # This is a mock implementation
        mock_results = {
            "weather": "The weather is sunny, 72°F",
            "capital": "The capital is Washington, D.C.",
            "population": "The population is approximately 331 million",
        }
        
        for key, value in mock_results.items():
            if key in query.lower():
                return value
        
        return "No relevant results found"
    
    def _finish_tool(self, answer: str) -> str:
        """
        Finish tool to return the final answer.
        
        Args:
            answer: Final answer to return
            
        Returns:
            The final answer
        """
        return answer
    
    def run(self, question: str) -> str:
        """
        Run the ReAct agent on a question.
        
        Args:
            question: The question or task to solve
            
        Returns:
            The final answer
        """
        print(f"\n{'='*60}")
        print(f"Question: {question}")
        print(f"{'='*60}\n")
        
        for iteration in range(self.max_iterations):
            print(f"--- Iteration {iteration + 1} ---")
            
            # Thought: Reason about what to do
            thought = self._generate_thought(question, iteration)
            print(f"Thought: {thought}")
            
            # Action: Decide what action to take
            action, action_input = self._generate_action(thought)
            print(f"Action: {action}({action_input})")
            
            # Observation: Execute the action and observe the result
            if action in self.tools:
                observation = self.tools[action](action_input)
                print(f"Observation: {observation}\n")
                
                if action == "finish":
                    return observation
            else:
                observation = f"Error: Unknown action '{action}'"
                print(f"Observation: {observation}\n")
        
        return "Maximum iterations reached without finding an answer."
    
    def _generate_thought(self, question: str, iteration: int) -> str:
        """
        Generate a thought based on the question and current iteration.
        This is a simplified version - in a real agent, this would use an LLM.
        
        Args:
            question: The original question
            iteration: Current iteration number
            
        Returns:
            A thought about what to do next
        """
        # Simplified reasoning - in production, use an LLM here
        if iteration == 0:
            if "calculate" in question.lower() or any(op in question for op in ['+', '-', '*', '/']):
                return "I need to perform a calculation to answer this question."
            else:
                return "I need to search for information to answer this question."
        else:
            return "I have enough information to provide the final answer."
    
    def _generate_action(self, thought: str) -> tuple[str, str]:
        """
        Generate an action based on the thought.
        This is a simplified version - in a real agent, this would use an LLM.
        
        Args:
            thought: The current thought
            
        Returns:
            Tuple of (action_name, action_input)
        """
        # Simplified action selection - in production, use an LLM here
        if "calculation" in thought.lower():
            return ("calculator", "2 + 2")
        elif "search" in thought.lower():
            return ("search", "weather")
        else:
            return ("finish", "Based on the information gathered, here is the answer.")


def main():
    """Example usage of the SimpleReActAgent."""
    agent = SimpleReActAgent(max_iterations=3)
    
    # Example 1: Simple calculation
    print("\n" + "="*70)
    print("EXAMPLE 1: Calculation")
    print("="*70)
    result = agent.run("What is 2 + 2?")
    print(f"\nFinal Answer: {result}")
    
    # Example 2: Information retrieval
    print("\n" + "="*70)
    print("EXAMPLE 2: Information Retrieval")
    print("="*70)
    result = agent.run("What is the weather like?")
    print(f"\nFinal Answer: {result}")


if __name__ == "__main__":
    main()
