"""
Simple Knowledge Graph Implementation

This module demonstrates how to create and query a basic knowledge graph
for use with AI agents.
"""

from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict, deque


class KnowledgeGraph:
    """
    A simple knowledge graph implementation using adjacency lists.
    
    Represents entities and relationships in a directed graph structure.
    """
    
    def __init__(self):
        """Initialize an empty knowledge graph."""
        self.graph: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
        self.entities: Set[str] = set()
        self.relationships: Set[str] = set()
    
    def add_triple(self, subject: str, predicate: str, obj: str):
        """
        Add a triple (subject, predicate, object) to the knowledge graph.
        
        Args:
            subject: The subject entity
            predicate: The relationship/predicate
            obj: The object entity
        """
        self.graph[subject].append((predicate, obj))
        self.entities.add(subject)
        self.entities.add(obj)
        self.relationships.add(predicate)
    
    def get_neighbors(self, entity: str, relationship: Optional[str] = None) -> List[Tuple[str, str]]:
        """
        Get neighbors of an entity.
        
        Args:
            entity: The entity to query
            relationship: Optional filter by relationship type
            
        Returns:
            List of (relationship, neighbor) tuples
        """
        neighbors = self.graph.get(entity, [])
        
        if relationship:
            return [(rel, neighbor) for rel, neighbor in neighbors if rel == relationship]
        return neighbors
    
    def find_path(self, start: str, end: str, max_depth: int = 5) -> Optional[List[Tuple[str, str, str]]]:
        """
        Find a path between two entities using BFS.
        
        Args:
            start: Starting entity
            end: Target entity
            max_depth: Maximum path length
            
        Returns:
            List of triples representing the path, or None if no path exists
        """
        if start not in self.entities or end not in self.entities:
            return None
        
        queue = deque([(start, [])])
        visited = {start}
        
        while queue:
            current, path = queue.popleft()
            
            if len(path) >= max_depth:
                continue
            
            if current == end:
                return path
            
            for relationship, neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [(current, relationship, neighbor)]
                    queue.append((neighbor, new_path))
        
        return None
    
    def query(self, subject: Optional[str] = None, 
              predicate: Optional[str] = None, 
              obj: Optional[str] = None) -> List[Tuple[str, str, str]]:
        """
        Query the knowledge graph with optional filters.
        
        Args:
            subject: Filter by subject
            predicate: Filter by predicate
            obj: Filter by object
            
        Returns:
            List of matching triples
        """
        results = []
        
        entities_to_check = [subject] if subject else self.entities
        
        for subj in entities_to_check:
            for pred, ob in self.graph.get(subj, []):
                if (predicate is None or pred == predicate) and \
                   (obj is None or ob == obj):
                    results.append((subj, pred, ob))
        
        return results
    
    def get_entity_info(self, entity: str) -> Dict[str, List[str]]:
        """
        Get all information about an entity.
        
        Args:
            entity: The entity to query
            
        Returns:
            Dictionary mapping relationships to lists of connected entities
        """
        info = defaultdict(list)
        
        for relationship, neighbor in self.get_neighbors(entity):
            info[relationship].append(neighbor)
        
        return dict(info)


