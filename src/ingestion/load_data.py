import os

import pandas as pd
import sqlalchemy as db
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_name = os.getenv("POSTGRES_DB")

    DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    raw_members = pd.read_csv("./data/members_v3.csv", index_col=False)
    raw_transactions = pd.read_csv("./data/transactions_v2.csv", index_col=False)
    raw_train = pd.read_csv("./data/train_v2.csv", index_col=False)

    engine = db.create_engine(DATABASE_URL, echo=True)

    with engine.connect() as conn:
        raw_members.to_sql(name='MEMBERS', con=conn, if_exists='replace')
        raw_train.to_sql(name='TRAIN', con=conn, if_exists='replace')
        raw_transactions.to_sql(name='TRANSACTIONS', con=conn, if_exists='replace')

        member_count = conn.execute(db.text('SELECT COUNT(msno) FROM "MEMBERS"')).fetchone()[0]
        transaction_count = conn.execute(db.text('SELECT COUNT(msno) FROM "TRANSACTIONS"')).fetchone()[0]
        train_count = conn.execute(db.text('SELECT COUNT(msno) FROM "TRAIN"')).fetchone()[0]

    print(len(raw_members) == member_count)
    print(len(raw_transactions) == transaction_count)
    print(len(raw_train) == train_count)

if __name__ == "__main__":
    main()
