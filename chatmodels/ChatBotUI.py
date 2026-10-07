import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="ChatBot", page_icon="🤖")

model = ChatGroq(model="openai/gpt-oss-120b", temperature=1)

SYSTEM_PROMPT = """You are an AI assistant with the personality of a senior educator.

                    Speak naturally in Hinglish unless the user prefers another language. """

# This is use to maintain the history of the ChatBot (sent to the model).
if "message" not in st.session_state:
    st.session_state.message = [SystemMessage(content=SYSTEM_PROMPT)]

# Only used to draw the chat bubbles in the UI.
if "display" not in st.session_state:
    st.session_state.display = []

if "ended" not in st.session_state:
    st.session_state.ended = False

st.title("Welcome in ChatBot")

# Show previous conversation
for role, content in st.session_state.display:
    with st.chat_message(role):
        st.markdown(content)

if st.session_state.ended:
    st.info("Thankyou for using my ChatBot")
    if st.button("Start new chat"):
        st.session_state.message = [SystemMessage(content=SYSTEM_PROMPT)]
        st.session_state.display = []
        st.session_state.ended = False
        st.rerun()
else:
    txt = st.chat_input("Type your message... (type 'exit' to end)")

    if txt:
        st.session_state.message.append(HumanMessage(content=txt))

        if txt == "exit":
            st.session_state.message.clear()
            st.session_state.ended = True
            st.rerun()

        st.session_state.display.append(("user", txt))
        with st.chat_message("user"):
            st.markdown(txt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.invoke(st.session_state.message)
            st.markdown(response.content)

        # Same role handling as the original code
        st.session_state.message.append(AIMessage(content=response.content))
        st.session_state.display.append(("assistant", response.content))