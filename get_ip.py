import requests
response = requests.get("http://ifconfig.me/all")
print(response.text)
