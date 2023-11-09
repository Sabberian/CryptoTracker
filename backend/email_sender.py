import smtplib
from email.message import EmailMessage

def generate_email_text(crypto_name: str, price: float, date_time: str, currency: str=""):
    return f"""
    🚀 Cryptocurrency Update 🚀

    Great news! The cryptocurrency {crypto_name} has successfully surpassed the {price}{currency} level. 📈

    📅 Date and Time: {date_time}

    Keep an eye on the market and good trading! 🌐💹
    """

def send_message(message: str, reciever: str):
    msg = EmailMessage()
    msg["Subject"] = "Crypto news"
    msg["From"] = "Crypto Tracker"
    msg["To"] = reciever
    msg.set_content(message)
    
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    
if __name__ == "__main__":
    send_message(generate_email_text("bitcoin", 35600.92, "10.11.2023 00:42", "$"), "elindanila@gmail.com")