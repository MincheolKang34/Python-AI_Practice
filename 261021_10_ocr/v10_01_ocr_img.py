import pytesseract
from PIL import Image
import os

# 1. Tesseract 실행 파일 경로 지정
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# 2. 이미지 불러오기
# image = Image.open("./input.jpg")
# image = Image.open("./input_kr.jpg")
image = Image.open("./input_car_crop.jpg")

# 3. OCR 수행
results = pytesseract.image_to_string(
    image,
    lang="kor"
)

# 4. 결과 출력
print(f"OCR 실행 결과 : {results}")
"""
OCR 실행 결과 : 
This is a lot of 12 point text to test the
ocr code and see if it works on all types
of file format.

The quick brown dog jumped over the
lazy fox. The quick brown dog jumped
over the lazy fox. The quick brown dog
jumped over the lazy fox. The quick
brown dog jumped over the lazy fox.
"""

"""
OCR 실행 결과(한국어만 설정) : 
Ｌ스트스때스56<1때

이수진

팀장 / 제품개발팀

+123-456-7890
1『6110@「62117/8「620[5166.0007
123 40616 56, 407 다, 51 12345
"""

"""
OCR 실행 결과(한국어+영어 설정) : 
LARANASKIN

이수진

팀장 / 제 품 개발팀

+123-456-7890
hello@reallygreatsite.com
123 Anywhere St., Any City, ST 12345
"""

## 1. 번호판 이미지 인식
"""
OCR 실행 결과 : 
"""
## 2. 다른 OCR과 비교
import easyocr

reader = easyocr.Reader(["ko", "en"])

result = reader.readtext("261021_10_ocr/input_car.jpg", detail=0)
print(f"OCR 실행 결과 : {result}")