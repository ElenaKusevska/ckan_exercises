import requests
import json

# Get a list of the names of all the users in the curators group:
url = 'http://localhost:5000/api/action/group_show'
response = requests.post(url, json.dumps({'id': 'curators', 'include_users': 'True' }), headers={"Content-Type": "application/json"})

user_names_of_curators_members = []
curators_members = json.loads(response.text)['result']['users']
for i in range (0, len(curators_members)):
    user_names_of_curators_members.append(curators_members[i]['name'])

print('user_names_of_curators_members', user_names_of_curators_members)
print(" ")

# List all groups:
url = 'http://localhost:5000/api/action/group_list'
response = requests.post(url, json.dumps({'id': 'curators'}), headers={"Content-Type": "application/json"})
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")

# get_site_user:
api_key = "471d0a38-e12d-4eb4-b723-80da92b988c5"
url = 'http://localhost:5000/api/action/get_site_user'
response = requests.post(url, json.dumps({'id': 'curators', 'include_users': 'True' }), headers={"Content-Type": "application/json", "Authorization": api_key})
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")

