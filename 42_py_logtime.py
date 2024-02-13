import datetime
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from credentials import UID, SECRET, USERNAME

# Make the request
client = BackendApplicationClient(client_id=UID)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url="https://api.intra.42.fr/oauth/token", client_id=UID, client_secret=SECRET)
# response = oauth.get("https://api.intra.42.fr/v2/users/" + USERNAME + "/locations_stats", params={"time_zone": "Europe/Berlin"}) # with timezone, timezone defaults to target users timezone anyway
response = oauth.get("https://api.intra.42.fr/v2/users/" + USERNAME + "/locations_stats")

# (Optional) Print the received object
# print(response.json())

# Get the current date to filter for the current month
today = datetime.date.today()
current_month = today.month
current_year = today.year

# Initialize the total sum of times
total_time_seconds = 0

# Iterate over the response object
for date_str, time_str in response.json().items():
    # Parse the date string
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    
    # Check if the date is in the current month
    if date.month == current_month and date.year == current_year:
        # Parse the time string
        time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S.%f")
        
        # Calculate the total time in seconds
        total_time_seconds += (time_obj.hour * 3600) + (time_obj.minute * 60) + time_obj.second + (time_obj.microsecond / 1000000)

# Convert the total time to hours, minutes, and seconds
total_hours = int(total_time_seconds // 3600)
total_minutes = int((total_time_seconds % 3600) // 60)
total_seconds = int(total_time_seconds % 60)

print(f"Logtime = {total_hours}:{total_minutes}:{total_seconds}")
