from transformers import pipeline
# 다운그레이드
# # pip install transformers==4.57.6

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
"""
번역 : 빠르게 변하는 세상에서 끊임없이 적응하고 배우는 능력은 아마도 
사람이 가질 수 있는 가장 소중한 기술일 것입니다. 기술이 산업을 
변화시키고 새로운 도전을 거의 매일 만들어내지만, 두려움보다 호기심을 
가진 사람들은 불확실성을 더 잘 헤쳐 나갈 수 있습니다. 진정한 성장은 
익숙한 영역 안에서 일어나기보다는, 시간이 지나면서 꾸준히 의도적으로 
내딛는 작은 발걸음들을 통해 이루어집니다. 따라서 장기적인 성공을 향한 
여정에서는 타고난 재능만큼이나 인내와 회복력도 매우 중요합니다.
"""

# 3. 요약 실행
summary = summarizer(
    text,
    min_length=20,  # 최소 토큰 수
    max_length=100, # 최대 토큰 수
    do_sample=False # 매번 동일 결과 출력
)

# 4. 결과 확인
sum_text = summary[0]["summary_text"]
print(f"요약된 문장 : {sum_text}")

"""
요약된 문장 : technology transforms industries and creates new 
challenges almost daily . those who embrace curiosity find 
themselves better equipped to navigate uncertainty . patience 
and resilience are just as important as raw talent .
"""
"""
번역 : 기술은 거의 매일 산업을 변화시키고 새로운 도전을 만들어냅니다. 
호기심을 가진 사람들은 불확실성을 더 잘 헤쳐 나갈 수 있습니다. 
인내와 회복력은 타고난 재능만큼이나 중요합니다.
"""