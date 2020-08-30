import requests
from requests.auth import HTTPDigestAuth

# define user and password
user = 'theuser'
passwd = 'thepass'

# TODO: use the basic authentication methon
#url = 'https://httpbin.org/basic-auth/theuser/thepass'
#resp = requests.get(url, auth=(user, passwd))
#print(resp.status_code)
#print(resp.text)

# TODO: use the digest authentication method
url = 'https://httpbin.org/digest-auth/theuser/thepass'
resp = requests.get(url, auth=HTTPDigestAuth(user, passwd))
print(resp.status_code)
print(resp.text)