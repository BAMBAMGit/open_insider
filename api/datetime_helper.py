# DATESTRING REFORMATTER HELPER FUNCTION

from datetime import datetime
from api.get_market_days import previous_trading_day

def format_date(date_string):
    # Convert the input date string to a datetime object
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')

    # Create a new date string in the 'MM/DD/YYYY' format
    formatted_date_string = date_obj.strftime('%m/%d/%Y')

    # Replace '/' with '%2F' to match the desired format
    formatted_date_string = formatted_date_string.replace('/', '%2F')

    return formatted_date_string

date_reformatted_start = format_date(previous_trading_day)
date_reformatted_end = date_reformatted_start

print(date_reformatted_start, date_reformatted_end)
