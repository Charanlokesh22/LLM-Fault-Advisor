
from transformers import pipeline
from config import MODEL_NAME
from rag_pipeline import query_faiss
from ner_module import extract_entities

# Load LLM for inference
llm_pipeline = pipeline("text-generation", model=MODEL_NAME, device_map="auto")

def get_fault_diagnosis(user_input):
    # Step 1: NER extraction
    entities = extract_entities(user_input)
    
    # Step 2: RAG fallback search
    context_docs = query_faiss(user_input)
    context_str = "\n".join(context_docs)

    # Step 3: Prompt LLM
    prompt = f"""You are an industrial maintenance advisor.
Entities detected: {entities}
Context from database:
{context_str}

Question: {user_input}
Answer:"""

    response = llm_pipeline(prompt, max_new_tokens=200, do_sample=True)[0]['generated_text']
    return response
