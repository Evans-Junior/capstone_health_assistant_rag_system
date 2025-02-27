# database/chromadb_setup.py

import chromadb
from chromadb.config import Settings
import pandas as pd

def initialize_chromadb(collection_name: str, csv_file: str):
    """
    Initialize the ChromaDB collection with data from the provided CSV file.
    """
    # Connect to ChromaDB
    client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="db"))

    # Load the CSV into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Initialize collection
    collection = client.create_collection(collection_name)

    # Add data to ChromaDB
    for index, row in df.iterrows():
        collection.add(
            documents=row[:-1].values.tolist(),  # Sensor values
            metadatas=[{"label": row["label"]}],  # Metadata with the label
            ids=[str(index)]
        )

    return collection

def query_chromadb(collection, sensor_data: list):
    """
    Query ChromaDB with the given sensor data.
    """
    # Query ChromaDB for the most similar data
    results = collection.query(
        query_embeddings=[sensor_data],
        n_results=1
    )

    # Return the result of the query
    return results['documents'][0] if results['documents'] else None
