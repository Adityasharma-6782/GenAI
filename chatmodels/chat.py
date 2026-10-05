from dotenv import load_dotenv

load_dotenv()

# ----------use init_chat_model---------------
# from langchain.chat_models import init_chat_model # this is the use of init_chat_model
# model = init_chat_model("google_genai:gemini-3.7-flash")
# --------------------------------------------

# ---------use model class----------

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model = "gemini-3.7-flash", temperature=0, max_tokens=20) # temperature is optional, default is 0.7(it's ramhe 0 to 1, 0 means logical answer, 1 means creative answer)
# max_tokens ==> The maximum number of tokens to generate in the chat response. This limits the length of the output.


responce = model.invoke("what you thimk about Arya college of engineering?")
print(responce.content)
