from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

load_dotenv()

class Database:

    def __init__(self, collection_name="monsters"):
        """Initialize the database connection and set the collection."""
        self.client = MongoClient(getenv("DB_URL"), tlsCAFile=where())
        self.db = self.client["BuildSprintDB"]
        self.collection = self.db[collection_name]

    def seed(self, amount: int):
        """Insert multiple random monster records into the database."""
        monsters = [Monster().to_dict() for _ in range(amount)]
        result = self.collection.insert_many(monsters)
        return len(result.inserted_ids) == amount


    def reset(self):
        """Delete all documents in the collection."""
        result = self.collection.delete_many({})
        return result.acknowledged

    def count(self) -> int:
        """Return the number of documents in the collection."""
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """Return all documents as a Pandas DataFrame."""
        data = list(self.collection.find({}, {"_id": False}))
        return DataFrame(data) if data else DataFrame()

    def html_table(self) -> str:
        """Return the collection as an HTML table or None if empty."""
        df = self.dataframe()
        return df.to_html() if not df.empty else None
    
if __name__ == "__main__":
    db = Database()

    # Reset and seed the database
    db.reset()
    print("Database cleared.")

    db.seed(1000)
    print(f"Inserted 1000 monsters. Current count: {db.count()}")

    # Print first 5 entries
    print(db.dataframe().head())