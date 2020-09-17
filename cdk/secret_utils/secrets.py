import requests
import base64

def getSecret():
    data = requests.get("https://rancher-requirements-check.kloia.com")
    encoded = base64.b64encode(data.content)

    return encoded.decode("utf-8")