class KnowledgeGraphAgent:
    """
    An agent that can reason over a knowledge graph.
    """
    
    def __init__(self, knowledge_graph: KnowledgeGraph):
        """
        Initialize the agent with a knowledge graph.
        
        Args:
            knowledge_graph: The knowledge graph to reason over
        """
        self.kg = knowledge_graph
    
    def answer_question(self, question: str) -> str:
        """
        Answer a question using the knowledge graph.
        This is a simplified implementation.
        
        Args:
            question: Natural language question
            
        Returns:
            Answer based on the knowledge graph
        """
        question_lower = question.lower()
        
        # Simple pattern matching for demo purposes
        if "what is" in question_lower or "who is" in question_lower:
            # Extract entity name (simplified)
            for entity in self.kg.entities:
                if entity.lower() in question_lower:
                    info = self.kg.get_entity_info(entity)
                    if info:
                        response = f"Information about {entity}:\n"
                        for rel, neighbors in info.items():
                            response += f"  {rel}: {', '.join(neighbors)}\n"
                        return response
                    return f"No information found about {entity}"
        
        elif "related" in question_lower or "connection" in question_lower:
            # Find relationships between entities
            entities_in_question = [e for e in self.kg.entities 
                                   if e.lower() in question_lower]
            
            if len(entities_in_question) >= 2:
                path = self.kg.find_path(entities_in_question[0], 
                                        entities_in_question[1])
                if path:
                    response = f"Path from {entities_in_question[0]} to {entities_in_question[1]}:\n"
                    for subj, pred, obj in path:
                        response += f"  {subj} --[{pred}]--> {obj}\n"
                    return response
                return f"No connection found between {entities_in_question[0]} and {entities_in_question[1]}"
        
        return "I couldn't understand the question. Try asking about specific entities or relationships."
    
    def get_all_facts(self) -> List[str]:
        """
        Get all facts in the knowledge graph as natural language.
        
        Returns:
            List of fact statements
        """
        facts = []
        for subject in self.kg.entities:
            for relationship, obj in self.kg.get_neighbors(subject):
                facts.append(f"{subject} {relationship} {obj}")
        return facts


def create_sample_knowledge_graph() -> KnowledgeGraph:
    """Create a sample knowledge graph with AI/ML concepts."""
    kg = KnowledgeGraph()
    
    # AI hierarchy
    kg.add_triple("Artificial Intelligence", "includes", "Machine Learning")
    kg.add_triple("Machine Learning", "includes", "Deep Learning")
    kg.add_triple("Machine Learning", "includes", "Supervised Learning")
    kg.add_triple("Machine Learning", "includes", "Unsupervised Learning")
    kg.add_triple("Deep Learning", "includes", "Neural Networks")
    
    # LLM relationships
    kg.add_triple("Large Language Models", "is_type_of", "Deep Learning")
    kg.add_triple("GPT", "is_example_of", "Large Language Models")
    kg.add_triple("BERT", "is_example_of", "Large Language Models")
    
    # AI Agents
    kg.add_triple("AI Agents", "uses", "Large Language Models")
    kg.add_triple("AI Agents", "uses", "Reasoning")
    kg.add_triple("ReAct", "is_type_of", "AI Agents")
    kg.add_triple("ReAct", "combines", "Reasoning")
    kg.add_triple("ReAct", "combines", "Action")
    
    # Frameworks
    kg.add_triple("LangChain", "is", "Framework")
    kg.add_triple("LangChain", "builds", "AI Agents")
    kg.add_triple("LlamaIndex", "is", "Framework")
    kg.add_triple("LlamaIndex", "builds", "AI Agents")
    
    return kg


def main():
    """Example usage of the knowledge graph and agent."""
    print("="*70)
    print("Knowledge Graph Agent Example")
    print("="*70)
    print()
    
    # Create knowledge graph
    kg = create_sample_knowledge_graph()
    
    print(f"Created knowledge graph with {len(kg.entities)} entities")
    print(f"and {len([t for e in kg.entities for t in kg.get_neighbors(e)])} relationships")
    print()
    
    # Create agent
    agent = KnowledgeGraphAgent(kg)
    
    # Show all facts
    print("Sample facts in the knowledge graph:")
    for i, fact in enumerate(agent.get_all_facts()[:10], 1):
        print(f"  {i}. {fact}")
    print()
    
    # Example queries
    print("Example Queries:")
    print("-" * 70)
    
    questions = [
        "What is Machine Learning?",
        "What is related to AI Agents?",
        "Is there a connection between Artificial Intelligence and Neural Networks?"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        answer = agent.answer_question(question)
        print(f"Answer: {answer}")
    
    # Direct graph queries
    print("\n" + "-" * 70)
    print("Direct Graph Queries:")
    print("-" * 70)
    
    print("\n1. Find path from 'Artificial Intelligence' to 'Neural Networks':")
    path = kg.find_path("Artificial Intelligence", "Neural Networks")
    if path:
        for subj, pred, obj in path:
            print(f"   {subj} --[{pred}]--> {obj}")
    
    print("\n2. All 'includes' relationships:")
    includes = kg.query(predicate="includes")
    for subj, pred, obj in includes:
        print(f"   {subj} {pred} {obj}")


if __name__ == "__main__":
    main()
