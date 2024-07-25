from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# set up selenium stuff
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

chrome_driver_path = '/usr/bin/chromedriver' # update this path if necessary

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# fetch data
reddit_user_url = 'https://www.reddit.com/user/dealingwith1/'

driver.get(reddit_user_url)

time.sleep(1)
height = driver.execute_script("return document.body.scrollHeight")
for i in range(5):
    driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));");
    print("page height: ", height)
    height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(1) # wait for page to load

page_source = driver.page_source

driver.quit()

with open("reddit_user_page.html", "w", encoding="utf-8") as file:
    file.write(page_source)


