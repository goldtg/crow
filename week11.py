from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd
import os


query_txt = input("검색어 입력: ")

ft_name = './data/' + query_txt + '.txt'
fc_name = './data/' + query_txt + '.csv'
fx_name = './data/' + query_txt + '.xlsx'

if not os.path.exists('./data'):
    os.makedirs('./data', exist_ok=True)

# n = time.localtime
# s = time.strftime("%Y-%m-%d-%c", time.localtime(time.time()))

driver = webdriver.Chrome()
url = 'https://www.naver.com/'
driver.get(url)


element = driver.find_element(By.ID, 'query')

element.send_keys(query_txt)

driver.find_element(By.ID, 'search-btn').click()

driver.find_element(By.LINK_TEXT, '블로그').click()

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')
content_list = soup.find_all('div', class_='view_wrap')

no =1
num =[]
title_ =[]
content_=[]
user_ =[]
date_ =[]

for c in content_list:
    num.append(no)
    print('번호:', no)
    
    title = c.find('div', 'title_area').get_text()
    title_.append(title.strip())
    print('제목:', title.strip())
    user_info = c.find('a', 'name').get_text()
    user_.append(user_info.strip())
    print('작성자:', user_info.strip())
    dsc_area = c.find('div', 'dsc_area').get_text()
    content_.append(dsc_area.strip())
    print('내용:', dsc_area.strip())

    dat = c.find('span', 'sub').get_text()
    date_.append(dat.strip())
    print('작성일자:', dat.strip())

    print('\n')

    if no == 10:
        break

    no += 1

f = open(ft_name, ' ㅈ', encoding='utf-8')
f.write(str(num))
f.write(str(title_))
f.write(str(user_))
f.write(str(content_))
f.close()

naver_blog = pd.DataFrame()
naver_blog['번호'] = num
naver_blog['날짜'] = date_
naver_blog['제목'] = title_
naver_blog['내용'] = content_
naver_blog['작성자'] = user_

naver_blog.to_csv(fc_name, encoding='utf-8-sig', index=False)
print('csv 파일 저장 경로:', fc_name)

naver_blog.to_excel(fx_name)
print('xls 파일 저장 경로:', fx_name)
