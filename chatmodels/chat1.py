from dotenv import load_dotenv
load_dotenv()

# ---------use of init_chat_model---------------
# from langchain.chat_models import init_chat_model
# model = init_chat_model("groq:openai/gpt-oss-120b")

# responce = model.invoke("What is Machine Learning?")
# print(responce.content)
# ------------------------------------------------

# -----------use modelClass-----------------
from langchain_groq import ChatGroq
model = ChatGroq(model="openai/gpt-oss-120b",temperature=0)

response = model.invoke("What is Python?")
print(response.content)
# -------------------------------------------