"""
Multi-Agent System Implementation

This module demonstrates a simple multi-agent system where multiple agents
collaborate to solve complex tasks.
"""

from typing import List, Dict, Any, Optional
from enum import Enum
from dataclasses import dataclass
from abc import ABC, abstractmethod


class AgentRole(Enum):
    """Enumeration of agent roles in the system."""
    SUPERVISOR = "supervisor"
    RESEARCHER = "researcher"
    WRITER = "writer"
    REVIEWER = "reviewer"
    EXECUTOR = "executor"


@dataclass
class Message:
    """Message structure for inter-agent communication."""
    sender: str
    receiver: str
    content: str
    message_type: str
    metadata: Optional[Dict[str, Any]] = None


class BaseAgent(ABC):
    """Base class for all agents in the multi-agent system."""
    
    def __init__(self, name: str, role: AgentRole):
        """
        Initialize an agent.
        
        Args:
            name: Agent's name
            role: Agent's role
        """
        self.name = name
        self.role = role
        self.message_queue: List[Message] = []
    
    def receive_message(self, message: Message):
        """
        Receive a message from another agent.
        
        Args:
            message: The message to receive
        """
        self.message_queue.append(message)
    
    @abstractmethod
    def process_task(self, task: str) -> str:
        """
        Process a task assigned to this agent.
        
        Args:
            task: Task description
            
        Returns:
            Task result
        """
        pass
    
    def send_message(self, receiver: str, content: str, 
                    message_type: str = "info") -> Message:
        """
        Create a message to send to another agent.
        
        Args:
            receiver: Name of the receiving agent
            content: Message content
            message_type: Type of message
            
        Returns:
            Created message
        """
        return Message(
            sender=self.name,
            receiver=receiver,
            content=content,
            message_type=message_type
        )


class SupervisorAgent(BaseAgent):
    """
    Supervisor agent that coordinates other agents.
    """
    
    def __init__(self, name: str = "Supervisor"):
        super().__init__(name, AgentRole.SUPERVISOR)
        self.workers: Dict[str, BaseAgent] = {}
    
    def register_worker(self, agent: BaseAgent):
        """Register a worker agent."""
        self.workers[agent.name] = agent
    
    def decompose_task(self, task: str) -> List[tuple[str, str]]:
        """
        Decompose a complex task into subtasks.
        
        Args:
            task: Complex task description
            
        Returns:
            List of (agent_role, subtask) tuples
        """
        # Simplified task decomposition
        if "research" in task.lower():
            return [
                ("researcher", "Research the topic"),
                ("writer", "Write a summary"),
                ("reviewer", "Review the content")
            ]
        elif "analysis" in task.lower():
            return [
                ("researcher", "Gather data"),
                ("executor", "Analyze data"),
                ("writer", "Create report")
            ]
        else:
            return [("executor", task)]
    
    def process_task(self, task: str) -> str:
        """
        Process a task by coordinating workers.
        
        Args:
            task: Task to coordinate
            
        Returns:
            Final result
        """
        print(f"\n{self.name}: Coordinating task: '{task}'")
        
        subtasks = self.decompose_task(task)
        results = []
        
        for role, subtask in subtasks:
            # Find an agent with the required role
            agent = self._find_agent_by_role(role)
            
            if agent:
                print(f"{self.name}: Assigning to {agent.name}: {subtask}")
                result = agent.process_task(subtask)
                results.append(result)
            else:
                print(f"{self.name}: No agent found for role {role}")
        
        # Aggregate results
        final_result = self._aggregate_results(results)
        print(f"{self.name}: Task completed!")
        return final_result
    
    def _find_agent_by_role(self, role: str) -> Optional[BaseAgent]:
        """Find an agent with a specific role."""
        for agent in self.workers.values():
            if agent.role.value == role:
                return agent
        return None
    
    def _aggregate_results(self, results: List[str]) -> str:
        """Aggregate results from multiple agents."""
        return "\n\n".join([f"Step {i+1}: {result}" 
                           for i, result in enumerate(results)])


