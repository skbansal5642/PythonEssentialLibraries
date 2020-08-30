import requests

# TODO: use a timeout value for a request
#resp = requests.get("https://httpbin.org/delay/0.5",timeout=1.0)
#print(resp.status_code)

# TODO: introspect the redirection history
#resp = requests.get('https://www.github.com')
#print(resp.url)
#print(resp.history)
#orig = resp.history.pop()
#print(orig.status_code)
#print(orig.url)
#print(orig.reason)

# TODO: use a session object to group requests and settings
sess = requests.Session()
#sess.get("https://httpbin.org/cookies/set/sample/123456789")

#resp = sess.get("https://httpbin.org/cookies")
#print(resp.text)

sess.headers.update({
    "User-Agent": "Mozilla/5.0 (x11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/80.0"
})
resp = sess.get("http://google.com")
print(len(resp.content))

sess.headers.update({
    "User-Agent": "Mozilla/5.0 (x11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/80.0"
})

resp = sess.get("http://google.com")
print(len(resp.content))
