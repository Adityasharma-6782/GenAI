from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=1)

print("press 0 for normal")
print("press 1 for logical")
print("press 2 for creative")

choice = int(input("Enter your choice: "))

if choice==0:
    mode = '''
            You are a helpful AI assistant.
            Give clear, accurate, and balanced answers.
            Keep the response easy to understand and relevant to the user's question.
            '''
elif choice==1:
    mode = '''
            You are a logical AI assistant.
            Analyze the problem step by step.
            Focus on facts, reasoning, accuracy, and clear explanations.
            Avoid unnecessary creativity.
            '''
else:
    mode= '''
            You are a creative AI assistant.
            Give imaginative, unique, and engaging responses.
            Think outside the box and provide multiple creative ideas when useful.
        '''
# This is use to maintain the history of the ChatBot.
message = [
    SystemMessage(content=mode)
]

print("====================Welcome in ChatBot====================")
while(True):
    txt = input("\nUser: ")
    message.append(HumanMessage(content=txt))
    if txt=="exit":
        break
    # response = model.invoke(txt)
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("AI: ",response.content)

print("\n==========Thankyou for using my ChatBot==========\n")

print(message)
message.clear()