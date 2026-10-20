from groq import Groq
from dotenv import load_dotenv  # .env 읽는 도구
import os


# 1. .env의 GROQ_API_KEY키를 환경변수로 불러옴
load_dotenv()

# 2. 키로 Groq 클라이언트 만들기(키를 통해서 요청)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. 질문 보내기
res = client.chat.completions.create(
    model="openai/gpt-oss-20b", # 무료, 빠름. 20b = 모델 파라미터 수(200억)
    messages=[
        {
            "role": "user", # 질문이나 요청할 때
            "content": "groq은 grok이랑 뭐가 다른거야?" # 질문
        }
    ]
)

# 4. 답변 받기
result = res.choices[0].message.content
print(result)