import requests

r = requests.get("https://facebook.com")
print(r.status_code)