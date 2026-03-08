import smtplib
from email.mime.text import MIMEText

EMAIL="vaibhav4122020@gmail.com"
APP_PASSWORD="YOUR_APP_PASSWORD"

def send_otp(receiver_email,otp):
    msg=MIMEText(f"Your OTP is: {otp}")
    msg["Subject"]="OTP Verification"
    msg["From"]=EMAIL
    msg["To"]=receiver_email

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(EMAIL,APP_PASSWORD)
    server.sendmail(EMAIL,receiver_email,msg.as_string())
    server.quit()
