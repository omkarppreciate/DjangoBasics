import requests

endpoint = "https://httpbin.org/anytghjhing"

response = requests.get(endpoint,json={"query": "hello world"})

print(response.status_code)