import pandas as pd
from models.meditron_model import run_meditron_health_assistant
from config.settings import DATASET_PATH_

# Load the CSV dataset into a DataFrame
df = pd.read_csv(DATASET_PATH_)

# Check if 'health_advice' column exists, if not, create it
if 'health_advice' not in df.columns:
    df['health_advice'] = ""

# Loop through the dataset and process each row
for index, row in df.iterrows():
    # Prepare sensor data as a dictionary (excluding the label column)
    sensor_data = row[:-1].to_dict()

    print(f"🔄 Processing sample {index}...")

    # Get health advice from Meditron model
    health_advice = run_meditron_health_assistant(sensor_data=sensor_data)

    # Debugging: Show the response
    print(f"📌 Health advice for sample {index}: {health_advice}")

    # Store the health advice in the DataFrame
    df.loc[index, 'health_advice'] = health_advice

    # Optional: Save progress every 100 samples to prevent data loss
    if index % 100 == 0:
        df.to_csv("balanced_dataset_with_health_advice.csv", index=False)
        print("💾 Autosaved progress...")

# Final save after processing all rows
df.to_csv("balanced_dataset_with_health_advice.csv", index=False)
print("✅ Processing completed! Results saved to 'balanced_dataset_with_health_advice.csv'.")
