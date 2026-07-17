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

DATABASE_SCHEMA = """
Table Name: retail_data

Columns:
Date
Store ID
Product ID
Category
Region
Inventory Level
Units Sold
Units Ordered
Demand Forecast
Price
Discount
Weather Condition
Holiday/Promotion
Competitor Pricing
Seasonality
"""

SYSTEM_PROMPT = f"""
You are an expert SQLite SQL generator.

Database Schema:

{DATABASE_SCHEMA}

IMPORTANT RULES:

1. Return ONLY SQL.
2. No markdown.
3. No explanation.
4. Table name is retail_data.
5. Use SQLite syntax only.

VERY IMPORTANT:

Whenever a column contains spaces,
ALWAYS wrap it in double quotes.

Example:

"Units Sold"

"Inventory Level"

"Demand Forecast"

"Holiday/Promotion"

"Store ID"

"Product ID"

"Competitor Pricing"

Always use double quotes around these columns.
"""

def generate_sql(user_question):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    return response.choices[0].message.content