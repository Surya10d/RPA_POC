import smtplib
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv


def send_email(screenshot_path):
    """
    Need to Load env variables
    :param screenshot_path: Screenshot file path with extension
    """
    load_dotenv()
    # Replace 'your_email@gmail.com' and 'your_app_password' is your APP password key for Gmail
    sender_email = os.environ.get("GMAIL_ADDRESS")
    sender_password = (os.environ.get("GMAIL_PASSWORD").replace("\xa0", " ")
                      .replace("'", "").replace('"', ''))
    recipient_email = "surya.mr+1@zyngl.com"
    subject = "Webpage Update Screenshot"
    body = "The webpage has been updated. See the attached screenshot."

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    with open(screenshot_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {screenshot_path}")

        # Attach the instance 'part' to instance 'msg'
        msg.attach(part)

    # Create SMTP session for sending the mail
    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your SMTP server
        server.starttls()  # Enable security
        server.login(sender_email, sender_password)  # Login with email and password
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)


if __name__ == "__main__":
    screenshot_path = sys.argv[1]
    send_email(screenshot_path)
