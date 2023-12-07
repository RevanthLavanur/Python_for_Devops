import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lavanurrevanthreddy258.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0lScKakjdfWzWnocyLsF589LfkUp8UY5ueVUn5AVugxP5LGkpmyHhJzkTqTXYHCX4f3lTbQmHhDXOuyKF6S-jSX-57JGX9HGgrfms7U87nR2TXM6zOUmLvNZXosP2JcspZmo9IloXWnaxnuNuBRqvmpFANACONE5-3UYkt1Ys6VE=8734DF32"

auth = HTTPBasicAuth("lavanurrevanthreddy258@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "REV"
    },
    "issuetype": {
      "id": "10004"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))