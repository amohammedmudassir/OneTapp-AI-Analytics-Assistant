from sql_agent import generate_sql
from database_query import execute_sql
from insight_generator import generate_business_insight

question = input("Ask your question: ")

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)

result = execute_sql(sql)

print("\nDatabase Result:\n")
print(result)

print("\nBusiness Insight:\n")

insight = generate_business_insight(question, result)

print(insight)