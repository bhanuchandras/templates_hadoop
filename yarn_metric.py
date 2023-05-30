import requests
from datetime import datetime, timedelta
import pandas as pd

# Create a pandas dataframe.
df = pd.DataFrame()


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

    return int(start_time.timestamp()*1000), int(end_time.timestamp()*1000)
start_time, end_time = get_time_range("1h")
# Make the request to the Hadoop jobhistory API.
headers = {
    "Accept": "application/json"
}

params = {
    "startedTimeBegin": start_time,
    "startedTimeEnd": end_time
}

response = requests.get(url, headers=headers, params=params)

# Check the response status code.
if response.status_code == 200:
    # The request was successful.
    jobs = response.json()

    # Print the job information.
    for job in jobs["apps"]["app"]:
        df = df.append({
        "job_id": job["id"],
        "user": job["user"],
        "queue": job["queue"],
        "job_name": job["name"],
        "job_status": job["state"],
        "job_finalstatus": job["finalStatus"],
        "job_start_time": job["startedTime"],
        "job_end_time": job["finishedTime"],
        "job_duration": job["elapsedTime"],
        "job_type": job["applicationType"],
    }, ignore_index=True)
    # Group the dataframe by job status.
    grouped_df = df.groupby("job_status")

    # Calculate the percentage of jobs in each status.
    grouped_df["percentage"] = grouped_df["count"] / len(df) * 100

    # Print the grouped dataframe.
    print(grouped_df)
else:
    # The request failed.
    print(response.status_code)
    print(response.content)
