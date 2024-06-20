import os
import cv2
import pytesseract

# Tesseract 경로 설정 (필요시 수정)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 기본 이미지 경로 템플릿
image_path_template = r"C:\Users\mousy\TermProjectTest\Price\Price{}.png"
output_file = r"C:\Users\mousy\TermProjectTest\Price\PriceFinal.txt"

N = 1

with open(output_file, 'w', encoding='utf-8') as f:
    while True:
        # 현재 N값을 이미지 경로에 적용
        image_path = image_path_template.format(N)
        
        # 파일 존재 여부 확인
        if os.path.exists(image_path):
            # 파일이 존재하면 이미지를 읽고 출력
            img = cv2.imread(image_path)
            
            # 이미지가 잘못 읽혔을 경우 오류 방지
            if img is None:
                print(f"Failed to load image at {image_path}")
                N += 1
                continue
            
            # 이미지 전처리
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

            # 글자 추출
            text = pytesseract.image_to_string(img_thresh, lang='kor')

            # 공백 제거
            text = text.replace(" ", "").strip()
            
            if text:  # 텍스트가 있는 경우에만 파일에 쓰기
                f.write(f'{text}\n')
                print('Detected text:', text)
            
            # N값을 증가
            N += 1
        else:
            # 파일이 존재하지 않으면 루프 종료
            print(f"No more images found at N={N}.")
            break