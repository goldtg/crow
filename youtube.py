from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd
import os

query_txt = input("검색어 입력: ")

driver = webdriver.Chrome()
url = 'https://www.youtube.com/'
driver.get(url)

search_box = driver.find_element(By.CSS_SELECTOR,"input#search")
search_box.click()
search_box.send_keys(query_txt)
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,"#search-icon-legacy").click()


time.sleep(1000)