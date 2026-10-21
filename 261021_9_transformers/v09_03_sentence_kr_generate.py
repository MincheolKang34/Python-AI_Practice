from transformers import pipeline

# 1. 텍스트 생성 파이프라인 생성
generator = pipeline("text-generation", model="Bllossom/llama-3.2-Korean-Bllossom-3B")   # 최초 1회 모델 다운로드 필요
# 모델 설명 : https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B 참고

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
이어서 쓸 첫 문장을 입력해주세요 : 그런데 갑자기 닌자가 나타났다!

그런데 갑자기 닌자가 나타났다! 닌자는 매우 강력한 힘을 가지고 있었고, 
그는 이 전투에서 이겨야만 한다고 생각했다. 닌자는 자신이 이긴다면, 
그 지역의 모든 사람들을 보호할 수 있게 되고,
"""
