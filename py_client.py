import requests


endpoint = "http://127.0.0.1:8000/api/post_view/"
get_respone = requests.get(endpoint)
print(get_respone.json())