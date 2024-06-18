from selenium import webdriver
from selenium.webdriver.common.by import By
import PyPDF2
import os
import time
from selenium.webdriver.chrome.options import Options
import requests



options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ssl-protocol=TLSv1.2")
driver = webdriver.Chrome(options=options)

search_term = input("검색어를 입력하세요: ")
num_files = int(input("저장할 PDF 파일 개수를 입력하세요: "))

driver.get('https://www.google.com/webhp?hl=ko&sa=X&ved=0ahUKEwjIw8Xi2uKGAxX1s1YBHe3eDrEQPAgJ')
search_box = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
search_box.click()
search_box.send_keys(search_term)
search_box.send_keys('\n')
def scroll_down(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    


for i in range(num_files):
    # PDF 파일 링크 찾기
    pdf_links = driver.find_elements(By.CSS_SELECTOR, 'a[href$=".pdf"]')
    
    # PDF 파일 다운로드
    if pdf_links:
        pdf_link = pdf_links[i]
        pdf_url = pdf_link.get_attribute('href')
        response = requests.get(pdf_url)
        with open(f'{search_term}_{i+1}.pdf', 'wb') as file:
            file.write(response.content)
    else:
        print(f"No PDF file found for index {i}")