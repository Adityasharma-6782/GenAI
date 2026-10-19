import json
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# Initialize model
model = ChatGroq(model="openai/gpt-oss-120b")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a professional information extraction assistant
        specializing in movie-related content.

        Analyze the paragraph and extract structured, factual information.

        Rules:
        - Extract only explicitly stated information.
        - Never hallucinate or infer unsupported facts.
        - Exclude irrelevant details and duplicate entries.
        - Preserve important context and relationships.
        - Return null for unavailable scalar values.
        - Return empty arrays for unavailable list values.
        - Keep the summary concise and accurate.
        - Return only valid JSON without Markdown or explanations.

        Output schema:
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
        """
    ),
    (
        "human",
        """
        Extract structured information from the following paragraph:

        {paragraph}
        """
    )
])

# Custom styling
st.markdown("""
<style>
    .block-container {
        max-width: 850px;
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
        font-size: 1rem;
        color: #8b8b98;
        margin-bottom: 2rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-weight: 600;
        border: none;
    }

    div[data-testid="stTextArea"] textarea {
        border-radius: 10px;
    }

    div[data-testid="stJson"] {
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
    'Transform unstructured text into structured, factual JSON.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# Paragraph input
st.subheader("Input Paragraph")

paragraph = st.text_area(
    "Enter the paragraph you want to analyze",
    placeholder="Paste a movie description, article, review, or other text here...",
    height=220,
    label_visibility="collapsed"
)

# Extraction button
extract_button = st.button(
    "Extract Information",
    type="primary",
    use_container_width=True
)

# Process paragraph
if extract_button:
    if not paragraph.strip():
        st.warning("Please enter a paragraph before extracting information.")

    else:
        try:
            with st.spinner("Analyzing paragraph..."):
                final_prompt = prompt.invoke({
                    "paragraph": paragraph
                })

                response = model.invoke(final_prompt)

                result = json.loads(response.content)

            st.divider()
            st.subheader("Extracted Information")

            st.json(result)

        except json.JSONDecodeError:
            st.error(
                "The model returned invalid JSON. Please try again."
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")
