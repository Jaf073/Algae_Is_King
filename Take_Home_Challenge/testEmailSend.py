# from email.message import EmailMessage
# import ssl
# import smtplib

# emailSender = '' # put your own here while testing

# senderPass = ''  # NOTE: You want to use something called an "app password" for this field, it's something that you can set up with gmails ONLY if you have two factor authentication enabled
# # obviously don't leave this filled in when you push to git

# emailVictim = '' # put somebody you don't like here while testing

# Dic = {'Andrew':'alr051@latech.edu', 'Kaylee':'kma072@latech.edu', 'Hayden':'hpr016@latech.edu', 'John':'jaf073@latech.edu', 'Tommy':'tpw006@email.latech.edu', 'Tim':'tcf006@latech.edu', 'Gabe':'gat015@latech.edu', 'Anky':'kiremire@latech.edu'}

# with open('email_template.txt', 'r') as file:
#           email_template = file.read()

# def replaceEmails(name_dic):
#     filledOutEmails = []
#     for name, emailVictim in name_dic.items():
#         email = EmailMessage()
#         email['From'] = emailSender
#         email['To'] = emailVictim
#         email['Subject'] = 'This is a test email subject'

#         contents = email_template
#         contents = contents.replace('[target]', name)
#         contents = contents.replace('fakeemail@email.com', emailSender)
#         contents = contents.replace('[your worst nightmare]', emailSender)

#         email.set_content(contents)

#         with open('IESB.jpeg', 'rb') as img:
#             email.add_attachment(img.read(), maintype='image', subtype='jpeg', filename='IESB.jpeg')

#         filledOutEmails.append(email)

#     return filledOutEmails

# preppedEmails = []
# preppedEmails.extend(replaceEmails(Dic))

# context = ssl.create_default_context()

# for email in preppedEmails:
#     emailVictim = email['To']

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(emailSender, senderPass)
    
#         # uncommenting the following command will send the email out
#         # DO NOT UNCOMMENT THIS DURING LARGE SCALE TESTING
#         #emailVictim = '' # if you want to do your own. put a 'break' after the next line
#         smtp.sendmail(emailSender, emailVictim, email.as_string())

print("Emails Sent")