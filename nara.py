from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd
import os

search = input("공고명으로 검색할 키워드는 무엇입니까?: ")
before_date = input("조회 시작일자 입력 (예: 2019/01/01): " )
after_date = input("조회 종료일자 입력 (예: 2019/01/01): " )
folder = input("파일로 저장할 폴더 이름을 쓰세요(예: c:\data\): ")

if not os.path.exists(folder):
    os.makedirs(folder)
os.chdir(folder)

driver = webdriver.Chrome()
url = 'https://www.g2b.go.kr/index.jsp'
driver.get(url)

#검색어 기입
search_box = driver.find_element(By.CSS_SELECTOR,"#bidNm")
search_box.click()
search_box.send_keys(search)

#시작 일정 기입
be_date= driver.find_element(By.CSS_SELECTOR,"#fromBidDt")
be_date.click()
be_date.clear()
be_date.send_keys(before_date)

#종료 일정 기입
be_date= driver.find_element(By.CSS_SELECTOR,"#toBidDt")
be_date.click()
be_date.clear()
be_date.send_keys(after_date)

#검색버튼
driver.find_element(By.CSS_SELECTOR, "a>strong").click()

subject_ = []
num_ =[]
classfi_=[]
title_=[]
pro_=[]
demand_=[]
meth_=[]
input_time_=[]
supply_=[]
bid=[]

select_frame1=driver.find_element(By.NAME,"sub")
driver.switch_to.frame(select_frame1)
select_frame2=driver.find_element(By.NAME,"main")
driver.switch_to.frame(select_frame2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

ex1= soup.find_all('tr')

print(ex1[1].get_text())

for i in range(len(ex1)):
    result = ex1[i].get_text()
    subject_.append(result)
    print(subject_)




# outer_frame = soup.find("frame", id="sub")
# print(outer_frame)
# inner_frame = outer_frame.find_all("#document")
# print(inner_frame)


# if outer_frame:
#     if inner_frame:
#         r=soup.find_all("p")
#         print(r)




time.sleep(500)


