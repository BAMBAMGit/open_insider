import pandas as pd
from api.scraper_script import scrape_openinsider_and_return_df
from api.build_query_params import query_params, base_url


# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Loop through pages until there is no data left
page = 1
# while True:
for r in range(50):
  # Add the 'page' parameter to the query parameters
  query_params['page'] = page

  # Construct the full URL
  full_url = base_url + "&".join([f"{param}={value}" for param, value in query_params.items()])

  # Scrape the data for the current page
  try:
    df = scrape_openinsider_and_return_df(full_url)
    print('page',page,full_url)

  # If there's no data on the current page, exit the loop
  except:
    print('You reached the end of the road.')
    break

  # Concatenate the data to the combined DataFrame
  combined_df = pd.concat([combined_df, df], ignore_index=True)

  # Move to the next page
  page += 1

# df_copy = combined_df.copy()
# df = df_copy.copy()

# df

table_html = df.to_html(classes='table table-striped table-bordered')