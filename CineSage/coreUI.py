import json
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List, Optional

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# Pydantic model
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# Initialize model and parser
model = ChatGroq(model="openai/gpt-oss-120b")
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a professional information extraction assistant
        specializing in movie-related content.

        Extract movie information only from facts explicitly stated
        in the provided paragraph.

        Do not hallucinate or infer unsupported information.
        Use null for unavailable optional fields.
        Use empty lists when genre or cast information is unavailable.
        Keep the summary concise and accurate.

        {format_instructions}
        """
    ),
    (
        "human",
        "{paragraph}"
    )
])

# Custom styling
st.markdown("""
<style>
    .block-container {
        max-width: 800px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 750;
        letter-spacing: -1px;
        margin-bottom: 0.4rem;
    }

    .subtitle {
        text-align: center;
        color: #8b8b98;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    div.stButton > button {
        width: 100%;
        height: 3rem;
        border-radius: 10px;
        font-weight: 600;
    }

    div[data-testid="stTextArea"] textarea {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="main-title">🎬 Movie Information Extractor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Extract structured movie details from any paragraph.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# Input
st.subheader("Input Paragraph")

paragraph = st.text_area(
    "Enter movie information",
    placeholder=(
        "Example: Inception is a 2010 science fiction film "
        "directed by Christopher Nolan and starring Leonardo "
        "DiCaprio..."
    ),
    height=200,
    label_visibility="collapsed"
)

# Extraction button
extract_button = st.button(
    "Extract Movie Information",
    type="primary",
    use_container_width=True
)

# Extraction logic
if extract_button:
    if not paragraph.strip():
        st.warning("Please enter a paragraph first.")

    else:
        try:
            with st.spinner("Extracting movie information..."):
                final_prompt = prompt.invoke({
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)

                movie = parser.parse(response.content)

            st.divider()
            st.subheader("Extracted Movie Details")

            st.markdown(f"### 🎥 {movie.title}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Release Year**")
                st.write(
                    movie.release_year
                    if movie.release_year is not None
                    else "Not available"
                )

                st.markdown("**Director**")
                st.write(movie.director or "Not available")

                st.markdown("**Rating**")
                st.write(
                    movie.rating
                    if movie.rating is not None
                    else "Not available"
                )

            with col2:
                st.markdown("**Genres**")
                st.write(", ".join(movie.genre) if movie.genre else "Not available")

                st.markdown("**Cast**")
                st.write(", ".join(movie.cast) if movie.cast else "Not available")

            st.markdown("**Summary**")
            st.write(movie.summary)

            st.divider()
            st.subheader("JSON Output")

            st.json(movie.model_dump())

        except Exception as e:
            st.error(f"Unable to extract movie information: {e}")
