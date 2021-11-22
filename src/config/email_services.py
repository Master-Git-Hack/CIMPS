from smtplib import SMTP
from src.config import email_name as user, email_pwd as pwd
def send_email(message,to_Email):
    try:
        # Start server conecction 
        smtp_session= SMTP('smtp.gmail.com', 587)
        # Encryt the connection
        smtp_session.starttls()

        # Sign In at server
        smtp_session.login(user,pwd)

        # Send email
        smtp_session.sendmail(user, to_Email, message)
        
        # Finish server connection
        smtp_session.quit() 
        return True
    except Exception as e:
        print(f'An error occurred at Email Service: {e}')
        return False