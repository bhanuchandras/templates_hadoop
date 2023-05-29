import requests
from datetime import datetime, timedelta

# Define the URL of the Hadoop jobhistory API.
#url = "http://localhost:8080/api/v1/jobs"

# Define the function to get the start and end times of the time range to query.
def get_time_range(time_range):
    now = datetime.now()
    if time_range == "1h":
        start_time = now - timedelta(hours=1)
        end_time = now
    elif time_range == "3h":
        start_time = now - timedelta(hours=3)
        end_time = now
    elif time_range == "24h":
        start_time = now - timedelta(days=1)
        end_time = now
    else:
        raise ValueError("Invalid time range")

    return start_time, end_time
start_time, end_time = get_time_range("1h")
# Make the request to the Hadoop jobhistory API.
headers = {
    "Accept": "application/json"
}

params = {
    "start-time": start_time,
    "end-time": end_time
}

response = requests.get(url, headers=headers, params=params)

# Check the response status code.
if response.status_code == 200:
    # The request was successful.
    jobs = response.json()

    # Print the job information.
    for job in jobs:
        print(job["apps"]["app"])

else:
    # The request failed.
    print(response.status_code)
    print(response.content)
