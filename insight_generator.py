from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def generate_business_insight(question, dataframe):

    prompt = f"""
You are a Retail Business Analyst.

The user asked:

{question}

SQL Result:

{dataframe}

IMPORTANT RULES:

1. Use ONLY the data provided.
2. Never invent numbers.
3. Never estimate percentages.
4. If data is missing, simply say it is unavailable.
5. Explain the result in business language.
6. Give one recommendation.
7. Keep response under 100 words.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content