import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase
import os
from config.config import Config


def send_email(subject, body, to_email,image_path, attachment_path=None):
    #print(f"Config values: SENDER={Config.EMAIL_SENDER}, PASSWORD={Config.EMAIL_PASSWORD}, SERVER={Config.SMTP_SERVER}, PORT={Config.SMTP_PORT}")
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' Not found.")
    if subject is None or body is None or to_email is None:
        print("Error: subject, body, and to_email cannot be None.")
        return
    try:
        # Create the MIMEMultipart message object
        msg = MIMEMultipart()
        
        # Setup the message headers
        msg['From'] = Config.EMAIL_SENDER
        msg['To'] = to_email
        msg['Subject'] = subject
        # Add body to the email
        msg.attach(MIMEText(body, 'plain'))
        with open(image_path,'rb') as image_file:
            img = MIMEImage(image_file.read())
            img.add_header('Content-Disposition','attachment',file_name=os.path.basename(image_path))
            img.attach(img)
        # Establish connection with the SMTP server
        server = smtplib.SMTP(Config.SMTP_SERVER,  int(Config.SMTP_PORT))
        server.starttls()  # Upgrade connection to secure
        
        # Login to the server using the sender's email and password
        server.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)
        #print("login scusefully")
        
        # Send the email
        server.sendmail(Config.EMAIL_SENDER, to_email, msg.as_string())
        print("Email sent successfully.")
        
        # Close the connection
        server.quit()
    
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

    