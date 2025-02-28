import os

# -------------------------
# File paths
# -------------------------
# Path to the dataset CSV file
DATASET_PATH = "../data/balanced_dataset.csv"
DATASET_PATH_ = "./data/balanced_dataset.csv"

# Path where you want to save the dataset with health advice
OUTPUT_PATH = "balanced_dataset_with_health_advice.csv"

# -------------------------
# Google Drive file ID
# -------------------------
# Google Drive file ID for dataset (if you want to change it in the future)
GOOGLE_DRIVE_FILE_ID = "1-PnrynLGqLGieczJMyvnY1u4kQQd2OWc"
GOOGLE_DRIVE_URL = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"

# -------------------------
# Ollama Model Settings
# -------------------------
# Path to Ollama executable, update if it is installed in a non-standard location
# OLLAMA_PATH = "/usr/local/bin/ollama"  # Change this if your Ollama CLI is installed elsewhere

# Meditron model settings
MEDITRON_MODEL_NAME = "meditron"  # Name of the model you are running with Ollama

# -------------------------
# Environment Settings
# -------------------------
# Set the environment to 'development' or 'production'
ENVIRONMENT = "development"

# -------------------------
# Other Configurations
# -------------------------
# Max length of input data for the model
# MAX_INPUT_LENGTH = 1000  # You can adjust this based on your model's requirements

# -------------------------
# Health Assistant Settings
# -------------------------
# The role and behavior of the model for the assistant
HEALTH_ASSISTANT_ROLE = """
    You are Meditron, a virtual health assistant. Your primary role is to assist both patients and doctors by providing:
    
    1. **Personalized health advice** based on health indicators such as sensor data or symptoms.
    2. **Clear and understandable explanations** of possible causes of health conditions.
    3. **Lifestyle improvement suggestions** like diet, exercise, sleep habits, and stress management.
    4. **Limitations and referrals**: If you are unsure about the diagnosis or the query, you will encourage the user to consult a healthcare professional.
    
    Here are some guidelines for your responses:
    - When receiving sensor data, interpret and offer insights into the possible causes or lifestyle improvements based on that data.
    - If the data points to a potential health issue, suggest immediate lifestyle changes and advise seeking medical consultation if necessary.
    - If you do not have enough information to give an accurate response, kindly suggest that the user consult a professional healthcare provider.
    - If the user mentions symptoms, provide possible explanations and lifestyle advice while still advising consultation with a doctor when appropriate.
    
    **Please respond in a way that is empathetic, informative, and helpful.**
    """
