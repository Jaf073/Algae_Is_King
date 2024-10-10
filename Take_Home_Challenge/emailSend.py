from email.message import EmailMessage
import ssl
import smtplib

emailSender = '' # put your own here while testing

senderPass = ''  # NOTE: You want to use something called an "app password" for this feild, it's something that you can set up with gmails ONLY if you have two factor authentication enabled
# obviously don't leave this filled in when you push to git

emailVictim = '' # put somebody you don't like here while testing

subject = 'This is a test email subject'
body = """
This is a test email body
This should be a seperate line
"""

email = EmailMessage()
email['From'] = emailSender
email['To'] = emailVictim
email['Subject'] = subject
email.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, senderPass)
    
    # uncommenting the following command will send the email out
    # DO NOT UNCOMMENT THIS DURING LARGE SCALE TESTING
    # smtp.sendmail(emailSender, emailVictim, email.as_string())
