# main.py

from database.chromadb_setup import initialize_chromadb, query_chromadb
from models.meditron_model import run_meditron_model
import pandas as pd

# Step 1: Initialize ChromaDB and load the data
csv_file = "data/balanced_dataset.csv"
collection_name = "balanced_dataset_collection"
collection = initialize_chromadb(collection_name, csv_file)

# Step 2: Check if sensor data should be provided or not
use_sensor_data = False  # Set to True if you want to use sensor data, False to use default input

if use_sensor_data:
    # If using sensor data, get data from the CSV
    df = pd.read_csv(csv_file)
    sensor_input = df.iloc[0, :-1].values.tolist()  # Get sensor data from the first row (Sensor_1 to Sensor_8)

    # Step 3: Query the database for the input data
    query_result = query_chromadb(collection, sensor_input)

    # Step 4: Send the result to the meditron model for prediction
    if query_result:
        sensor_input_str = " ".join(map(str, sensor_input))  # Convert sensor data to a string
        prediction = run_meditron_model(sensor_input_str)
        print(f"Prediction from meditron: {prediction}")
    else:
        print("No relevant data found in ChromaDB.")
else:
    # If not using sensor data, ask for a general response
    print("No sensor data provided, using default behavior.")
    prediction = run_meditron_model()
    print(f"Prediction from meditron: {prediction}")
