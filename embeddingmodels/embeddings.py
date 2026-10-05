from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    dimensions=64
)

text = [
        "who are you?",
        "what is your name?",
        "where are you from?"
]

# vector = embedding.embed_query("You are going to learn GenAI.")
vector = embedding.embed_documents(texts=text)
print(vector)