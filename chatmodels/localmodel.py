
# this is use when you want to use a aprticular model in your machine without using any API key, download from HuggingFace

'''
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline(
    model_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    pipeline=dict(
        max_new_token=512,
        do_simple=True,
        repetation_penalty=1.03
    ),
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("How are you?")

print(response.content)
'''