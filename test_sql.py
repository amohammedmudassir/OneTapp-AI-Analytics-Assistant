from sql_agent import generate_sql

question = "Which region has the highest total units sold?"

sql = generate_sql(question)

print(sql)