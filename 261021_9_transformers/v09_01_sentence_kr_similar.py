from sentence_transformers import SentenceTransformer, util

# 1. 모델 로드
model = SentenceTransformer("jhgan/ko-sroberta-multitask")
# 모델 설명 :
    # https://github.com/jhgan00/ko-sentence-transformers 참고

# 2. 비교할 두 문장 정의
# 2-1. 의미상 완전히 다른 두 문장 예시 -> 낮은 유사도 기대
# sen1 = "고양이가 소파 위에서 자고 있다"
# sen2 = "내일 학교에 수학 시험이 있다."
# 2-2. 의미상 비슷한 문장 예시 -> 높은 유사도 기대
sen1 = "그는 도서관에서 책을 읽고 있다."
sen2 = "책을 읽는 그는 도서관에 있다."
# 2-3. 비슷한 단어
# sen1 = "개"
# sen2 = "강아지"

# 3. 문장 -> 숫자 좌표로 바꾸기(인코딩)
emb1 = model.encode(sen1, convert_to_tensor=True)
emb2 = model.encode(sen2, convert_to_tensor=True)

# 4. 두 문장 유사도 측정(코사인 유사도)
cos_sim = util.pytorch_cos_sim(emb1, emb2)

# 5. 결과 출력
print(f"두 문장의 유사도 : {cos_sim.item():.4f}")

"""
sen1 = "고양이가 소파 위에서 자고 있다"
sen2 = "내일 학교에 수학 시험이 있다."

두 문장의 유사도 : -0.0405
"""

"""
sen1 = "그는 도서관에서 책을 읽고 있다."
sen2 = "책을 읽는 그는 도서관에 있다."

두 문장의 유사도 : 0.9413
"""

"""
sen1 = "개"
sen2 = "강아지"

두 문장의 유사도 : 0.7976
"""