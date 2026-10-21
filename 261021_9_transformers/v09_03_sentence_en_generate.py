from transformers import pipeline

# 1. 텍스트 생성 파이프라인 생성
generator = pipeline("text-generation", model="gpt2")   # 최초 1회 모델 다운로드 필요

# 2. 시드 문장 입력 (이어 쓸 첫 부분)
q = input("이어서 쓸 첫 문장을 입력해주세요 : ")

# 3. 텍스트 생성 실행
results = generator(
    q,
    max_new_tokens=50,      # 추가 생성할 토큰 수(길수록 추론 시간도 길어짐)
    num_return_sequences=1,  # 반환 문장 1개로 설정
)

# 4. 결과 출력
print(results[0]["generated_text"])

"""
이어서 쓸 첫 문장을 입력해주세요 : However, suddenly ninja has appeared!! 

However, suddenly ninja has appeared!! Everyone is so excited for them!! The world is moving forward!! And what is this all about?!

I'll have to explain more soon.

Chapter 40: The Mysterious One

(TLN: It's possible that the title
"""
"""
번역)

그런데 갑자기 닌자가 나타났어!! 모두가 그들을 정말 기대하고 있어요!! 세상이 앞으로 나아가고 있어요!! 이게 도대체 무슨 이야기예요?!

곧 더 자세히 설명드리겠습니다.

제40장: 신비로운 자

(TLN: 제목이 그럴 가능성이 있습니다
"""
