# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lavanurrevanthreddy258.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("lavanurrevanthreddy258@gmail.com", "ATATT3xFfGF0lScKakjdfWzWnocyLsF589LfkUp8UY5ueVUn5AVugxP5LGkpmyHhJzkTqTXYHCX4f3lTbQmHhDXOuyKF6S-jSX-57JGX9HGgrfms7U87nR2TXM6zOUmLvNZXosP2JcspZmo9IloXWnaxnuNuBRqvmpFANACONE5-3UYkt1Ys6VE=8734DF32")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


output = json.loads(response.text)

name = output[1]["name"]
name1 = output[0]["name"]
print(name)
print(name1)