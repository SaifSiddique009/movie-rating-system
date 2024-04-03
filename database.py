from sqlalchemy import create_engine, text
import pymysql
import os

# Replace with your actual database credentials
db_connection_str = os.environ['DB_CONN_STR']

# Create the engine
engine = create_engine(db_connection_str, connect_args={
    "ssl": {
        "ca": "ca.pem",  # replace with the path to your CA certificate
    },
})

try:
    with engine.connect() as conn:
        # conn.execute(text("CREATE TABLE mytest (id INTEGER PRIMARY KEY)"))
        conn.execute(text("INSERT INTO mytest (id) VALUES (1), (2)"))
        result = conn.execute(text("SELECT * FROM mytest"))
        print(result.fetchall())
except Exception as e:
    print(f"Error: {e}")
