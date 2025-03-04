# models/meditron_model.py

import subprocess
from config.settings import MEDITRON_MODEL_NAME, HEALTH_ASSISTANT_ROLE

import subprocess
from config.settings import MEDITRON_MODEL_NAME, HEALTH_ASSISTANT_ROLE

import subprocess
from config.settings import MEDITRON_MODEL_NAME, HEALTH_ASSISTANT_ROLE

def run_meditron_health_assistant(sensor_data=None, symptoms=None, question=None):
    prompt = HEALTH_ASSISTANT_ROLE
    input_data = ""

    if sensor_data:
        input_data = f"Sensor data: {sensor_data}. Please analyze and provide health advice."
    elif symptoms:
        input_data = f"Symptoms: {symptoms}. Please provide possible causes and suggestions."
    elif question:
        input_data = f"Question: {question}. Please provide a detailed response."
    else:
        input_data = "No sensor data provided."

    full_prompt = f"{prompt}\n{input_data}"

    try:
        result = subprocess.run(
            ["ollama", "run", MEDITRON_MODEL_NAME],
            input=full_prompt,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running Meditron model: {e.stderr}"


def run_meditron_model(sensor_input: str = None) -> str:
    """
    Run the meditron model using Ollama and get the prediction.
    
    Args:
        sensor_input (str): The sensor data formatted as a string. If None, a default prompt will be used.
    
    Returns:
        str: The prediction result from the meditron model.
    """
    if not sensor_input:
        # If no sensor input is provided, use a default message or behavior
        sensor_input = "No sensor data provided. Please respond with general information."
    
    # Run the Ollama model with the input
    command = f"ollama run meditron --input '{sensor_input}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    return result.stdout


