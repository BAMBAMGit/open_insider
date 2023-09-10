# Create a calendar
import pandas_market_calendars as mcal
import pandas as pd
nyse = mcal.get_calendar('NYSE')

# Getting the previous trading day and the next trading day  --> this is to help with scraping insider trading data from the correct previous date. and for setting the correct date for setting stops
# also helps for setting the correct date for setting the final sell date.

# Get the current date
current_date = pd.Timestamp.now().date()

# Calculate dates for 14 days ahead and 10 days behind
dates_ahead = [current_date + pd.DateOffset(days=i) for i in range(1, 15)]
dates_behind = [current_date - pd.DateOffset(days=i) for i in range(1, 11)]

# Convert the dates to 'YYYY-MM-DD' string format
current_date_str = current_date.strftime('%Y-%m-%d')
dates_ahead_str = [date.strftime('%Y-%m-%d') for date in dates_ahead]
dates_behind_str = [date.strftime('%Y-%m-%d') for date in dates_behind]

# Print the dates
print("Dates 10 Days Ahead:")
print(dates_ahead_str)

print("\nDates 10 Days Behind:")
print(dates_behind_str)

# find next trading day
current_date_str = '2023-09-10'
for d in dates_ahead_str:
  dates_df = nyse.schedule(start_date=current_date_str, end_date=d)
  if len(dates_df) > 0:
    next_trading_day = d
    print('\nnext_trading_day:',next_trading_day)
    break

# find previous trading day
for d in dates_behind_str:
  dates_df = nyse.schedule(start_date=d, end_date=current_date_str)
  if len(dates_df) > 0:
    previous_trading_day = d
    print('previous_trading_day:',previous_trading_day)
    break

print(dates_ahead_str[::-1])
# find 14 days ahead
for d in dates_ahead_str[::-1]:
  dates_df = nyse.schedule(start_date=d, end_date=d)
  if len(dates_df) == 1:
    days_ahead_14 = d
    print('days_ahead_14:',days_ahead_14)
    break