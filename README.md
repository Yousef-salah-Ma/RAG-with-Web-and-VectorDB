# Hybrid-RAG-Agent

A Hybrid Retrieval-Augmented Generation (RAG) system built from scratch using a local Qwen model, ChromaDB, and Tavily Search. The system uses an LLM-based router to dynamically choose between web search and private vector database retrieval.

## Features

- Local Qwen2.5-3B-Instruct
- Hybrid Retrieval (Web + Private Knowledge)
- ChromaDB Vector Database
- Sentence Transformers Embeddings
- Tavily Web Search
- Custom LLM Router
- Modular Project Structure

## Project Structure

```
Hybrid-RAG-Agent/
│
├── app.py
├── model.py
├── router.py
├── search.py
├── generator.py
├── prompt.py
├── requirements.txt
├── README.md
├── my_db/
└── data/
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Yousef-salah-Ma/RAG-with-Web-and-VectorDB.git
cd Hybrid-RAG-Agent
```

### 2. Create a virtual environment

Using Conda:

```bash
conda create -n rag python=3.11
conda activate rag
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Tavily API Key

Create a `.env` file:

```text
TAVILY_API_KEY=YOUR_API_KEY
```

or set it as an environment variable.

### 5. Build the Vector Database

Place your documents inside the data folder, then run the indexing script (if applicable).

### 6. Run the application

```bash
python app.py
```

Example:

```
Enter question:
What is XSS?
```

Output:

```
XSS stands for Cross-Site Scripting...
```

---

## Technologies

- Python
- Qwen2.5-3B-Instruct
- Hugging Face Transformers
- ChromaDB
- Sentence Transformers
- Tavily Search API
- PyTorch

---

## Architecture

```
            User
              │
              ▼
        LLM Router
       /          \
      ▼            ▼
Web Search   Private Search
      \          /
       ▼        ▼
     Retrieved Context
             │
             ▼
        Qwen Generator
             │
             ▼
       Final Response
```

---

## Future Improvements

- Conversation Memory
- Multi-tool Agent
- FastAPI REST API
- Streaming Responses
- LangGraph Integration
- Docker Support
- Evaluation Pipeline
