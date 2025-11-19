"""
Custom Tools for AI Agents

This module demonstrates how to create custom tools that agents can use
to interact with external systems and perform various tasks.
"""

from typing import Any, Dict, Optional, List
from datetime import datetime
import json
import math


class BaseTool:
    """Base class for all tools."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize a tool.
        
        Args:
            name: Tool name
            description: Description of what the tool does
        """
        self.name = name
        self.description = description
    
    def run(self, input_data: Any) -> str:
        """
        Execute the tool.
        
        Args:
            input_data: Input data for the tool
            
        Returns:
            Tool execution result
        """
        raise NotImplementedError("Subclasses must implement run method")


class CalculatorTool(BaseTool):
    """Tool for performing mathematical calculations."""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs mathematical calculations. Input should be a valid mathematical expression."
        )
    
    def run(self, expression: str) -> str:
        """
        Evaluate a mathematical expression.
        
        Args:
            expression: Mathematical expression to evaluate
            
        Returns:
            Result of the calculation
        """
        try:
            # Safe math operations
            safe_dict = {
                '__builtins__': {},
                'abs': abs,
                'max': max,
                'min': min,
                'pow': pow,
                'round': round,
                'sum': sum,
                'sqrt': math.sqrt,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'pi': math.pi,
                'e': math.e,
            }
            result = eval(expression, safe_dict, {})
            return f"Result: {result}"
        except Exception as e:
            return f"Error calculating '{expression}': {str(e)}"


class WeatherTool(BaseTool):
    """Tool for getting weather information (mock implementation)."""
    
    def __init__(self):
        super().__init__(
            name="weather",
            description="Gets weather information for a location. Input should be a city name."
        )
        self.mock_data = {
            "new york": {"temp": 72, "condition": "Sunny", "humidity": 45},
            "london": {"temp": 63, "condition": "Cloudy", "humidity": 70},
            "tokyo": {"temp": 75, "condition": "Clear", "humidity": 55},
            "paris": {"temp": 68, "condition": "Partly Cloudy", "humidity": 60},
        }
    
    def run(self, city: str) -> str:
        """
        Get weather for a city.
        
        Args:
            city: City name
            
        Returns:
            Weather information
        """
        city_lower = city.lower().strip()
        if city_lower in self.mock_data:
            weather = self.mock_data[city_lower]
            return (f"Weather in {city.title()}: "
                   f"{weather['condition']}, "
                   f"{weather['temp']}°F, "
                   f"Humidity: {weather['humidity']}%")
        else:
            return f"Weather data not available for {city}"


class DateTimeTool(BaseTool):
    """Tool for getting current date and time information."""
    
    def __init__(self):
        super().__init__(
            name="datetime",
            description="Gets current date and time. Input can be empty or a timezone."
        )
    
    def run(self, timezone: str = "") -> str:
        """
        Get current date and time.
        
        Args:
            timezone: Optional timezone (not implemented in this example)
            
        Returns:
            Current date and time
        """
        now = datetime.now()
        return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"


class SearchTool(BaseTool):
    """Tool for searching information (mock implementation)."""
    
    def __init__(self):
        super().__init__(
            name="search",
            description="Searches for information on a topic. Input should be a search query."
        )
        self.knowledge_base = {
            "ai agents": "AI agents are autonomous systems that perceive their environment and take actions to achieve goals.",
            "react": "ReAct (Reasoning and Acting) is a paradigm for AI agents that combines reasoning with action execution.",
            "langchain": "LangChain is a framework for developing applications powered by language models.",
            "llm": "Large Language Models (LLMs) are AI models trained on vast amounts of text data.",
        }
    
    def run(self, query: str) -> str:
        """
        Search for information.
        
        Args:
            query: Search query
            
        Returns:
            Search results
        """
        query_lower = query.lower().strip()
        
        # Simple keyword matching
        for key, value in self.knowledge_base.items():
            if key in query_lower:
                return f"Search result for '{query}': {value}"
        
        return f"No specific information found for '{query}'"


class FileWriteTool(BaseTool):
    """Tool for writing to files."""
    
    def __init__(self, base_path: str = "/tmp"):
        super().__init__(
            name="file_write",
            description="Writes content to a file. Input should be JSON with 'filename' and 'content'."
        )
        self.base_path = base_path
    
    def run(self, input_data: str) -> str:
        """
        Write content to a file.
        
        Args:
            input_data: JSON string with filename and content
            
        Returns:
            Success or error message
        """
        try:
            data = json.loads(input_data)
            filename = data.get("filename")
            content = data.get("content")
            
            if not filename or content is None:
                return "Error: Both 'filename' and 'content' are required"
            
            filepath = f"{self.base_path}/{filename}"
            with open(filepath, 'w') as f:
                f.write(content)
            
            return f"Successfully wrote to {filepath}"
        except json.JSONDecodeError:
            return "Error: Input must be valid JSON"
        except Exception as e:
            return f"Error writing file: {str(e)}"


class ToolRegistry:
    """Registry for managing available tools."""
    
    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}
    
    def register(self, tool: BaseTool):
        """Register a tool."""
        self.tools[tool.name] = tool
    
    def get_tool(self, name: str) -> Optional[BaseTool]:
        """Get a tool by name."""
        return self.tools.get(name)
    
    def list_tools(self) -> List[Dict[str, str]]:
        """List all available tools."""
        return [
            {"name": tool.name, "description": tool.description}
            for tool in self.tools.values()
        ]
    
    def execute_tool(self, name: str, input_data: Any) -> str:
        """Execute a tool by name."""
        tool = self.get_tool(name)
        if tool:
            return tool.run(input_data)
        else:
            return f"Error: Tool '{name}' not found"


def create_default_tool_registry() -> ToolRegistry:
    """Create a tool registry with default tools."""
    registry = ToolRegistry()
    
    registry.register(CalculatorTool())
    registry.register(WeatherTool())
    registry.register(DateTimeTool())
    registry.register(SearchTool())
    registry.register(FileWriteTool())
    
    return registry


def main():
    """Example usage of custom tools."""
    print("="*70)
    print("Custom Tools Example")
    print("="*70)
    print()
    
    # Create tool registry
    registry = create_default_tool_registry()
    
    # List available tools
    print("Available Tools:")
    for tool in registry.list_tools():
        print(f"  - {tool['name']}: {tool['description']}")
    print()
    
    # Example tool executions
    print("Example Tool Executions:")
    print("-" * 70)
    
    print("\n1. Calculator:")
    result = registry.execute_tool("calculator", "2 + 2 * 3")
    print(f"   Input: '2 + 2 * 3'")
    print(f"   Output: {result}")
    
    print("\n2. Weather:")
    result = registry.execute_tool("weather", "New York")
    print(f"   Input: 'New York'")
    print(f"   Output: {result}")
    
    print("\n3. DateTime:")
    result = registry.execute_tool("datetime", "")
    print(f"   Output: {result}")
    
    print("\n4. Search:")
    result = registry.execute_tool("search", "what are AI agents?")
    print(f"   Input: 'what are AI agents?'")
    print(f"   Output: {result}")
    
    print("\n5. File Write:")
    input_json = '{"filename": "test.txt", "content": "Hello, World!"}'
    result = registry.execute_tool("file_write", input_json)
    print(f"   Input: {input_json}")
    print(f"   Output: {result}")


if __name__ == "__main__":
    main()
