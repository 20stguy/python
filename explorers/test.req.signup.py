import requests
import json


url = "http://localhost:8080/api/auth/signup"

data = {'username': 'st4rt_2',
        'email': 'email_2@email.com',
        'password': '1234_2'}

headers = {'Content-type': "application/json", 'Accept': 'text/plain'}

res = requests.post(url, data=json.dumps(data), headers=headers)

print(res.text)