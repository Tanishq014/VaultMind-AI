# VaultMind AI Engine 🧠

This is the Python/FastAPI microservice for the VaultMind application. It acts as the "Brain" of the RAG (Retrieval-Augmented Generation) pipeline.

## Architecture
1. **Listens:** Receives ingestion requests from the Spring Boot backend.
2. **Fetches:** Downloads raw documents (PDFs, MD, TXT) from Cloudflare R2.
3. **Parses & Chunks:** Extracts text using `PyMuPDF` and splits it via `Langchain`.
4. **Embeds:** Converts text to vector embeddings.
5. **Stores:** Saves vectors to PostgreSQL via `pgvector`.

## Local Development Setup

### 1. Environment Activation
Ensure you are running the virtual environment:
\`\`\`bash
# Windows
.\venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate
\`\`\`

### 2. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Run the Server
\`\`\`bash
fastapi dev main.py
\`\`\`
*(Server will start on http://localhost:8000)*