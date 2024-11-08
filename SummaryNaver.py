import requests
import pandas as pd
import re
import json

# 긍정 리뷰 키워드 요약
pos_df = pd.read_csv('naverpositive_review.csv', encoding='utf-8-sig')

positive_reviews = pos_df['review'] # 긍정 리뷰 데이터프레임
content = positive_reviews.tolist()
all_content = "\n".join(content)

# 발급받은 API 키
client_id = "client_id" 
client_secret = "client_secret"

# 긍정 리뷰 요약

url = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"
headers = {"X-NCP-APIGW-API-KEY-ID": client_id,
          "X-NCP-APIGW-API-KEY": client_secret,
          "Content-Type": "application/json"}


data = {
  "document": {
    "content": all_content
  },
  "option": {
    "language": "ko",
    "model": "general",
    "tone": 3,
    "summaryCount": 3
  }
}

response = requests.post(url,headers=headers, data =json.dumps(data))
rescode = response.status_code

if rescode == 200:
    pos_summary = response.json()['summary']
    print(pos_summary)
else:
    print(f"Error Code: {response.status_code}, Message: {response.text}")



# 부정 리뷰 키워드 요약
neg_df = pd.read_csv('navernegative_review.csv', encoding='utf-8-sig')

negative_reviews = neg_df['review'] 
content2 = negative_reviews.tolist()
all_content2 = "\n".join(content2)

# 발급받은 API 키
client_id = "client_id" 
client_secret = "client_secret"

# 부정 리뷰 요약

url = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"
headers = {"X-NCP-APIGW-API-KEY-ID": client_id,
          "X-NCP-APIGW-API-KEY": client_secret,
          "Content-Type": "application/json"}


data = {
  "document": {
    "content": all_content2
  },
  "option": {
    "language": "ko",
    "model": "general",
    "tone": 3,
    "summaryCount": 3
  }
}

response = requests.post(url,headers=headers, data =json.dumps(data))
rescode = response.status_code

if rescode == 200:
    neg_summary = response.json()['summary']
    print(neg_summary)
else:
    print(f"Error Code: {response.status_code}, Message: {response.text}")


summary_df = pd.DataFrame({'positive_summary': pos_summary, 'negative_summary': neg_summary}, index = range(0,1))
      
print(summary_df)

summary_df.to_csv("naversummary.csv", encoding="UTF-8-sig", index=False)
