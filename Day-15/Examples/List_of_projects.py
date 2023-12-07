from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json


app = Flask(__name__)



@app.route('/jira', methods=['POST'])
def jira():
    


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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))






app.run(host='0.0.0.0',port=5000)