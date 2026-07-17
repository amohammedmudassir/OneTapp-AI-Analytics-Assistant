import sqlite3
import pandas as pd

DATABASE = "database/retail.db"

def execute_sql(sql):

    conn = sqlite3.connect(DATABASE)

    try:
        df = pd.read_sql_query(sql, conn)

        conn.close()

        if df.empty:
            return None

        return df

    except Exception:
        conn.close()
        return "SQL_ERROR"