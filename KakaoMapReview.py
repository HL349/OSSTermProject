from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
from time import sleep
import time
import pandas as pd
import re

# Chrome 웹드라이버 경로 설정

driver = webdriver.Chrome()

# 크롤링할 URL
url = "https://map.kakao.com/"
driver.get(url)
time.sleep(5)    # 페이지 로드 될 때까지 대기

query = input('검색할 키워드를 입력하세요: ') # 터미널에 키워드 입력(남대문시장)

# 검색어 창을 찾아 search 변수에 저장 (By.XPATH 방식)
search_box = driver.find_element(By.XPATH, '//*[@id="search.keyword.query"]') # 개발자 도구(F12)로 검색창 XPATH 직접 확인
search_box.send_keys(query)
search_box.send_keys(Keys.ENTER)
time.sleep(5)

# 검색어 입력 후 나오는 첫 번째 항목의 상세보기 버튼 클릭
detailviews = driver.find_element(By.XPATH, '//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]')
detailviews.send_keys(Keys.ENTER)
driver.switch_to.window(driver.window_handles[-1]) # 카카오맵은 상세보기를 누르면 새 창이 열리기 때문에 새로운 창으로 넘어가야 함
time.sleep(3)

# 리뷰 탭 클릭
review_tap = driver.find_element(By.CSS_SELECTOR, '#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > div.location_evaluation > a:nth-child(3)')
review_tap.click()
time.sleep(3)

# 더보기 버튼이 안 나올 때까지 눌러 모든 리뷰 로드
while True:    
    try:
        moreviews = driver.find_element(By.CSS_SELECTOR, '#mArticle > div.cont_evaluation > div.evaluation_review > a > span.txt_more')
        moreviews.click()
        time.sleep(0.1)
    except:
        print('클릭완료')
        break

# 리뷰 수집
review = driver.find_elements(By.CLASS_NAME, 'txt_comment')
#more_button = driver.find_element(By.CSS_SELECTOR, '#mArticle > div.cont_evaluation > div.evaluation_review > ul > li:nth-child(14) > div.comment_info > p > button')
review_list = []

for i in range(len(review)):
    #if more_button.is_displayed():
        #more_button.click()    
    if review[i].text.strip():   # 텍스트가 있는 리뷰만 수집
        review_text = review[i].text.strip()   
        review_list.append(review[i].text)    
print(review_list)


dic = {'리뷰': review_list}

df = pd.DataFrame(dic)


print(df)


df.to_csv('kakao_review.csv', index=False, encoding='utf-8-sig')
