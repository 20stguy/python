import requests
import json

url = "http://localhost:8080"
data = {"msg": "This is msg from python"}
# header = {"content-type": "application/json", "Accept": "text/plain", "x-access-token": "iwantaconnect!"}
header = {"content-type": "application/json", "Accept": "text/plain"}
r = requests.post(url, data=json.dumps(data), headers=header)

print(r.status_code) # nodejs에서 보내주는 satus code출력(200)
print(r.text) # nodejs에서 보내주는 상태 출력




