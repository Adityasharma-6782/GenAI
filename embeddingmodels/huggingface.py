from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",
)

text = [
        "who are you?",
        "what is your name?",
        "where are you from?"
]

# vector = embedding.embed_query("You are going to learn GenAI.")
vector = embeddings.embed_documents(texts=text)
print(vector)