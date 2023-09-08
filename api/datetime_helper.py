# DATESTRING REFORMATTER HELPER FUNCTION
from datetime import datetime

def format_date(date_string):
    # Convert the input date string to a datetime object
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')

    # Create a new date string in the 'MM/DD/YYYY' format
    formatted_date_string = date_obj.strftime('%m/%d/%Y')

    # Replace '/' with '%2F' to match the desired format
    formatted_date_string = formatted_date_string.replace('/', '%2F')

    return formatted_date_string

# yesterday's date:
from datetime import datetime, timedelta

# Calculate yesterday's date by subtracting one day --> this is in UTC. --> 6am Los Angeles = 1pm UTC
today = datetime.now()
yesterday = today - timedelta(days=1)

# Format the date as 'YYYY-MM-DD'
formatted_yesterday = yesterday.strftime('%Y-%m-%d')

# Set parameters
date_initial_start = formatted_yesterday
date_initial_end = formatted_yesterday

date_reformatted_start = format_date(date_initial_start)
date_reformatted_end = format_date(date_initial_end)

print(date_reformatted_start, date_reformatted_end)