import smtplib 
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_NO = os.getenv("TWILIO_TOKEN")
ACC_SID = os.getenv("TWILIO_ACC_SID")


class NotificationManager:
    def __init__(self):
        self.smtp_address = os.getenv("SMTP_ADDRESS")
        self.email_app_pass = os.getenv("EMAIL_APP_PASS")
        self.myemail = os.getenv("MY_EMAIL")
        self.twilio_what_no = os.getenv("TWILIO_WHAT_NO")
        self.twilio_verified_no = os.getenv("TWILIO_VERIFIED_NO")
        
        self.client = Client(ACC_SID, TOKEN_NO)
        self.connection = smtplib.SMTP(self.smtp_address)
        
    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.myemail, password=self.email_app_pass)
            
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.myemail, 
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode("wtf-8")
                )
    
    def send_notification(self, message_text):
        message = self.client.messages.create(
            from_= self.twilio_what_no,
            body=message_text,
            to=self.twilio_verified_no,
        )
        print(message.sid)