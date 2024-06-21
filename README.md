[매뉴얼]

ExchangeRateNoodles.py
- 잔치국수 환율 모델

ExchangeRateTteokbokki.py
- 떡볶이 환율 모델

Front.html
- 프런트
- 각 모듈 실행 후 저장 -> 각 버튼 클릭 후 저장된 결과 불러오기 방식으로 화면에 띄우기

KakaoMapReview.py
- 카카오맵 리뷰
- '검색할 키워드를 입력하세요: ' 라고 띄워지면 터미널에 키워드 입력
- 결과는 csv로 저장

NaverReview.py
- 네이버 지도 리뷰
- 리뷰 페이지 url 직접 코드에 입력해야함
- 결과는 csv로 저장

Price.py
- 이미지(Price.zip)에서 텍스트 추출
- 이미지 전처리, 모든 이미지에 대해서 처리

PriceTxtExtract.py
- Price.py에서 '떡볶이'와 '잔치국수'에 대한 가격만 추출
- 그것에 대한 평균 값 계산 및 출력

ReviewSentimentKakao.py
- 텍스트 전처리
- 네이버 클로바 API 사용

ReviewSentimentNaver.py
- 텍스트 전처리
- 네이버 클로바 API 사용

ReviewTranslationKakao.py
- 파파고 번역 API 사용
- 리뷰 번역

ReviewTranslationNaver.py
- 파파고 번역 API 사용
- 리뷰 번역

SummaryKakao.py
- 긍정, 부정 리뷰 키워드 요약

SummaryNaver.py
- 긍정, 부정 리뷰 키워드 요약

# [외국인을 위한 전통시장 리뷰 및 가격표 보급 시스템]

• 프로젝트 요약

◦각 시장의 리뷰를 ‘네이버 지도’ 또는 ‘카카오 맵’ 등의 리뷰 사이트에서 모아 한눈에 파악할 수 있도록 하고, 긍정적/부정적 리뷰로 분류하며 키워드로 요약된 전체적인 시장의 리뷰를 알 수 있도록 한다.   
◦리뷰 사이트에서 모아온 리뷰를 각 선택된 언어로 번역한다.

◦시장의 가격표를 찍은 사진을 모은 후 음식의 평균적인 가격을 알 수 있도록 하며, 환율 계산을 하여 서비스 이용자인 외국인들이 정확한 가격을 알 수 있도록 한다.

1. 지도 웹사이트의 리뷰 크롤링
- 네이버 지도/카카오 맵에서 특정 전통시장(남대문 시장)의 리뷰를 자동으로 수집하고 이를 CSV 파일로  저장하여 데이터 분석에 활용하는 것을 목표로 함.

. [사용한 기술과 도구]

① 프로그래밍 언어: Python               ④ 웹 드라이버: Selenium       
② 데이터 처리 및 저장: pandas           ⑤ 브라우저 자동화 도구: ChromeDriver
③ 크롬 드라이버 관리: webdriver_manager (네이버 지도)
④ HTML 파싱: BeautifulSoup (카카오 맵)

