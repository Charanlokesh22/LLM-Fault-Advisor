
import pandas as pd
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from config import DATA_PATH, FAISS_INDEX_PATH, EMBEDDING_MODEL

def build_faiss_index():
    df = pd.read_csv(DATA_PATH)
    documents = [
        f"Fault: {row['fault_description']} | Action: {row['maintenance_action']}"
        for _, row in df.iterrows()
    ]
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = FAISS.from_texts(documents, embeddings)
    vectorstore.save_local(FAISS_INDEX_PATH)

def query_faiss(query):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    docs = vectorstore.similarity_search(query, k=2)
    return [doc.page_content for doc in docs]

if __name__ == "__main__":
    build_faiss_index()
    print(query_faiss("motor overheating"))
