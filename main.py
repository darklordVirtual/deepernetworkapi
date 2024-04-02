import requests

# Base URL
base_url = 'http://34.34.34.34/api/'

# Endpoints
endpoints = [
    'system-info/network-address',
    'system-info/session-info',
    'admin/getDeviceId',
    'system-info/usage',
    'system-info/hardware-info',
    'liquid',
    'dynamic-data',
    'traffic/session-speed',
    'worldmap-data',
    'inform'
]

# Authorization token add your own key here
headers = {
    'Authorization': 'Bearer yourkey-here'
}

# Function to fetch data from each endpoint
def fetch_data(endpoint):
    response = requests.get(base_url + endpoint, headers=headers)
    if response.ok:
        return response.json()
    else:
        return response.status_code, response.text

# Iterate over endpoints and fetch data
data = {}
for endpoint in endpoints:
    data[endpoint] = fetch_data(endpoint)

# Now 'data' dictionary contains the results from each endpoint
# You can print it out, process it or integrate it into your systems as needed
for key, value in data.items():
    print(f"{key}:\n{value}\n")
