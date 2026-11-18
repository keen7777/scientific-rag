# Scientific RAG

A fully local, persistent Retrieval-Augmented Generation (RAG) system for scientific literature.

## Overview

Scientific RAG aims to provide reliable, evidence-grounded question answering over scientific papers.

The system will support:

- PDF ingestion with page-level metadata
- Text chunking and embedding generation
- Persistent vector storage and semantic retrieval
- Local LLM inference using Ollama
- Source-grounded answers with verifiable citations
- Retrieval and generation evaluation

The architecture is designed to support future cloud LLM integration and reuse of core RAG components in other applications.

## Tech Stack

- **Language:** Python 3.12
- **PDF Processing:** PyMuPDF
- **Local LLM:** Qwen 2.5 7B via Ollama
- **Testing:** pytest
- **Environment:** Python venv

Additional dependencies will be introduced as the project evolves.

## Getting Started

Create and activate the virtual environment:

```bash
conda create -n scientific-rag python=3.12 pip
conda activate scientific-rag
python -m pip install -e ".[dev]"
```

Install the project and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Testing

Run the test suite:

```bash
python -m pytest
```

## Development Status

**Milestone 1 — PDF Ingestion (In Progress)**

The current focus is on reliable page-level text extraction from scientific PDF documents, preserving metadata required for downstream retrieval and citation generation.

## License

To be determined.