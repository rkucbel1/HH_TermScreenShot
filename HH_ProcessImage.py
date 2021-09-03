#Program to process images and extract text data
#Use space.ocr API to process. API key: environment variable
#API documentation:https://ocr.space/OCRAPI
import json
import requests
from datetime import date
import re
import os

path_to_image = os.environ.get('PATH_TO_HH_SCREENSHOT_IMAGE')
api_key = os.environ.get('SPACE_OCR_API_KEY')

#Open an image file and send to space.ocr to process into text
filename = path_to_image + '/HH_Cropped1FF.png'
payload = { 'apikey': api_key, 'language': 'eng', 'scale': 'true', 'OCREngine': '1'}

with open(filename, 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image', files={filename: f}, data=payload,)

data = r.content.decode()
text_terms = json.loads(data)

filename = path_to_image + '/HH_Cropped2FF.png'
payload = { 'apikey': api_key, 'language': 'eng', 'scale': 'true', 'OCREngine': '2'}

with open(filename, 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image', files={filename: f}, data=payload,)

data = r.content.decode()
text_price = json.loads(data)

#Post-process the string data
#First get the front month and based on that determine term data from lookup table
print(text_terms['ParsedResults'][0]['ParsedText'])

string_text_terms = str(text_terms['ParsedResults'][0]['ParsedText'])
string_text_terms = string_text_terms.upper()
string_text_terms = string_text_terms.split('\r\n')

current_month = string_text_terms[0]
current_month = current_month.split('(')
current_month = current_month[1]
current_month = current_month.split(' ')
current_month = current_month[0]
print(current_month)

month_lookup = {'JAN':['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
          'FEB': ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
          'MAR': ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
          'APR': ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
          'MAY': ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
          'JUN': ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
          'JUL': ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          'AUG': ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
          'SEP': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
          'OCT': ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'],
          'NOV': ['Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr'],
          'DEC': ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']}

#Second get the price data and make a string with individual price elements
print(text_price['ParsedResults'][0]['ParsedText'])

string_text_price = str(text_price['ParsedResults'][0]['ParsedText'])
string_text_price = string_text_price.split('\n')

#Filter out any character not a digit or decimal (sometimes the OCR adds random characters)
i=0
for i in range(len(string_text_price)):
    string_text_price[i] = re.sub("[^0-9^.]", "", string_text_price[i])
    i = i+1

#Third get a date to timestamp the data
today = date.today()
today = str(today)

#Finally write term and price data to a json file for use by other scripts/programs
term_data = {}
term_data['Updated'] = today
term_data['T1_Month'] = month_lookup[current_month][0]
term_data['T2_Month'] = month_lookup[current_month][1]
term_data['T3_Month'] = month_lookup[current_month][2]
term_data['T4_Month'] = month_lookup[current_month][3]
term_data['T5_Month'] = month_lookup[current_month][4]
term_data['T6_Month'] = month_lookup[current_month][5]
term_data['T1_price'] = string_text_price[0]
term_data['T2_price'] = string_text_price[1]
term_data['T3_price'] = string_text_price[2]
term_data['T4_price'] = string_text_price[3]
term_data['T5_price'] = string_text_price[4]
term_data['T6_price'] = string_text_price[5]

def writeToJSONFile(path, filename, data):
    filePathNameWExt = '/' + path + '/' + filename + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

path = path_to_image
filename = 'HH_TermData'
writeToJSONFile(path, filename, term_data)
