from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """You are an intelligent movies information extraction AI.

            Analyze the following paragraph and extract useful information.

            Rules:
            - Extract only information explicitly present in the paragraph.
            - Never hallucinate or infer unsupported facts.
            - Ignore irrelevant details.
            - Preserve important context.
            - If information is unavailable, return null.
            - Keep the summary concise.
            - Return ONLY valid JSON.
            - Do not use Markdown.
            - Do not add explanations outside the JSON.

            Output schema:

            {{
              "main_topic": "",
              "summary": "",
              "key_points": [],
              "people": [],
              "organizations": [],
              "locations": [],
              "products_or_technologies": [],
              "dates": [],
              "numbers_and_statistics": [],
              "events": [],
              "relationships": [],
              "keywords": [],
              "missing_information": []
            }}
            """
         ),
         ("human",
          """Extarct information from this Paragraph:
            {paragraph}
            """
          )
    ]
)

para = input("Enter Paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph" : para}
)

response = model.invoke(final_prompt)

print(response.content)