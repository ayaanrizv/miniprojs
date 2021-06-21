import smtplib
from email.message import EmailMessage

email = EmailMessage()  # email object
email['from'] = 'Ayaan'
email['to'] = 'receiver_email'
email['subject'] = 'You won 1,000,000 dollars'
email.set_content('No you did\'nt hahahahahha')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # hello
    smtp.starttls()  # encryption --securely
    smtp.login('sender_email', 'sender_email_pass')  # make sure less secure app access is turned on for this to work
    smtp.send_message(email)
    print("all good boss!")
