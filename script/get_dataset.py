import gdown
import pandas as pd
from config.settings import GOOGLE_DRIVE_URL, DATASET_PATH

# Download the file
gdown.download(GOOGLE_DRIVE_URL, DATASET_PATH, quiet=False)

# Load the CSV into a DataFrame
df = pd.read_csv(DATASET_PATH)

# Display the first few rows
print(df.head())
