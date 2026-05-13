# VaultMind-Ai Architecture Decisions

## 01 | Separate FastAPI Service for AI/RAG Processing

**Status:** Proposed

### Problem

VaultMind is transitioning from a secure file vault into an AI-native private memory system. AI/RAG workloads such as text extraction, chunking, embeddings, and retrieval have different runtime and library requirements than the Spring Boot product backend.

### Decision

Create a separate `VaultMind-Ai` FastAPI service responsible for AI/RAG processing, while keeping Spring Boot as the system of record for authentication, users, file metadata, and authorization.

### Rationale

FastAPI provides a Python-native environment for AI libraries, embedding models, text extraction tools, and future LLM orchestration. Separating this from Spring Boot prevents the core product backend from becoming tightly coupled to ML-specific dependencies.

### Consequences

- The system gains a clean service boundary between product logic and AI processing.
- Spring Boot remains responsible for user authorization and ownership.
- VaultMind-Ai can evolve independently as the RAG system becomes more complex.
- Cross-service communication must be designed carefully before production use.