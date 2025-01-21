import openai
from config import config
import os
import json
import requests


def parse_car_description(description):


    """
    Function to send car description to OpenAI API and retrieve a structured response in JSON format.
    Args:
        description (str): The description of the car.
    
    Returns:
        dict: A dictionary containing the car details in the specified JSON format.
    """

    API_KEY = config.Config.AZURE_OPENAI_KEY
    EndPoint = config.Config.ENDPOINT

    # Define the prompt that guides the model to return the correct structured response
    prompt = f"""
    Given the following car description, generate the car's details in a structured JSON format:

    Description: {description}

    The JSON should follow this structure:
    {{
        "car": {{

            "color": "<string>",
            "brand": "<string>",
            "model": "<string>",
            "manufactured_year": <int>,
            "motor_size_cc": <int>,
            "tires": {{
                "type": "<string>",
                "manufactured_year": <int>
            }},
            "windows": "<string>",
            "notices": [
                {{
                    "type": "<string>",
                    "description": "<string>"
                }}
            ],
            "price": {{
                "amount": <int>,
                "currency": "<string>"
            }}
        }}
    }}

    Please provide the response in the above format.
    """
    # prepare the request payload
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    # Send the request to the API endpoint
    response = requests.post(EndPoint, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"
    
