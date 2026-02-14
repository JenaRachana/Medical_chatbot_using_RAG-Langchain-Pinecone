# Medical_chatbot_using_RAG-Langchain-Pinecone

# Medical Chatbot Using RAG, LangChain & Pinecone

A medical question-answering chatbot built using Retrieval-Augmented Generation (RAG) that uses LangChain for orchestration and Pinecone as a vector database. This project ingests medical documents, embeds them, and provides context-aware answers using an LLM.

---

## 🚀 Features

- 📄 Load and process medical documents (PDFs / text files)
- ✂️ Split large text into semantically useful chunks
- 🧠 Generate embeddings with an embedding model
- 🗂️ Store vectors in Pinecone vector database
- 🤖 Answer user queries using context retrieved from the vector store
- 🌐 Runs locally with a Flask-based chatbot UI

---

## 📦 Requirements

Before running, make sure you have:

- Python 3.10+
- Pinecone account & API key
- OpenAI API key (or other LLM provider)

Install dependencies with:

```bash
pip install -r requirements.txt

⚙️ Environment Variables

Create a .env file in the root directory with:
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_env
PINECONE_INDEX_NAME=medical-chatbot-index

🛠️ Build the Vector Index

Run this script once to create embeddings and store document vectors:
python store_index.py
It will:

Load data from data/ (PDF or text files)

Split text into chunks

Embed chunks with a vector embedding model

Upload to Pinecone index

🗣️ Start the Chatbot

After indexing, start the app:

python app.py


Open your browser and navigate to:

http://localhost:5000


Enter medical questions and get context-based answers.

📂 Directory Structure
├── data/                     # Medical documents to index
├── src/                      # Project source code
├── templates/                # Flask HTML templates
├── static/                  # CSS/JS for UI
├── store_index.py            # Builds Pinecone vector index
├── app.py                  # Chatbot application
├── requirements.txt
├── setup.py
├── .env.example              # Example env file
└── README.md

🧠 How It Works

Document loading: Text and PDFs are loaded and cleaned

Chunking: Large text is split into smaller overlapping chunks

Embedding: Each chunk is turned into a high-dimensional vector

Vector DB: Chunks are stored in Pinecone for fast semantic search

RAG Pipeline: User question → embed → search vectors → provide to LLM → generate answer

📌 Notes

Chunk size and overlap affect quality: a larger overlap preserves more context.

Ensure Pinecone index has the correct dimensionality matching embedding model.

This is for educational/demonstration purposes only — not medical advice.

🧪 Troubleshooting

Index not found: Check PINECONE_INDEX_NAME and env setup

Slow embedding: Larger docs take time — try smaller batches

LLM errors: Update API keys or check provider quotas

📜 License

This project is open source — modify and use it responsibly.


---

### Why this README structure matters

This format covers all essential aspects that a real README *should* have:

- Installation steps  
- Environment setup  
- Run steps  
- Project architecture  
- How RAG works  
- Troubleshooting  

It turns a nearly empty README into a **fully usable project documentation** — which is exactly what interviewers and collaborators expect in real projects.

---

If you want, I can also generate a **diagram version** or a **one-page summary slide** for presentations/interviews.
::contentReference[oaicite:0]{index=0}
