from transformers import pipeline

# 1. 감정 분석 파이프라인 생성
classifier = pipeline("sentiment-analysis", model="dlckdfuf141/korean-emotion-kluebert-v2")
# 모델에 대한 자세한 내용은 https://huggingface.co/dlckdfuf141/korean-emotion-kluebert-v2 참고

# 2. 분석할 문장 입력
# 2-1. 긍정 문장
# text = "나 오늘 완전 기분 좋아."
# 2-2. 부정 문장
# text = "그녀는 오늘 행복하지 않아."
# 2-3. 부정 단어
text = "분노"

# 3. 문장 분석
results = classifier(text)

def id_to_emotion(id:int)->str:
    match id:
        case 0:
            return "공포"
        case 1:
            return "놀람"
        case 2:
            return "분노"
        case 3:
            return "슬픔"
        case 4:
            return "중립"
        case 5:
            return "행복"
        case 6:
            return "혐오"
    

# 4. 결과 확인
print(f"문장 분석 결과 : {id_to_emotion(results[0]['label'])}")
# 1에 가까울수록 모델 확신도 높음
print(f"문장 분석 점수 : {results[0]['score']:.4f}")

"""
text = "나 오늘 완전 기분 좋아."
문장 분석 결과 : 행복
문장 분석 점수 : 1.0000
"""

"""
text = "그녀는 오늘 행복하지 않아."
문장 분석 결과 : 슬픔
문장 분석 점수 : 0.9999
"""

"""
text = "분노"
문장 분석 결과 : 분노
문장 분석 점수 : 0.9999
"""