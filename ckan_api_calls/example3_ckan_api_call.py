import requests
import json

# List all tags not in vocabularies:
url = 'http://localhost:5000/api/action/tag_list'
response = requests.post(url)
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")

# List all vocabularies:
url = 'http://localhost:5000/api/action/vocabulary_list'
response = requests.post(url)
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")

# Create new user:
url = 'http://localhost:5000/api/action/user_create'
response = requests.post(url, json.dumps({'name': 'api_created_user', 'email': 'api@user.com', 'password': 'ABCDABCD123!'}), headers={"Content-Type": "application/json", "Authorization": "471d0a38-e12d-4eb4-b723-80da92b988c5"})
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")

# Create new vocabulary, 'vocabulary1':
url = 'http://localhost:5000/api/action/vocabulary_create'
response = requests.post(url, json.dumps({'name': 'vocabulary2'}), headers={"Content-Type": "application/json", "Authorization": "471d0a38-e12d-4eb4-b723-80da92b988c5"})
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")

# Create new tag, 'tag1', in vocabulary1:
url = 'http://localhost:5000/api/action/tag_create'
response = requests.post(url, json.dumps({'name': 'tag1', 'vocabulary_id': 'cd152cd9-1a9f-4444-bb4a-223a59a7f61e'}), headers={"Content-Type": "application/json", "Authorization": "471d0a38-e12d-4eb4-b723-80da92b988c5"})
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")

# List all tags in vocabulary1:
url = 'http://localhost:5000/api/action/tag_list'
response = requests.post(url, json.dumps({'vocabulary_id': 'vocabulary1'}), headers={"Content-Type": "application/json"})
print(response)
print(json.dumps(response.json(), indent=4, sort_keys=True))
print(" ")


