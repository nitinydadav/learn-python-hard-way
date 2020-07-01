import requests

print(dir(requests))
print("\n")
url = "https://www.linkedin.com/developers/apps/verification/92f1390a-3665-4f54-bea4-551c6e6551c6"
rqs = requests.get(url)
print(dir(rqs))
print("\n")
print(rqs.content)

r = requests.post("https://www.linkedin.com/developers/apps/verification/92f1390a-3665-4f54-bea4-551c6e6551c6", data = {'key':'value'})

