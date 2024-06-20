from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# 크롬 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 네이버 남대문시장 페이지로 이동
driver.get("https://m.place.naver.com/place/13304144/review/visitor?entry=plt")

# wait 설정
wait = WebDriverWait(driver, 10)

# '더보기' 버튼을 반복적으로 클릭하여 모든 리뷰 로드
while True:
    try:
        more_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fvwqf')))
        driver.execute_script("arguments[0].click();", more_button)
        time.sleep(1)  # 페이지 로드 시간 대기
    except Exception:
        break

# 모든 리뷰 요소 추출
reviews = driver.find_elements(By.CLASS_NAME, 'zPfVt')
review_list = [review.text for review in reviews]

# 크롬 드라이버 종료
driver.quit()

# 리뷰를 CSV 파일로 저장
df = pd.DataFrame(review_list, columns=["Review"])
df.to_csv("naver_review.csv", index=False, encoding='utf-8-sig')

print("리뷰가 naver_review.csv 파일에 저장되었습니다.")
