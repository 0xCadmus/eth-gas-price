# Reference https://docs.deversifi.com/docs#getV1TradingRGetGasPrice
# Returns ETH gas price in wei

import requests
import json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

url = "https://api.stg.deversifi.com/v1/trading/r/getGasPrice"

response = requests.request(
    "GET",
    url,
    headers=headers,
)

gasPrice = json.dumps(response.json(), indent=2)
gasPrice = json.loads(gasPrice) # Convert to dictionary