#! /usr/local/bin/python3
'''
This is to send ivona automated messages throughout the day to eat and drink water 
The message will be customized by the time of day and sent through jenkins 

NOTE: maybe a despair message for like 2/3a vibes
'''

from py_imessage import imessage
from datetime import datetime
from time import sleep

def send_to_ivona():
    
    # messages by day
    # phone to send to
    phone_number = "4086809977"
    # testing_phone = "4085109943"

    # variables to be used for meals of the day
    lunch = "13"
    dinner = "18"
    
    # get message based on time of day
    #  ex: if >=noon: remember to have some lunch etc..
    breakfast_message = "Don't forget to get some caffeine and have some breakfast"
    lunch_message = "Don't forget to eat lunch today"
    dinner_message = "Don't forget to have some dinner today"

    hydration_is_key = "drink some water. Hydration is key :)"

    # get time of day
    timeOfDay = datetime.now().strftime("%H:%M")
    print("time of day: ", timeOfDay)

    hour = timeOfDay.split(':')[0]


    # get message to send 
    # and add reminders for the day based on the time of day it is :)
    message_to_Send = "REMINDER: It is: " + timeOfDay +". I know time doesn't make sense and it's ok to loose track of time. \n"

    if hour < lunch:
        message_to_Send += breakfast_message + "\n and " + hydration_is_key + " I love you and if I don't see you today sending all my love and hugs"
    elif hour >= lunch and hour <= dinner:
        message_to_Send += lunch_message + "\n and " + hydration_is_key + " I love you and if I don't see you today sending all my love and hugs"
    else:
        message_to_Send += dinner_message + "\n and " + hydration_is_key + " I love you and if I don't see you today sending all my love and hugs"
    

    print('sending to: ', phone_number)
    print('sending: ',message_to_Send)    
    
    try:
        # guid = imessage.send(phone_number, message_to_Send)
        imessage.send(phone_number, message_to_Send)
        print('SUCCESS: messages sent')

        

        # sleep(5)
        # resp = imessage.status(guid)
        # print('status of message is: ', resp)
        # sleep(5)
        # print('Message was delivered at:', resp.get("date_delivered"))

    except Exception as e:
        print('ERROR: ', str(e))

    


if __name__=='__main__':
    send_to_ivona()

