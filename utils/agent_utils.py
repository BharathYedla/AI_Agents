"""
Utility functions for AI Agents

This module provides common utilities used across different agent implementations.
"""

import os
import json
from typing import Any, Dict, Optional
from pathlib import Path


def load_api_key(service: str, env_var: Optional[str] = None) -> Optional[str]:
    """
    Load API key from environment variables.
    
    Args:
        service: Service name (e.g., 'openai', 'anthropic')
        env_var: Custom environment variable name (optional)
        
    Returns:
        API key or None if not found
    """
    if env_var:
        return os.getenv(env_var)
    
    # Try common environment variable patterns
    common_vars = [
        f"{service.upper()}_API_KEY",
        f"{service.upper()}_KEY",
        f"{service}_api_key"
    ]
    
    for var in common_vars:
        key = os.getenv(var)
        if key:
            return key
    
    return None


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from a JSON file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
    """
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in config file: {config_path}")
        return {}


def save_config(config: Dict[str, Any], config_path: str = "config.json"):
    """
    Save configuration to a JSON file.
    
    Args:
        config: Configuration dictionary
        config_path: Path to save configuration
    """
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)


def setup_logging(log_file: str = "agent.log", level: str = "INFO"):
    """
    Set up logging for agents.
    
    Args:
        log_file: Path to log file
        level: Logging level
    """
    import logging
    
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


def ensure_directory(path: str):
    """
    Ensure a directory exists, create if it doesn't.
    
    Args:
        path: Directory path
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def truncate_text(text: str, max_length: int = 1000, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def format_agent_response(response: str, agent_name: str = "Agent") -> str:
    """
    Format an agent's response for display.
    
    Args:
        response: Agent's response
        agent_name: Name of the agent
        
    Returns:
        Formatted response
    """
    border = "=" * 70
    return f"\n{border}\n{agent_name} Response:\n{border}\n{response}\n{border}\n"


def validate_environment():
    """
    Validate that required environment variables are set.
    
    Returns:
        Dictionary of validation results
    """
    results = {
        "openai_key": bool(os.getenv("OPENAI_API_KEY")),
        "anthropic_key": bool(os.getenv("ANTHROPIC_API_KEY")),
        "python_version": True  # Add actual version check if needed
    }
    
    return results


def print_validation_results():
    """Print environment validation results."""
    results = validate_environment()
    
    print("\nEnvironment Validation:")
    print("-" * 40)
    for key, value in results.items():
        status = "✓" if value else "✗"
        print(f"{status} {key}: {'Set' if value else 'Not set'}")
    print()


if __name__ == "__main__":
    print("Agent Utilities Module")
    print("=" * 70)
    print("\nAvailable utilities:")
    print("  - load_api_key(): Load API keys from environment")
    print("  - load_config(): Load configuration from JSON")
    print("  - setup_logging(): Configure logging")
    print("  - ensure_directory(): Create directories")
    print("  - truncate_text(): Truncate long text")
    print("  - format_agent_response(): Format agent output")
    print("  - validate_environment(): Check environment setup")
    print()
    
    print_validation_results()
