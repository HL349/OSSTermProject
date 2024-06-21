import requests
import json
import pandas as pd
import sys
import re

df = pd.read_csv('kakao_review.csv', encoding='utf-8-sig')

# 전처리
def preprocess_text(text):
     text = re.sub(r'[^가-힣 ]', '', str(text), re.UNICODE)  # 한글 제외한 문자 제거
     text = re.sub(r'\b더보기\b', '', str(text))  # 더보기 문자 제거
     text = re.sub('\s+', ' ', text).strip() # 불필요한 공백 문자 제거
     return text


df['리뷰'] = df['리뷰'].apply(preprocess_text)
df = df[df['리뷰'] != '']

# 중복 제거
df = df.drop_duplicates(subset=['리뷰'], keep='first')

review_text = df['리뷰']

# 네이버 API 사용 시 필요한 키로 개인 발급 받아야 함
client_id = "8z47hfo7sw"
client_secret = "OFnp7HqkiGS0WyuxjF1Fli3LGKzdnnIVquIYhNb4"

url="https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"
headers={   "X-NCP-APIGW-API-KEY-ID": client_id, 
            "X-NCP-APIGW-API-KEY": client_secret,
            "Content-Type": "application/json"}

sentiment = []
negative = []
positive = []
neutral = []

for i in review_text:
    content = i
    data  = {
        "content": content
    }

    response = requests.post(url,headers=headers, data=json.dumps(data) )
    rescode = response.status_code

    if rescode == 200:
        parsed_data = response.json()

        senti = parsed_data['document']['sentiment']
        sentiment.append(senti)

        confidence = parsed_data['document']['confidence']
        negative.append(confidence['negative'])
        positive.append(confidence['positive'])
        neutral.append(confidence['neutral'])
    else:
        print("Error:", response.text)

data = {
    'review': review_text,
    'sentiment': sentiment,
    'negative': negative,
    'positive': positive,
    'neutral': neutral
}
result_df = pd.DataFrame(data)
print(result_df)

negative_reviews = result_df[result_df['sentiment'] == 'negative']
print(negative_reviews)

print("-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----")

positive_reviews = result_df[result_df['sentiment'] == 'positive']
print(positive_reviews)
result_df.to_csv('kakaosentiment_analysis_result.csv',index=False, encoding='utf-8-sig')
negative_reviews.to_csv('kakaonegative_review.csv',index=False, encoding='utf-8-sig')
positive_reviews.to_csv('kakaopositive_review.csv',index=False, encoding='utf-8-sig')
