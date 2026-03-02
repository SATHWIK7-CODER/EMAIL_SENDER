import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# ─────────────────────────────────────────
#   CONFIGURATION -- Edit these details
# ─────────────────────────────────────────

SENDER_EMAIL = "vvsssathwik82@gmail.com"    # Your Gmail address
SENDER_PASS  = "pxal xejq xlsr ffyb"     # Your 16-letter App Password

# List of recipients -- add as many as you want
CONTACTS = [
    {"name": "loki",       "email": "vvsslohi9@gmail.com"},
    {"name": "kaili",      "email": "kalisrin2@gmail.com"},
    {"name": "srnu",       "email": "vurakarana2@gmail.com"},
    {"name": "sk",         "email": "saisriji05@gmail.com"}
]

ATTACHMENT = None   # Set to a file path like "report.pdf" or leave None



#   FUNCTION 1: Build the email message

def build_email(to_name, to_email):
    msg = MIMEMultipart()
    msg['From']    = SENDER_EMAIL
    msg['To']      = to_email
    msg['Subject'] = f"Hello {to_name}!"

    # Email body -- personalized for each person
    body = f"""Dear {to_name},

This is an automated email sent using Python.

 It uses smtplib and the email library to:
  - Create and format email messages
  - Connect securely to Gmail's SMTP server
  - Send personalized emails automatically

This project demonstrates email automation using Python.

Best regards,
Python Email Bot"""

    msg.attach(MIMEText(body, 'plain'))

    # Attach a file if provided
    if ATTACHMENT and os.path.exists(ATTACHMENT):
        with open(ATTACHMENT, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(ATTACHMENT)}')
        msg.attach(part)

    return msg


#   FUNCTION 2: Send emails to all contacts

def send_emails():
    try:
        # Connect to Gmail's SMTP server securely
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASS)
            print("Login successful!\n")

            sent_count = 0

            for contact in CONTACTS:
                name  = contact['name']
                email = contact['email']

                msg = build_email(name, email)
                server.sendmail(SENDER_EMAIL, email, msg.as_string())

                print(f"Email sent to {name} ({email})")
                sent_count += 1

            print(f"\nDone! {sent_count} email(s) sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and App Password.")

    except smtplib.SMTPRecipientsRefused:
        print("One or more recipient emails are invalid.")

    except smtplib.SMTPConnectError:
        print("Could not connect to Gmail. Check your internet connection.")

    except Exception as e:
        print(f"An error occurred: {e}")


#   RUN THE PROGRAM

if __name__ == "__main__":
    print("Starting Email Sender...\n")
    send_emails()