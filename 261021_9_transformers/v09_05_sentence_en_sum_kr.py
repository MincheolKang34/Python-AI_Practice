from deep_translator import GoogleTranslator, MyMemoryTranslator    # 구글 번역, 무료 온라인 번역 서비스
from deep_translator.exceptions import TooManyRequests
from transformers import pipeline
# 다운그레이드
# # pip install transformers==4.57.6
# MyMemory : 이탈리아 Translated사가 운영하는 무료 온라인 번역 서비스. deep-translator가 이 서비스의 공개 API를 호출

summarizer = pipeline("summarization", model="t5-small")

# 2. 요약할 원문(영어 단락)
text = """
In a rapidly changing world, the ability to adapt and learn 
continuously is perhaps the most valuable skill a person can 
possess. While technology transforms industries and creates 
new challenges almost daily, those who embrace curiosity 
rather than fear find themselves better equipped to 
navigate uncertainty. True growth rarely happens inside our 
comfort zones; it is forged through small, deliberate steps 
taken consistently over time. Therefore, patience and 
resilience are just as important as raw talent on the journey 
toward long-term success.
"""

# 3. 요약 실행
summary = summarizer(
    text,
    min_length=20,  # 최소 토큰 수
    max_length=100, # 최대 토큰 수
    do_sample=False # 매번 동일 결과 출력
)

def trans_en_to_kor(sentence:str)->str:
    """
    주어진 영어 문장을 한국어로 번역하는 함수
    """
    try:
        kr_text = GoogleTranslator(source="en", target="ko").translate(sentence)
    except TooManyRequests:  # 구글 일시 차단 시 MyMemory로 대체
        kr_text = MyMemoryTranslator(source="en-US", target="ko-KR").translate(sentence)

    return kr_text

# 4. 결과 확인
sum_text = summary[0]["summary_text"]
# print(f"요약된 문장 : {sum_text}")

# 4-1. 한글 번역


print(f"한국어로 번역 후 요약된 문장 : {trans_en_to_kor(sum_text)}")

"""
한국어로 번역 후 요약된 문장 : 기술은 산업을 변화시키고 거의 매일 새로운 도전을 만듭니다. 호기심을 포용하는 
사람들은 불확실성을 헤쳐나갈 수 있는 능력을 갖추게 됩니다. 인내와 회복력은 원천적인 
재능만큼이나 중요합니다.
"""