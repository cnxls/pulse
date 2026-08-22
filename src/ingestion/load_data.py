import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv
import os


load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

raw_members = pd.read_csv("./data/members_v3.csv")
raw_transactions = pd.read_csv("./data/transactions_v2.csv")
raw_train = pd.read_csv("./data/train_v2.csv")

engine = db.create_engine(DATABASE_URL, echo=True)

with engine.connect() as conn:
    result = conn.execute(db.text("SELECT 1"))
    print(result.fetchone())