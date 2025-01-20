import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    OPENAI_API_KEY = os.getenv("Azure_OpenAi_Key")
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = os.getenv("SMTP_PORT")
