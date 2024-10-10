'''
ooohhh fancy credits up here ooohhhh
made by the footman at 8:46pm 10/8/24
'''

'''Modify the names into pretty String'''
# includes needed for email sending
from email.message import EmailMessage
import ssl
import smtplib

def getName(name):
    #Find first Dash to split string into First and Last name
    Dash = name.index('-')

    #Get first Name
    firstName = name[:Dash]
    #Uppercase First Letter
    firstName = firstName[0].upper() + firstName[1:]

    #Find index where last name ends
    if '-' in name[Dash+1:]:
        end = Dash + name[Dash+1:].index('-') + 1 
    else:
        end = len(name)-2
        
    lastName = name[Dash+1:end]
    #Uppercase First Letter
    lastName = lastName[0].upper() + lastName[1:]

    #Make full name and return
    newName = firstName + " " + lastName
    return newName

def getEmail(email):
    stop = email.index("\n")
    return(email[:stop])
                       
'''Open Folder and Split information into emails and names'''
def splitInfo(filename):
    nameDict = {}
    with open(filename) as f:
        for x, line in enumerate(f, start=0): #enumerate file into strings
            if line[:6] == '/name/': #Check if string is a name
                name = getName(line[6:])
            elif line[:6] == 'mailto': #Check if string is emal
                email = getEmail(line[7:])
                    
                #If we have the email, we have the name
                nameDict[name] = email
    return(nameDict)
                    
nameDict = splitInfo('finished')

# email variable setup
emailSender = ''
senderPass = '' # note that this needs an app password, not the literal password
subject = 'This is a test email subject'
body = """
This is a test email body
oooooh crazy
third line
"""

# email class setup (continued within loop)
email = EmailMessage()
email['From'] = emailSender
email['Subject'] = subject
email.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, senderPass)

for name, emailVictim in nameDict.items():
    # string formatting goes here


    # DO NOT UNCOMMENT THIS LINE OF CODE
    # THE EMAILS WILL SEND IF YOU RUN THIS
    # (with valid credentials in the emailSender & emailPass variables
    #smtp.sendmail(emailSender, emailVictim, email.as_string())
