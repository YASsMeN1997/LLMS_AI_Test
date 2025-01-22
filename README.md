---

# Car Info Submission and Email Notification App

This project provides a web app that allows users to submit car descriptions, upload car images, and receive the car details formatted as a structured JSON via email. The app processes the description using OpenAI's GPT-4o mini model and sends an email containing the car details, including a JSON format and the uploaded image as an attachment.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [How It Works](#how-it-works)

---

## Overview

This app takes the following inputs from users:

- **Car Description**: A textual description of the car.
- **Car Image**: The image of the car.
- **User Email**: The email address where the car details will be sent.

After processing the description using OpenAI's GPT-4o mini model, it generates a JSON object containing structured car details. The details are then sent to the provided email along with the uploaded car image.

---

## Features

- **Car Description Parsing**: Automatically parses car descriptions to generate structured JSON.
- **Image Upload**: Allows users to upload car images.
- **Email Sending**: Sends car details and image to a provided email address.
- **Structured JSON Output**: Sends well-formatted JSON output in html style for easy readability.
- **Gradio Interface**: User-friendly interface for interaction.

---

## Technologies Used

- **Python**: The programming language used for backend logic.
- **Gradio**: Framework for building interactive web interfaces.
- **OpenAI GPT-4o Mini**: Used for generating structured JSON from the car description.
- **SMTP (Gmail)**: For sending the email with car details and image attachment.
- **Shutil**: Used to save uploaded images to the server.

---

## Setup and Installation

Follow the steps below to set up and run the app on your local machine or any cloud platform.

1. Clone the Repository

Clone the repository to your local machine.

```python
bash
git clone https://github.com/YASsMeN1997/LLMS_AI_Test.git
```

2. Set Up Virtual Environment (Optional but recommended)

It is recommended to use a virtual environment to manage the dependencies.

```python
bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install Dependencies
Install the required Python packages listed in the requirements.txt file.

```python
bash
pip install -r requirements.txt
```

4. Create a .env File

The .env file should contain your API key and other environment variables. Create a .env file in the root directory of the project and add the following content:

```python
AZURE_OPENAI_KEY = your_openai_api_key_here
SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
SENDER_EMAIL = your_email@gmail.com
SENDER_PASSWORD = your_email_password_here
ENDPOINT = your_Deployment_Endpoint
```

5. Ensure the assets Folder Exists

Make sure you have an assets folder in the root directory of your project to store the uploaded images. If the folder doesn't exist, create it:

```python
bash
mkdir assets
```

---

## Usage

1. **Run the App**

After setting up the project, run the app.py file to start the Gradio interface.

```python
bash
python app.py
```

This will launch a local Gradio interface in your browser where you can interact with the app.

2. **Input Fields**

- Car Description: Enter the description of the car.
- Car Image: Upload an image of the car.
- Email Address: Enter the email where the car details will be sent.

3. **Submit Data**
Click on the "Send Car Details" button to submit the car description, image, and email. The app will process the car description, generate the car details in JSON format, and send an email to the provided email address with the car details and the image attached.

---


## How It Works

1. **Input Processing**:
   - The user provides the car description, image, and email.
   
2. **Car Description Parsing**:
   - The app uses OpenAI's GPT-4o Mini model to process the car description and generate a structured JSON object containing the car details.

3. **Email Sending**:
   - The car details and the image are sent via email to the user.

4. **Image Upload**:
   - The uploaded image is saved in the assets folder on the server.

---

### Example

Here’s an example of a user input and the corresponding email output:

**User Input**:

- Car Description: Blue Ford Fusion produced in 2015 featuring a 2.0-liter engine. The vehicle has low mileage with only 40,000 miles on the odometer.
- Car Image: Upload a car image (e.g., image001.jpg).
- User Email: user@example.com.

**Email Output**:


**Subject**: Car Details

Here are the details of the car in JSON format:

```python
{
    "car": {
        "body_type": "sedan",
        "color": "Blue",
        "brand": "Ford",
        "model": "Fusion",
        "manufactured_year": 2015,
        "motor_size_cc": 2000,
        "tires": {
            "type": "brand-new",
            "manufactured_year": 2022
        },
        "windows": "tinted",
        "notices": [
            {
                "type": "Mileage",
                "description": "Low mileage with only 40,000 miles on the odometer."
            }
        ],
        "price": {
            "amount": 1000000,
            "currency": "L.E"
        }
    }
}
```
![image002](https://github.com/user-attachments/assets/0abb808d-8b0d-4442-88c4-84377f7ee1f1)
