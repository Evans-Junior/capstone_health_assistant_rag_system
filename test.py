# Example usage:

from models.meditron_model import run_meditron_health_assistant


if __name__ == "__main__":
    # You can test the function directly
    sensor_data = {
        "Sensor": 85,
        "blood_pressure": "120/80",
        "temperature": 98.6,
        "glucose": 110
    }
    symptoms = "Fatigue and dizziness"
    
    response = run_meditron_health_assistant(sensor_data=sensor_data)
    print(response)

    response_symptoms = run_meditron_health_assistant(symptoms=symptoms)
    print(response_symptoms)