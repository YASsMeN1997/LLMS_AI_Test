import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase
from config.config import Config
from src.car_description import parse_car_description
import os
import json
import shutil


def send_email(subject, json_data, to_email,image_path, attachment_path=None):
    #print(f"Config values: SENDER={Config.EMAIL_SENDER}, PASSWORD={Config.EMAIL_PASSWORD}, SERVER={Config.SMTP_SERVER}, PORT={Config.SMTP_PORT}")
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' Not found.")
    if subject is None or json_data is None or to_email is None:
        print("Error: subject, body, and to_email cannot be None.")
        return
    try:
        msg = MIMEMultipart()
        msg['From'] = Config.EMAIL_SENDER
        msg['To'] = to_email
        msg['Subject'] = subject

        #body = "Please check car details in JSON format && the attached car image below:\n"
        # Create HTML email body with code enclosed in <pre> and <code> tags
        html_body = f"""
        <html>
        <head>
        <style>
            pre {{
                font-family: 'Courier New', Courier, monospace;
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 5px;
            }}
        </style>
        </head>
        <body>
            
            <p>Here are the details of the car in JSON format:</p>
            <pre><code>{json_data}</code></pre>
            <p>Kindly check the attached car image.</p>
            <p>Regards,<br>Your Car Info App</p>
        </body>
        </html>
        """

        # Attach the HTML body to the email
        msg.attach(MIMEText(html_body, 'html'))


        with open(image_path, 'rb') as image_file:
            img = MIMEImage(image_file.read())
            img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
            
            # Attach the image to the email
            msg.attach(img)

        server = smtplib.SMTP(Config.SMTP_SERVER, int(Config.SMTP_PORT))
        server.starttls()
        server.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)
        server.sendmail(Config.EMAIL_SENDER, to_email, msg.as_string())
        print("Email sent successfully.")
        server.quit()
    
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

def process_car_info(description, car_image, user_email):
    if not description:
        return "Please provide a description of the car."
    if not car_image:
        return "Please upload a car image."
    if not user_email:
        return "Please enter your email."

    # Save the uploaded car image to the 'assets' folder
    #print(car_image)
    image_path = os.path.join('assets', os.path.basename(car_image))
    shutil.copy(car_image,image_path)

    # Get the car details in JSON format
    car_details = parse_car_description(description)
    
    # Set the subject and the email content
    subject = "Car Details"
    #json_data = car_details
    cleaned_json = car_details.replace("```","").strip().replace("json","").strip()
    #formatted_json = json.dumps(car_details,indent=4)
    
    # Send the email with the car details and the image
    try:
        send_email(subject, cleaned_json, user_email, image_path)
        return "Car details sent successfully to the provided email!"
    except Exception as e:
        return f"Failed to send email. Error: {e}"
