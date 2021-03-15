import requests
import json

# Show all groups
url = 'http://localhost:5000/api/action/group_list'
response = requests.post(url)
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))

print(" ")
print("-----------------------------------------------------")
print(" ")

# Show nonexistent group http query
url = 'http://localhost:5000/api/action/group_show?id=data-explorer'
response = requests.post(url)
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))

print(" ")
print("-----------------------------------------------------")
print(" ")

# Show group that exists using http query
url = 'http://localhost:5000/api/action/group_show?id=curators'
response = requests.post(url)
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))

print(" ")
print("-----------------------------------------------------")
print(" ")

# Show nonexistent group using json query
url = 'http://localhost:5000/api/action/group_show'
response = requests.post(url, json.dumps({'id': 'nonexistent-group'}), headers={"Content-Type": "application/json"})
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))

print(" ")
print("-----------------------------------------------------")
print(" ")

# Show group that exists using json query
url = 'http://localhost:5000/api/action/group_show'
response = requests.post(url, json.dumps({'id': 'curators'}), headers={"Content-Type": "application/json"})
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))


