import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import asyncio

import os
from dotenv import load_dotenv
load_dotenv()
#Password must be in application format like "abcd efgh qwer asdf"
PASSWORD = os.environ.get("EMAIL_PASSWORD")

SERVER = "smtp.gmail.com"
PORT = 587
EMAIL = "cryptotrackerproject@gmail.com"


def generate_notification_message_text(crypto_name: str, price: float, direction: str, date_time: str, currency: str = "") -> str:
    return f"""
    🚀 Cryptocurrency Update 🚀

    Great news! The cryptocurrency {crypto_name} has successfully surpassed the {price}{currency} level form {"lower" if direction == "up" else "upper"} price. 📈

    📅 Date and Time: {date_time}

    Keep an eye on the market and good luck! 🌐💹
    """
    
def generate_subject(crypto_name: str, price: float, currency: str = ""):
    return f"🚀 [Cryptocurrency Alert] {crypto_name} Surpasses {price}{currency} - Market Update 📈"

def create_message(to_email: str, crypto_name: str, price: float, direction, date_time: str, currency: str = "") -> MIMEMultipart:
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = to_email
    message["Subject"] = generate_subject(crypto_name, price, currency)
    message.attach(MIMEText(generate_notification_message_text(crypto_name, price, direction, date_time, currency), 'plain'))
    return message

async def send_notification_email(message: MIMEMultipart) -> bool:
    try:
        server = smtplib.SMTP(SERVER, PORT)
        server.starttls()

        server.login(EMAIL, PASSWORD)
        await asyncio.to_thread(server.sendmail, EMAIL, message["To"], message.as_string())
        server.quit()
        
        return True
    
    except Exception as e:
        print("Error sending email:", e)
        return False