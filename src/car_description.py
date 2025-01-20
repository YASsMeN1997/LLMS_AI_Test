import openai
from config import config
import os
import json

def parse_car_description(description):

    openai.OPENAI_API_KEY = config.Config.OPENAI_API_KEY
    """
    Function to send car description to OpenAI API and retrieve a structured response in JSON format.
    Args:
        description (str): The description of the car.
    
    Returns:
        dict: A dictionary containing the car details in the specified JSON format.
    """
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
    # Send the request to OpenAI API
    response = openai.Completion.create(
        engine="gpt-4o-mini-YY3943",  
        prompt=prompt,
        max_tokens=200,  
        temperature=0.3,  
        n=1,  # We want only one response
        stop=["\n"]  # Ensure it stops at the end of the response
    )

    # Extract the generated response
    response_text = response.choices[0].text.strip()

    try:
        car_details = json.loads(response_text)
        return car_details
    except json.JSONDecodeError:
        # If JSON is invalid, return an error message
        return {"error": "Failed to parse JSON response"}