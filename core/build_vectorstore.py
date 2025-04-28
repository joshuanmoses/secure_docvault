# core/build_vectorstore.py

from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

# Path where your decrypted documents are temporarily read
VAULT_PATH = "data/vault"

def load_documents():
    documents = []
    metadata = []
    for folder in os.listdir(VAULT_PATH):
        folder_path = os.path.join(VAULT_PATH, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith('.enc'):
                    # In production, you'd decrypt the file here
                    documents.append(f"Dummy content of {file} in {folder}")  # Placeholder
                    metadata.append((folder, file))
    return documents, metadata

def create_vectorstore(documents, metadata):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(documents)

    # Build FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Save index + metadata
    vectorstore = {
        "index": index,
        "metadata": metadata
    }

    with open('models/vectorstore.pkl', 'wb') as f:
        pickle.dump(vectorstore, f)

    print("[+] Vectorstore built and saved as models/vectorstore.pkl")

if __name__ == "__main__":
    documents, metadata = load_documents()
    if documents:
        create_vectorstore(documents, metadata)
    else:
        print("[!] No documents found in vault to index.")
