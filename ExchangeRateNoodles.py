import requests

# 환율 정보 가져오기 함수
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency)

# 특정 항목의 가격 가져오기 함수
def get_price_of_item(file_path, item_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if item_name in line:
            price_str = line.split(':')[1].strip().replace(',', '')
            return int(price_str)
    return None

# 파일 경로
file_path = "C:\Users\Path\Price\PriceFinal.txt"

# 특정 항목의 가격 가져오기 (잔치국수)
item_name = "잔치국수"
average_price = get_price_of_item(file_path, item_name)

if average_price is None:
    print(f"{item_name}의 가격을 찾을 수 없습니다.")
else:
    # 사용자로부터 변환할 나라 입력 받기
    target_currency = input("어느 나라의 화폐로 변경할 것인지 입력하세요 (예: USD, EUR, JPY): ").upper()

    # 원화를 선택한 화폐로 변환
    exchange_rate = get_exchange_rate('KRW', target_currency)
    if exchange_rate:
        converted_price = average_price * exchange_rate
        print(f"평균 {item_name} 가격 ({target_currency}): {converted_price:.2f} {target_currency}")
    else:
        print("환율 정보를 가져오는 데 실패했습니다.")
