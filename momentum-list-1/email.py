# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()


def send_email():
    message = Mail(
        from_email=(os.getenv('FROM_EMAIL'), 'Evan Kanter'),
        to_emails=[os.getenv('TO_EMAIL_1'), os.getenv('TO_EMAIL_2')],
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

def send_email_custom(subject: str, body: str):
    message = Mail(
        from_email=(os.getenv('FROM_EMAIL'), 'Evan Kanter'),
        to_emails=[os.getenv('TO_EMAIL_1'), os.getenv('TO_EMAIL_2'), os.getenv('TO_EMAIL_3')],
        subject=subject,
        html_content=body.replace("\n", "<br/>"))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

if __name__ == "__main__":
    send_email()
