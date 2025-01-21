import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    AZURE_OPENAI_KEY = os.getenv("Azure_OpenAi_Key")
    EMAIL_SENDER = os.getenv("SENDER_EMAIL")
    EMAIL_PASSWORD = os.getenv('password')
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = os.getenv("SMTP_PORT")
    ENDPOINT = os.getenv("ENDPOINT")
