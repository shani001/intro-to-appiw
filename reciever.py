import requests

f=requests.get("http://127.0.0.1:5000/home")
print(f.json())