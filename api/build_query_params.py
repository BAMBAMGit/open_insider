# BUILD QUERY PARAMETERS
from api.datetime_helper import date_reformatted_start

# Base URL
base_url = "http://openinsider.com/screener?"

from urllib.parse import urlparse, parse_qs, unquote

minimum_share_price = str(4)
max_filing_delay = str(5)
minimum_dollars_traded = str(20)  # in k's
number_of_officers = str(1)
number_of_insiders = str(1)
group_by_filing_or_company = str(2)  # 0 means by filing, 2 means company
cob = str(1)
ceo = str(1)
pres = str(1)
coo = str(1)
cfo = str(1)

# Define the URL
url = "http://openinsider.com/screener?s=&o=&pl="+minimum_share_price+"&ph=&ll=&lh=&fd=-1&fdr="+date_reformatted_start+"+-+"+date_reformatted_start+"&td=0&tdr=&fdlyl=&fdlyh="+max_filing_delay+"&daysago=&xp=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&iscob="+cob+"&isceo="+ceo+"&ispres="+pres+"&iscoo="+coo+"&iscfo="+cfo+"&grp="+group_by_filing_or_company+"&nfl=&nfh=&nil="+number_of_insiders+"&nih=&nol="+number_of_officers+"&noh=&v2l="+minimum_dollars_traded+"&v2h=&oc2l=&oc2h=&sortcol=0&cnt=1000"

# Parse the URL and extract the query parameters
parsed_url = urlparse(url)
query_parameters = parse_qs(parsed_url.query)

# Convert query parameters to a dictionary
query_params = {key: value[0] if key != 'fdr' and key != 'tdr' else unquote(value[0].replace(" - ", "+-+")) for key, value in query_parameters.items()}

# Print the dictionary
print(query_params)