링크: [카카오맵 리뷰](https://github.com/HL349/OSSTermProject/blob/main/KakaoMapReview.py), [네이버리뷰](https://github.com/HL349/OSSTermProject/blob/main/NaverReview.py)

※	크롬 웹드라이버 버전 호환 주의, Selenium으로 동작할 때 웹페이지의 HTML 문서 분석 필요
-	예시: 카카오맵 검색창의 XPATH를 가져와야 하는 경우, 카카오맵 검색창에서 마우스 오른쪽 버튼을 클릭하여 검사를 누르면 HTML 문서에서 해당 요소 복사 가능

![image](https://github.com/HL349/OSSTermProject/assets/163121438/0c46786a-762b-4434-bebb-27766cb07056)

[실행 결과- 총 106개의 리뷰 수집]

![image](https://github.com/HL349/OSSTermProject/assets/163121438/744b52e1-461d-4520-a768-8122609becad)

![image](https://github.com/HL349/OSSTermProject/assets/163121438/e2b0e603-22ce-4225-b021-3e2daab64046)

2. 리뷰 감정 분석 시스템
- 네이버 지도/카카오맵에서 수집한 리뷰 데이터를 분석하여 긍정, 부정, 중립으로 분류하고, 각 리뷰의 감정 점수를 산출하여 CSV 파일로 저장하는 것을 목표로 함.

[사용한 기술과 도구]

① 프로그래밍 언어: Python  ② 데이터 처리 및 저장: pandas       
③ 정규 표현식: re (텍스트 전처리) ④ 네이버 감정 분석 API: Naver Clova Sentiment
⑤ HTTP 요청: requests

링크: [리뷰감정분석-카카오](https://github.com/HL349/OSSTermProject/blob/main/ReviewSentimentKakao.py),
[리뷰감정분석-네이버](https://github.com/HL349/OSSTermProject/blob/main/ReviewSentimentNaver.py)
※	네이버 API 사용시 필요한 키 개인 발급 필요, 사용 구조 파악 및 변형

[실행 결과]

positive, neutral, negative 로 감정 분류 및 각각의 추정 확률값
![image](https://github.com/HL349/OSSTermProject/assets/163121438/7f6ce898-d574-46a0-8225-3eb93685b73a)

Positive review만 따로 추출-총 38개
![image](https://github.com/HL349/OSSTermProject/assets/163121438/42aceffa-9388-4aad-ab61-83edea910d00)

Negative review만 추출- 총 14개
 ![image](https://github.com/HL349/OSSTermProject/assets/163121438/31320030-d858-4514-8a5a-6e87feb05266)

3. 리뷰 요약 시스템

. [사용한 기술과 도구]

① 프로그래밍 언어: Python                 ④ HTTP 요청: requests  
② 데이터 처리 및 저장: pandas              
③ 텍스트 요약 API: Naver Cloud Platform(Naver Clova Summary)

링크: [리뷰요약서비스-카카오](https://github.com/HL349/OSSTermProject/blob/main/SummaryKakao.py),
      [리뷰요약서비스-네이버](https://github.com/HL349/OSSTermProject/blob/main/SummaryNaver.py)

[실행 결과]
![image](https://github.com/HL349/OSSTermProject/assets/163121438/2a6cdb6a-739f-46d0-bac9-15057d50c152)

4. 리뷰 번역 시스템
- 리뷰 데이터를 사용하여 사용자가 입력한 언어 코드에 따라 리뷰를 번역하고, 번역된 결과를 데이터프레임으로 출력하는 것을 목표로 함.

[사용한 기술과 도구]

① 프로그래밍 언어: Python                 ④ HTTP 요청: requests  
② 데이터 처리 및 저장: pandas              
③ 번역 API: Naver Papago API

링크: [리뷰번역시스템-카카오](https://github.com/HL349/OSSTermProject/blob/main/ReviewTranslationKakao.py),
[리뷰번역시스템-네이버](https://github.com/HL349/OSSTermProject/blob/main/ReviewTranslationNaver.py)

[실행 결과]
긍정 리뷰 요약, 부정 리뷰 요약에 대해 일본어로 번역한 예시
![image](https://github.com/HL349/OSSTermProject/assets/163121438/943d7022-1baf-486c-a0fd-f6d58e94ba83)

5. 가격표 이미지 내 가격 정보 추출 후 평균 가격 산출 시스템
- 가격표 이미지로부터 가격 정보 텍스트를 추출하여 특정 음식의 평균 가격을 산출하는 것을 목표로 한다. Tesseract OCR 엔진을 활용하여 이미지 내의 텍스트를 인식하고, 이를 전처리 과정을 거쳐 최종적으로 텍스트로 출력한다. 출력한 가격 정보 텍스트로 평균 가격을 계산한다.

. [사용한 기술과 도구]
① 프로그래밍 언어: Python             ④ HTTP 요청 및 데이터 처리: requests        
② 라이브러리: OpenCV(이미지 처리), Tesseract OCR(텍스트 인식)        
③ 외부 도구: Tesseract-OCR 바이너리 설치   

링크: [가격표 인식](https://github.com/HL349/OSSTermProject/blob/main/Price.py)

6. 평균 가격 환율 변환 시스템
- 실시간 환율 정보를 활용하여 사용자가 입력한 나라의 화폐로 변환된 음식(떡볶이/잔치국수)    의 평균 가격을 출력 하는 것을 목표로 함.

. [사용한 기술과 도구]
① 프로그래밍 언어: Python                 ④ HTTP 요청 및 데이터 처리: requests
② 환율 API: ExchangeRate-API              
③ 사용자 입력 처리: Python의 내장 함수 및 문자열 처리 기능

링크: [환율 변환](https://github.com/HL349/OSSTermProject/blob/main/PriceTxtExtract.py)

[실행 결과]
떡볶이 가격에 대해 일본 엔화로 환전
![스크린샷 2024-06-21 145836](https://github.com/HL349/OSSTermProject/assets/131737162/984bc416-f2c9-4eb1-a1ba-59efc845a5cc)

[최종 UI 기능 구현] 
-각 시장의 위치와 크롤링한 리뷰, 추출한 가격 표기 후 그것을 각 나라의 언어와 환율로 바꿔   표기해주는 기능을 출력하는 것을 목표로 함.

링크: [최종 UI](https://github.com/HL349/OSSTermProject/blob/main/Front.html)

. [사용한 기술과 도구]
① 프로그래밍 언어: HTML, Javascript
② 지도 API: google maps api              
③ 사용자 입력 처리: 버튼 클릭

- 기능 및 구현 방법:
1. Google Maps를 통해 시장의 위치를 보여준다. 마커를 클릭하면 그 위치가 지도의 중심으로 이동한다. 
2. 리뷰 데이터와 가격 데이터, 번역 데이터를 버튼을 클릭하면 각각 csv 파일을 로컬파일에서 업로드 한다.
3. 패널 콘텐츠 표시 상태가 사용자의 상호작용의 상태에 따라 표시 상태가 변경된다.







