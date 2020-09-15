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

    # message for late nights
    late_nights = "I'm probably asleep by now bug, but here are a few reminders: don't be too hard on yourself, you're wonderful, beautiful and very capable. sleep well and sweet dreams <3 "
    anxiety = "I know the past couple weeks have been really hard to get through and it doesn't feel like it right now, but you're safe, you're ok, and this will end. I love you so much and I hope you always feel like you're flying on appa with warm winds and beautiful views. Sleep well and sweet dreams bug <3 "

    hydration_is_key = "drink some water. Hydration is key :)"

    # get time of day
    timeOfDay = datetime.now().strftime("%H:%M")
    print("time of day: ", timeOfDay)

    hour = timeOfDay.split(':')[0]
    # print(hour)
    # exit()
    # get message to send
    # and add reminders for the day based on the time of day it is :)
    message_to_Send = "REMINDER: It is: " + timeOfDay +". I know time doesn't make sense and it's ok to loose track of time. \n"

    if hour > "09" and hour < lunch:
        message_to_Send += breakfast_message + "\n and " + hydration_is_key + " I love you and if I don't see you today sending all my love and hugs. Don't forget to write down your dreams, so you can tell me about them :')"
    elif hour >= lunch and hour < dinner:
        message_to_Send += lunch_message + "\n and " + hydration_is_key + " I love you and if I don't see you today sending all my love and hugs"
    elif hour > dinner and hour < "23":
        message_to_Send += dinner_message + "\n and " + hydration_is_key + " I love you and if I don't see you today sending all my love and hugs"
    else:
        message_to_Send = anxiety

    print('sending to: ', phone_number)
    print('sending: ',message_to_Send)
    
    try:
        # guid = imessage.send(phone_number, message_to_Send)
        imessage.send(phone_number, message_to_Send)
        print('SUCCESS: message sent')

        # sleep(5)
        # resp = imessage.status(guid)
        # print('status of message is: ', resp)
        # sleep(5)
        # print('Message was delivered at:', resp.get("date_delivered"))

    except Exception as e:
        print('ERROR: ', e)
        # return error code
        # exit(1)




if __name__=='__main__':
    send_to_ivona()
