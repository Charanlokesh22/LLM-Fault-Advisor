LLM-powered Industrial Fault Detection & Maintenance Advisor

 Overview
This project demonstrates a domain-specific LLM application that:
- Uses LoRA fine-tuning concepts (simulated here with base models)
- Integrates RAG (Retrieval-Augmented Generation) with FAISS
- Performs NER-based entity extraction
- Runs a FastAPI API for real-time fault diagnosis



Features
- Real-time fault detection & maintenance advice**
- NER + RAG hybrid search for high reliability
- Scalable, modular architecture
- Works locally without massive GPU requirements


Tech Stack:
- Python
- Hugging Face Transformers
- LangChain
- FAISS
- FastAPI
- spaCy

Installation:

bash
Clone the repository
git clone https://github.com/Charanlokesh22/llm-fault-detection.git

 Navigate into the project folder
cd llm-fault-detection

 Install dependencies
pip install -r requirements.txt

 Download spaCy language model
python -m spacy download en_core_web_sm


Build Vector Index:
-python rag_pipeline.py


Run API:
-uvicorn app:app --reload


Example Usage:
-curl -X POST "http://127.0.0.1:8000/diagnose" -H "Content-Type: application/json" -d "\"Motor overheating in pump\""


Response:
{
  "diagnosis": "Detected overheating fault. Recommended action: Reduce load and allow cooling..."
}


