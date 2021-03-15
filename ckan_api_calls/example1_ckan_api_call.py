import requests
import json

url = 'http://localhost:5000/api/action/status_show'

response = requests.post(url)
print(response)

#print the response text (the content of the requested file):
#print(response.content)
#print(response.text)
print(json.dumps(response.json(), indent=4, sort_keys=True))

# convert to python dictionary:
dict_response = json.loads(response.text)

# convert back to json object:
y = json.dumps(dict_response)


