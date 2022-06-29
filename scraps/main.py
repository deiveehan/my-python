import requests

r = requests.get("https://reqres.in/api/users?page=2")
content = r.json()

people = content['data']
for abc in people:
    print(abc['email'])
# print(content['data'][1]['email'])






