# Chapter 5: Building a RAG-Based Movie Recommendation System

## Overview
This project demonstrates the development of an intelligent Movie Recommendation System using Retrieval-Augmented Generation (RAG). By combining vector search with a Large Language Model (LLM), the system provides personalized, context-aware movie suggestions based on natural language queries.

## System Design & Architecture

The system is built upon a modern RAG pipeline designed for accuracy and efficiency.

### 1. Data Ingestion & Processing
-   **Source Data**: Movie descriptions and metadata.
-   **Chunking Strategy**: The notebook explores various text splitting techniques to optimize retrieval:
    -   *RecursiveCharacterTextSplitter*: Respects document structure.
    -   *MarkdownTextSplitter* & *HTMLHeaderTextSplitter*: Structure-aware splitting.
    -   *Proposition Chunking*: Breaks text into independent, meaningful propositions for precise retrieval.

### 2. Vector Storage
-   **Database**: **ChromaDB** is used as the vector store to index and manage movie embeddings.
-   **Embeddings**: Movie descriptions are converted into dense vector representations using **Sentence Transformers** (`all-MiniLM-L6-v2`), enabling semantic understanding of the content.

### 3. Retrieval System
-   **Semantic Search**: When a user asks a question (e.g., "What are good movies for a rainy day?"), the system converts the query into a vector and retrieves the top-k most relevant movie chunks from ChromaDB using cosine similarity.

### 4. Generative Response
-   **LLM**: **Mistral-7B-Instruct-v0.1** is employed to synthesize the retrieved information.
-   **Context Integration**: Retrieved movie titles and descriptions are fed as context into the LLM prompt.
-   **Output**: The model generates a natural language response recommending specific movies and explaining *why* they fit the user's request.

### 5. Optimization & Performance
To ensure the system is production-ready and cost-effective, the following optimizations are demonstrated:
-   **Quantization**: Implementation of Binary and Int8 quantization to reduce memory footprint and increase retrieval speed without significant accuracy loss.
-   **Matryoshka Embeddings**: Techniques to truncate embedding dimensions (e.g., from 768 to 128), drastically reducing storage costs and latency.

## Business Value & Product Aspects

### Enhanced User Experience
Unlike traditional keyword-based search, this system understands *intent*. Users can ask vague or thematic questions ("inspiring movies about underdogs"), and the semantic search bridges the gap to find relevant content, leading to higher user engagement and satisfaction.

### Scalability
-   **Vector Search**: ChromaDB scales efficiently to handle large catalogs of movies.
-   **Storage Optimization**: The use of quantization and Matryoshka embeddings reduces the infrastructure costs associated with storing millions of vectors, making the solution viable for large-scale deployments.

### Cost Efficiency
-   **Open Source Models**: Utilizing Mistral-7B and Sentence Transformers avoids per-token costs associated with proprietary APIs.
-   **Resource Management**: Optimization techniques allow the system to run on smaller, less expensive hardware instances.

## How to Run

1.  **Environment Setup**:
    Ensure you have the required dependencies installed.
    ```bash
    pip install -r requirements.txt
    ```
    *Note: Key packages include `langchain`, `chromadb`, `transformers`, `sentence-transformers`, `llama-index`.*

2.  **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook "Chapter V.ipynb"
    ```

3.  **Execute Cells**:
    Run the notebook cells sequentially to:
    -   Load and process movie data.
    -   Generate embeddings and populate ChromaDB.
    -   Run the RAG pipeline to generate recommendations.
