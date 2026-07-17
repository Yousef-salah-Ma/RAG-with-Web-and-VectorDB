import chromadb
from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(
    path="my_db"
)


collection = client.get_collection(
    "documents"
)


embed_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



def search(query, k=5):

    query_embedding = embed_model.encode(query)


    result = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=k
    )


    docs = result["documents"][0]


    context = "\n\n".join(docs)


    return context