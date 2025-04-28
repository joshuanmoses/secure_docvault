from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_index(documents):
    embeddings = model.encode(documents)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def save_index(index):
    faiss.write_index(index, 'models/vectorstore.pkl')

def load_index():
    return faiss.read_index('models/vectorstore.pkl')

def search_index(query, documents):
    index = load_index()
    query_vector = model.encode([query])
    D, I = index.search(query_vector, k=5)
    return [documents[i] for i in I[0]]
