from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
            """
            You are a professional information extraction assistant
            specializing in movie-related content.

            Your task is to analyze the provided paragraph and extract
            structured, factual information.

            Extraction Guidelines:
            1. Use only information explicitly stated in the paragraph.
            2. Do not hallucinate, assume, or infer unsupported facts.
            3. Exclude irrelevant information.
            4. Preserve important context and factual relationships.
            5. Return null for unavailable scalar information and empty arrays for unavailable list information.
            6. Keep the summary concise, accurate, and informative.
            7. Avoid duplicate entries.
            8. Preserve names, dates, numbers, and terminology as stated.
            9. Return only valid JSON without Markdown or explanations.
            10. Follow the output schema exactly.

            Output Schema:
            {{
                "main_topic": null,
                "summary": null,
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

            Field Definitions:
            - main_topic: The primary subject of the paragraph.
            - summary: A concise summary of the provided content.
            - key_points: The most important explicitly stated facts.
            - people: Names of individuals mentioned in the paragraph.
            - organizations: Companies, studios, institutions, or other organizations explicitly mentioned.
            - locations: Explicitly mentioned places and geographical locations.
            - products_or_technologies: Explicitly mentioned products, technologies, tools, or platforms.
            - dates: Dates, years, and time periods explicitly stated.
            - numbers_and_statistics: Explicit numerical values, measurements, quantities, and statistics.
            - events: Explicitly mentioned events, activities, or occurrences.
            - relationships: Explicitly stated relationships between people, organizations, locations, or other entities.
            - keywords: Relevant terms and concepts from the paragraph.
            - missing_information: Important information relevant to the paragraph's subject that is explicitly indicated as unknown or unavailable. Do not list arbitrary details that are absent.

            Ensure that every extracted fact is supported by the paragraph.
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