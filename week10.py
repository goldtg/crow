from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd

driver = webdriver.Chrome()
url = 'https://www.naver.com/'

driver.get(url)
time.sleep(2)


click_box = driver.find_element(By.CSS_SELECTOR, "input#query.search_input")
click_box.click()
click_box.send_keys("여름 휴가")
search_btn = driver.find_element(By.CSS_SELECTOR, "svg#search-btn" )
search_btn.click()
ex1= driver.find_elements(By.CSS_SELECTOR, "a.tab")
ex1[1].click()


html_sourse =driver.page_source

soup = BeautifulSoup(html_sourse, 'html.parser')

tit = soup.find_all('a', class_ = "title_link")
writer = soup.find_all('a', class_ = "name")
ago = soup.find_all("span", class_ ="sub")
con = soup.find_all("a", class_ ="dsc_link")



num = 1
no = []
title = []
content = []
ago_ = []
writer_ =[]



with open('memo.txt', 'w', encoding='utf-8-sig') as f:
    for i in range(len(tit)):
        f.write(f"번호: {i+1}\n")
        f.write(f"제목: {tit[i].get_text(strip=True)}\n")
        f.write(f"작성자: {writer[i].get_text(strip=True)}\n")
        f.write(f"작성 시간: {ago[i].get_text(strip=True)}\n")
        f.write(f"내용: {con[i].get_text(strip=True)}\n")
        f.write("\n")

for i in range(len(tit)):
    no.append(i+1)
    ex2 = tit[i].get_text(strip=True)
    title.append(ex2)

for i in range(len(writer)):
    writer_name = writer[i].get_text(strip=True)
    writer_.append(writer_name)

for i in range(len(ago)):
    wr_time = ago[i].get_text(strip=True)
    ago_.append(wr_time)
    print(ago_)

for i in range(len(con)):
    co = con[i].get_text(strip=True)
    content.append(co)

# print(len(tit),len(writer),len(ago_),len(con))

ago_.remove('‘여름휴가’관련광고')
ago_.remove('도움말')




print("완료")

sub = pd.DataFrame()
sub['번호'] = no
sub['작성자'] = writer_
sub['제목'] = title
sub['내용'] = content
sub['작성일자'] = ago_

sub.to_excel("여름휴가.xlsx", index=False)
sub.to_csv("여름휴가.csv", index=False, encoding='utf-8-sig')

time.sleep(1000)