class ResearcherAgent(BaseAgent):
    """Agent specialized in research tasks."""
    
    def __init__(self, name: str = "Researcher"):
        super().__init__(name, AgentRole.RESEARCHER)
        self.knowledge_base = {
            "AI agents": "AI agents are autonomous systems that can perceive and act.",
            "multi-agent": "Multi-agent systems involve multiple cooperating agents.",
            "LLM": "Large Language Models are trained on vast text corpora."
        }
    
    def process_task(self, task: str) -> str:
        """Research information related to the task."""
        print(f"  {self.name}: Researching...")
        
        # Simple keyword matching
        findings = []
        for key, value in self.knowledge_base.items():
            if key in task.lower():
                findings.append(value)
        
        if findings:
            return f"Research findings: {' '.join(findings)}"
        return "Research findings: General information gathered."


class WriterAgent(BaseAgent):
    """Agent specialized in writing and content creation."""
    
    def __init__(self, name: str = "Writer"):
        super().__init__(name, AgentRole.WRITER)
    
    def process_task(self, task: str) -> str:
        """Create written content based on the task."""
        print(f"  {self.name}: Writing content...")
        
        # Check for recent research in message queue
        research_data = self._get_research_data()
        
        content = f"Content created based on: {task}"
        if research_data:
            content += f"\nIncorporating research: {research_data}"
        
        return content
    
    def _get_research_data(self) -> str:
        """Extract research data from messages."""
        for message in self.message_queue:
            if message.message_type == "research_result":
                return message.content
        return ""


class ReviewerAgent(BaseAgent):
    """Agent specialized in reviewing and quality assurance."""
    
    def __init__(self, name: str = "Reviewer"):
        super().__init__(name, AgentRole.REVIEWER)
    
    def process_task(self, task: str) -> str:
        """Review content and provide feedback."""
        print(f"  {self.name}: Reviewing...")
        
        # Simple review checks
        issues = []
        if len(task) < 20:
            issues.append("Content seems too brief")
        
        if issues:
            return f"Review complete. Issues found: {', '.join(issues)}"
        return "Review complete. Content approved."


class ExecutorAgent(BaseAgent):
    """General-purpose executor agent."""
    
    def __init__(self, name: str = "Executor"):
        super().__init__(name, AgentRole.EXECUTOR)
    
    def process_task(self, task: str) -> str:
        """Execute a general task."""
        print(f"  {self.name}: Executing task...")
        return f"Task executed: {task}"


class MultiAgentSystem:
    """
    Multi-agent system that manages multiple agents.
    """
    
    def __init__(self):
        """Initialize the multi-agent system."""
        self.agents: Dict[str, BaseAgent] = {}
        self.supervisor: Optional[SupervisorAgent] = None
    
    def add_agent(self, agent: BaseAgent):
        """Add an agent to the system."""
        self.agents[agent.name] = agent
        
        if isinstance(agent, SupervisorAgent):
            self.supervisor = agent
    
    def setup_default_system(self):
        """Set up a default multi-agent system."""
        # Create supervisor
        supervisor = SupervisorAgent()
        
        # Create worker agents
        researcher = ResearcherAgent()
        writer = WriterAgent()
        reviewer = ReviewerAgent()
        executor = ExecutorAgent()
        
        # Register workers with supervisor
        supervisor.register_worker(researcher)
        supervisor.register_worker(writer)
        supervisor.register_worker(reviewer)
        supervisor.register_worker(executor)
        
        # Add all agents to system
        self.add_agent(supervisor)
        self.add_agent(researcher)
        self.add_agent(writer)
        self.add_agent(reviewer)
        self.add_agent(executor)
    
    def execute_task(self, task: str) -> str:
        """
        Execute a task using the multi-agent system.
        
        Args:
            task: Task to execute
            
        Returns:
            Task result
        """
        if not self.supervisor:
            return "No supervisor agent available"
        
        return self.supervisor.process_task(task)


def main():
    """Example usage of the multi-agent system."""
    print("="*70)
    print("Multi-Agent System Example")
    print("="*70)
    
    # Create and setup system
    system = MultiAgentSystem()
    system.setup_default_system()
    
    print(f"\nSystem initialized with {len(system.agents)} agents:")
    for agent in system.agents.values():
        print(f"  - {agent.name} ({agent.role.value})")
    
    # Example tasks
    tasks = [
        "Research about AI agents and create a summary",
        "Perform analysis on the data",
        "Execute a simple task"
    ]
    
    for i, task in enumerate(tasks, 1):
        print(f"\n{'='*70}")
        print(f"Task {i}: {task}")
        print(f"{'='*70}")
        
        result = system.execute_task(task)
        
        print(f"\n{'-'*70}")
        print("Final Result:")
        print(f"{'-'*70}")
        print(result)


if __name__ == "__main__":
    main()
