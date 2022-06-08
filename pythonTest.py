# imports for sending requests to the mirai server
import requests
import json

# initilize the url and headers for future post requests to the server
url = "http://localhost:3000"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# Use wake word to 'wake up' assistant to then be ready to record your command


def wake_up():
    return True


def take_command():
    command = input("Send command: ")
    return command


def run_mirai():
    command = take_command()

    # Log off mirror
    if "log off" in command:
        r = requests.post(url, data=json.dumps({'msg': 'log off'}), headers=headers)
        print(r.text)

    # Log into mirror
    elif "log on" in command:
        r = requests.post(url, data=json.dumps({'msg': 'log in'}), headers=headers)
        print(r.text)

    # Clear Screen
    elif "clear screen" in command:
        r = requests.post(url, data=json.dumps({'msg': 'clear screen'}), headers=headers)
        print(r.text)

    # Restore Screen
    elif "restore screen" in command:
        r = requests.post(url, data=json.dumps({'msg': 'restore screen'}), headers=headers)
        print(r.text)

    # Turn Mirror on
    elif "wake up" in command:
        r = requests.post(url, data=json.dumps({'msg': 'wake up'}), headers=headers)
        print(r.text)

    # Turn Mirror off
    elif "go to sleep" in command:
        r = requests.post(url, data=json.dumps({'msg': 'go to sleep'}), headers=headers)
        print(r.text)

    # Add reminder to Reminder Module
    # structure of a reminder request:
    # "Mirai remind me to <reminder>"
    elif "remind me" in command:
        try:
            command = command.replace('remind me to', '')
            r = requests.post(url, data=json.dumps({'msg': command}), headers=headers)
            print(r.text)
        except:
            print("Not a valid command")

    # Remove reminder from Reminder Module
    # structure of a delete reminder request:
    # "Mirai cross off my reminder to <reminder>"
    elif "cross off" in command:
        try:
            command = command.replace('cross of my reminder to', '')
            r = requests.post(url, data=json.dumps({'msg': command}), headers=headers)
            print(r.text)
        except:
            print("Not a valid command")

    # Add event to Calender Module
    # structure of a event request:
    # "Mirai add a <event> event to my calander on <date>"
    elif "cross off" in command:
        try:
            command = command.replace('add a', '')
            command = command.replace('event to my calander on', ':')
            command = command.split(":")
            r = requests.post(url, data=json.dumps({'msg': command}), headers=headers)
            print(r.text)
        except:
            print("Not a valid command")
    # Remove event from Calender Module
    # Play song on spotify module
    # Play playlist on spotify module
    # Pause music
    # Resume Music
    # Turn off Spotify Module


while True:
    run_mirai()
#while True:
#    command = input("Enter your command: ")
#    if "mirai" in command:
#        command = command.replace('mirai', '')
#    if command == "quit":
#        break
#    else:
#        r = requests.post(url, data=json.dumps({'msg': command}), headers=headers)
#        print(r.text)
#print("Finished")