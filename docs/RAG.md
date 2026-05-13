# VaultMind RAG Architecture

## Goal

VaultMind-Ai converts uploaded user files into private, searchable, AI-ready memory.

## Current Status

Phase 1: FastAPI service foundation.

## Planned Pipeline

1. Receive an indexing request from the VaultMind backend.
2. Extract text from the uploaded file.
3. Split extracted text into chunks.
4. Generate embeddings for each chunk.
5. Store chunks and vectors in PostgreSQL.
6. Retrieve relevant chunks for a user question.
7. Use an LLM to synthesize a grounded answer.

## Security Rules

- Spring Boot remains the system of record for authentication and file ownership.
- VaultMind-Ai must not trust user identity directly from the frontend.
- Every future chunk must be associated with `owner_user_id`.
- Every future embedding must be associated with `owner_user_id`.
- Every future retrieval query must filter by `owner_user_id`.