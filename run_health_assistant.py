# import script.get_dataset as get_dataset
from database.chromadb_setup import initialize_chromadb, query_chromadb
from models.meditron_model import run_meditron_health_assistant
import pandas as pd
# import gdown
from  config.settings import DATASET_PATH_

# Load the CSV into a DataFrame
df = pd.read_csv(DATASET_PATH_)

# Now, let's loop through the dataset and process each row
# Assuming 'label' is the target column and the rest are sensor readings
for index, row in df.iterrows():
    # Prepare sensor data for the assistant
    sensor_data = row[:-1].to_dict()  # Exclude the last column 'label'
    symptoms = None  # You can add symptoms if available in another format
    
    print(f"Processing sample {index}...")
    health_advice = run_meditron_health_assistant(sensor_data=sensor_data)
    print("Health advice:", health_advice)
    
    # Optionally, you can store the results or display them
    # For example, saving the advice into the dataset
    df.loc[index, 'health_advice'] = health_advice

# Save the results to a new CSV file
df.to_csv("balanced_dataset_with_health_advice.csv", index=False)
print("Processing completed. Results saved to 'balanced_dataset_with_health_advice.csv'.")
# The script downloads the dataset, processes each row, and saves the health advice back to a new CSV file. You can further customize the processing logic and data handling as needed. The `run_meditron_health_assistant` function is used to get health advice based on sensor data. You can modify the script to include additional features or data processing steps.