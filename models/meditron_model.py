# models/meditron_model.py

import subprocess
from config.settings import MEDITRON_MODEL_NAME, HEALTH_ASSISTANT_ROLE

def run_meditron_health_assistant(sensor_data=None, symptoms=None, question=None):
    """
    Run the Meditron model to act as a health assistant for patients or doctors.
    This model provides health advice based on input sensor data or symptoms.
    
    :param sensor_data: A dictionary or string containing sensor readings.
    :param symptoms: A string of symptoms described by the user.
    :return: A string response from the model with health advice.
    """
    # Define the Meditron prompt with health assistant role
    prompt = HEALTH_ASSISTANT_ROLE

    # Form the input based on the data available
    if sensor_data:
        input_data = f"Sensor data: {sensor_data}. Please analyze and provide health advice."
    elif symptoms:
        input_data = f"Symptoms: {symptoms}. Please provide possible causes and suggestions."
    elif question:
        input_data = f"Question: {question}. Please provide a detailed response."
    else:
        input_data = "No sensor data or symptoms provided. Please describe the patient's condition for advice."

    # Concatenate the prompt with the input data
    full_prompt = prompt + "\n" + input_data + "\n" + " Ask the user for more context if needed and offer lifestyle recommendations for health improvement."
    
    # Run the Ollama model using the full prompt
    try:
        result = subprocess.run(
            ['ollama', 'run', MEDITRON_MODEL_NAME, '--input', full_prompt],
            capture_output=True, text=True, check=True
        )
        # Extract and return the response from the model
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


