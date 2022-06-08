import requests
import uuid
import json

# command and data in json format
# data can take a nested json objects if more then one feild is needed
def sendToMirror(cmd, data):
    requests.post("http://localhost:8080/Mirai-API", data=json.dumps({'cmd': cmd, 'data': data}), headers={'Content-type': 'application/json'})


# needs project_id and Autherization key from user
# takes and uploads the reminder to Todoist
#def addReminder(reminder):
#    requests.post(
#            "https://api.todoist.com/rest/v1/tasks",
#            data=json.dumps({
#                "content": reminder,
#                "project_id": 2267023454
#            }),
#            headers={
#                "Content-Type": "application/json",
#                "X-Request-Id": str(uuid.uuid4()),
#                "Authorization": "Bearer 420429ee162d001d28516b03c667f9b5bfbe07ba"
#            }).json()


# deletes reminder based off of reminder_id
#def deleteReminder(reminder_id):
#    requests.post(
#    "https://api.todoist.com/rest/v1/tasks/" + reminder_id + "/close",
#    headers={
#        "X-Request-Id": str(uuid.uuid4()),
#        "Authorization": "Bearer 0123456789abcdef0123456789"
#    })