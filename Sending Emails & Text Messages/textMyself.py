#! python3
# textMyself.py - Defines function that texts the message passed t it as argument

# Credentials:
accSID = '################################'
token = '################################'

myNumber = "##########"
twilioNumber = '##########'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accSID,token)
    twilioCli.messages.create(body = message,from_=twilioNumber,to = myNumber)

textmyself('This is great!')