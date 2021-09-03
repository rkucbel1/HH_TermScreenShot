#Get the term data from .json file and upload it to the database
import json
import requests
import os

path_to_image = os.environ.get('PATH_TO_HH_SCREENSHOT_IMAGE')
link_hh_terms = os.environ.get('LINK_HH_TERMS')
api_weekend_or_holiday = os.environ.get('LINK_WEEKEND_OR_HOLIDAY')
token = os.environ.get('PA_API_TOKEN')

#Get most recent data from .json file
with open(path_to_image + '/HH_TermData.json', 'r') as f:
    f_contents = f.read()

new_data = json.loads(f_contents)

#Get the most recent date
current_date = new_data['Updated']
print('Current Date', current_date)

#Get the last date as from database
url = link_hh_terms
r = requests.get(url)
old_data = json.loads(r.text)
last_date = old_data[-1]['Updated']
print('Database last updated date: ', last_date)

#Get if today is a weekend or holiday
url = api_weekend_or_holiday
data = requests.get(url)
status = json.loads(data.text)
status = status[-1]['status']

#Update the database  if current_date != last_date.
if (current_date == last_date) or (status == 'MKT_CLOSED'):
   print(status) 
   print('No update')

else:
    url = link_hh_terms
    headers = {'Authorization': token}

    payload = new_data

    resp = requests.post(url, headers=headers, data=payload)
    print('http response:',resp)
