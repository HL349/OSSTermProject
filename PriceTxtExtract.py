import re

input_file = r"C:\Users\mousy\TermProjectTest\Price\PriceFinal.txt"

# 가격을 추출하기 위한 정규 표현식
price_pattern = re.compile(r'\d+[,.]?\d*')

# 결과를 저장할 딕셔너리
prices = {
    "떡볶이": None,
    "잔치국수": None
}

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if '떡볶이' in line:
            match = price_pattern.search(line)
            if match:
                prices["떡볶이"] = match.group()
        elif '잔치국수' in line:
            match = price_pattern.search(line)
            if match:
                prices["잔치국수"] = match.group()

# 결과 출력
print(f"떡볶이 가격: {prices['떡볶이']}")
print(f"잔치국수 가격: {prices['잔치국수']}")
