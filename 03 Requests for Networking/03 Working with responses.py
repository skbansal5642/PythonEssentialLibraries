import requests

# TODO: work with status codes
#resp = requests.get("https://httpbin.org/status/200")
#resp = requests.get("https://httpbin.org/status/404")
#print(resp.status_code)
#resp.raise_for_status()

# TODO: examine the response encoding
#resp = requests.get("https://httpbin.org/html")
#print(resp.encoding)
#print(resp.text)
#print(resp.content)

# TODO: To read json content, use the json() function
resp = requests.get("https://httpbin.org/json")
print(resp.json)
print(resp.headers)
print(resp.headers['content-type'])