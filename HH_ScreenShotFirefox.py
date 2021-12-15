#Program to take a screen shot at url
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os

path_to_image = os.environ.get('PATH_TO_HH_SCREENSHOT_IMAGE')

url = 'https://www.barchart.com/futures/quotes/NGY00/futures-prices'

profile_loc = os.path.expanduser('~/.mozilla/firefox/comrimyc.default-release/')

firefox_options = Options()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--headless')
firefox_options.add_argument('--windowsize=1920,890')
fp = webdriver.FirefoxProfile(profile_loc)

driver = webdriver.Firefox(fp, executable_path='/usr/bin/geckodriver', options=firefox_options)
driver.maximize_window()

try:
   time.sleep(3)
   screen = driver.get(url)
   time.sleep(10)
   driver.get_screenshot_as_file(path_to_image + '/HH_FirefoxScreenShot.png')

finally:
   driver.close()
