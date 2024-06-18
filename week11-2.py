import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd
import os
import requests
import urllib
from urllib.parse import urljoin

driver = webdriver.Chrome()
url = 'https://pixabay.com/ko/'
driver.get(url)
time.sleep(2)

search_name = input("1. 크롤링할 이미지의 키워드는 무엇입니까?: ")
search_num = int(input("2. 크롤링 할 건수는 몇 건 입니까?: "))
# f_dir = input("저장 폴더 이름: ")




s = time.strftime("%Y-%m-%d-%c", time.localtime(time.time()))
if not os.path.exists('./ex'):
    os.makedirs('./ex', exist_ok=True)
os.chdir('./ex')


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)

#검색 박스 선택
search_box = driver.find_element(By.TAG_NAME, 'input')
search_box.click()

#검색어 입력
search_box.send_keys(search_name)
search_box.send_keys("\n")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
img_src = soup.find('div', class_ ='results--mB75j').find_all('img')

# print(img_src)
scroll_down(driver)
time.sleep(2)

file_num = 0
count = 1
img_src_ =[]


for i in img_src:
    img_src1 = i['src']
    img_src_.append(img_src1)
    count +=1
    # if not img_src1:
    #     img_src1 = i.get('data-src')
    # if img_src1:
    #     img_src1 = urljoin(driver.current_url, img_src1)
    #     img_src_.append(img_src1)
    #     count += 1
for i in range(0, len(img_src_)):
    if img_src_[i].startswith('/static/img/blank.gif'):
        continue  # 빈 이미지 URL은 건너뛰기
    try:
        urllib.request.urlretrieve(img_src_[i],str(file_num)+'.jpg')
    except (urllib.error.URLError, IOError) as e:
        print(f"Error downloading image {i}: {e}")
        continue
    file_num +=1
    time.sleep(0.5)
    print("%s 번째 이미지 저장중입니다 =====" %file_num)
    




time.sleep(1000)