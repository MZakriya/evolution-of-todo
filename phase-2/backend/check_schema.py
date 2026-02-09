from sqlalchemy import create_engine, inspect
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

try:
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)
    if inspector.has_table('user'):
        print("Table 'user' exists. Columns:")
        columns = inspector.get_columns('user')
        for column in columns:
            print(f"- {column['name']}")
    else:
        print("Table 'user' does not exist.")
except Exception as e:
    print(f"Error: {e}")
