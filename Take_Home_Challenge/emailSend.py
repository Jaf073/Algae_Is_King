from email.message import EmailMessage
import ssl
import smtplib
from splitInfo_02 import splitInfo

emailSender = '' # put your own here while testing

senderPass = ''  # NOTE: You want to use something called an "app password" for this field, it's something that you can set up with gmails ONLY if you have two factor authentication enabled
# obviously don't leave this filled in when you push to git

emailVictim = '' # put somebody you don't like here while testing

Dic1, Dic2, Dic3 = splitInfo('finished.txt')

with open('email_template.txt', 'r') as file:
          email_template = file.read()

def replaceEmails(name_dic):
    filledOutEmails = []
    for name, emailVictim in name_dic.items():
        email = EmailMessage()
        email['From'] = emailSender
        email['To'] = emailVictim
        email['Subject'] = 'This is a test email subject'

        contents = email_template
        contents = contents.replace('[target]', name)
        contents = contents.replace('fakeemail@email.com', emailSender)
        contents = contents.replace('[your worst nightmare]', emailSender)

        email.set_content(contents)

        with open('IESB.jpeg', 'rb') as img:
            email.add_attachment(img.read(), maintype='image', subtype='jpeg', filename='IESB.jpeg')

        filledOutEmails.append(email)

    return filledOutEmails

preppedEmails = []
preppedEmails.extend(replaceEmails(Dic1))
preppedEmails.extend(replaceEmails(Dic2))
preppedEmails.extend(replaceEmails(Dic3))

context = ssl.create_default_context()

for email in preppedEmails:
    emailVictim = email['To']

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, senderPass)
    
        # uncommenting the following command will send the email out
        # DO NOT UNCOMMENT THIS DURING LARGE SCALE TESTING
        #emailVictim = '' # if you want to do your own. put a 'break' after the next line
        #smtp.sendmail(emailSender, emailVictim, email.as_string())
