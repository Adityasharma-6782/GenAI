from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

from pydantic import BaseModel
from typing import List, Optional

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

from langchain_core.output_parsers import PydanticOutputParser

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
            """
            You are a professional information extraction assistant
            specializing in movie-related content.
            {fotmat_instruction}
            """
         ),
         ("human","{paragraph}")
    ]
)

para = input("Enter Paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph" : para,
     "fotmat_instruction" : parser.get_config_jsonschema()
    }
)

response = model.invoke(final_prompt)

print(response.content)