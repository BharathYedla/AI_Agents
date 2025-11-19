# Knowledge Graph Agents

This directory contains implementations of agents that use knowledge graphs for structured reasoning and information retrieval.

## What are Knowledge Graphs?

Knowledge graphs represent information as nodes (entities) and edges (relationships). They enable:
- Structured knowledge representation
- Complex relationship queries
- Multi-hop reasoning
- Semantic understanding

## Examples in this Directory

- `simple_knowledge_graph.py` - Basic knowledge graph implementation
- `neo4j_agent.py` - Agent using Neo4j graph database
- `networkx_agent.py` - Agent using NetworkX for graph operations
- `rdf_agent.py` - Agent working with RDF triples
- `graph_rag_agent.py` - Retrieval-Augmented Generation with graphs

## Knowledge Graph Concepts

### Entities and Relations
- **Entities**: People, places, things, concepts
- **Relations**: Connections between entities
- **Properties**: Attributes of entities

### Graph Types
- **Property Graphs**: Nodes and edges with properties (Neo4j)
- **RDF Graphs**: Subject-Predicate-Object triples
- **Directed Graphs**: Edges have direction
- **Multigraphs**: Multiple edges between nodes

## Use Cases

1. **Question Answering**: Answer complex queries by traversing graphs
2. **Recommendation**: Find related items through graph structure
3. **Knowledge Discovery**: Uncover hidden relationships
4. **Semantic Search**: Find entities based on meaning

## Building a Knowledge Graph Agent

```python
from networkx import DiGraph

# Create graph
graph = DiGraph()
graph.add_edge("AI", "Machine Learning", relationship="includes")
graph.add_edge("Machine Learning", "Deep Learning", relationship="includes")

# Query graph
path = find_path(graph, "AI", "Deep Learning")
```

## Graph Query Languages

- **Cypher**: Neo4j's query language
- **SPARQL**: RDF query language
- **Gremlin**: Apache TinkerPop traversal language

## Integration with LLMs

Knowledge graphs can enhance LLMs by:
- Providing structured context
- Enabling fact verification
- Supporting multi-hop reasoning
- Grounding responses in facts

## References

- [Neo4j Documentation](https://neo4j.com/docs/)
- [NetworkX Documentation](https://networkx.org/)
- [Knowledge Graphs Paper](https://arxiv.org/abs/2003.02320)
