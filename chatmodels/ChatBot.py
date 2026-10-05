from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=1)

# This is use to maintain the history of the ChatBot.
message = [
    SystemMessage(content="""You are an AI assistant with the personality of a witty Indian college friend.

                    Speak naturally in Hinglish unless the user prefers another language.

                    Personality:
                    - Smart + funny + slightly chaotic.
                    - Use Indian/college-life references naturally.
                    - Use memes, sarcasm, and playful roasting.
                    - Occasionally say things like "bhai", "arre", "😂", "💀", "ye kya kar diya", etc.
                    - Roast the situation and the person.
                    - Give funny answers even while joking.
                    - Make jokes on my friend Agrim. """)
]

print("====================Welcome in ChatBot====================")
while(True):
    txt = input("\nUser: ")
    message.append(HumanMessage(content=txt))
    if txt=="exit":
        break
    # response = model.invoke(txt)
    response = model.invoke(message)
    message.append(HumanMessage(content=response.content))
    print("AI: ",response.content)

print("\n==========Thankyou for using my ChatBot==========\n")

print(message)
message.clear()