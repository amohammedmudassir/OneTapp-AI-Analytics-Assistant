import streamlit as st
import time

from sql_agent import generate_sql
from database_query import execute_sql
from insight_generator import generate_business_insight
from validator import is_valid_question

st.set_page_config(
    page_title="OneTapp AI Analytics Assistant",
    layout="wide"
)
# Sidebar
st.sidebar.header("💡 Example Questions")

st.sidebar.markdown("""
- Which region sold the highest units?
- Which category has the highest inventory?
- Show average price by category.
- Which season has the highest demand forecast?
""")

st.title("🛒 OneTapp AI Analytics Assistant")

st.write(
    "Ask business questions about sales, inventory, promotions, pricing, products and regions."
)

st.caption("📊 Dataset: 73,100 retail records")

question = st.text_input(
    "Ask a Question",
    placeholder="Example: Which region sold the highest units?"
)

if st.button("Analyze"):

    # Empty question
    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    # Validate domain
    if not is_valid_question(question):
        st.warning(
            "I can only answer questions related to retail sales, inventory, products, promotions, pricing, regions, demand forecasting and business analytics using the available dataset."
        )
        st.stop()

    start_time = time.time()
    with st.spinner("🤖 AI is analyzing your question..."):

        # Generate SQL
        sql = generate_sql(question)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        # Execute SQL
        result = execute_sql(sql)

        # SQL Error
        if isinstance(result, str) and result == "SQL_ERROR":
            st.error(
                "Unable to process your request. Please try another retail-related analytical question."
            )
            st.stop()

        # No Data Found
        if result is None:
            st.info(
                "No matching data was found for your question."
            )
            st.stop()

        # Show Result
        st.subheader("Query Result")
        st.dataframe(result, use_container_width=True)

        # Generate Business Insight
        insight = generate_business_insight(question, result)

        end_time = time.time()
        execution_time = end_time - start_time

        st.subheader("Business Insight")
        st.success(insight)
        st.caption(f"⏱ Analysis completed in {execution_time:.2f} seconds")