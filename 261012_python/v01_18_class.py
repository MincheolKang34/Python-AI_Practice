# 클래스, 객체 생성 실습
# 속성 3개, 메서드 2개
# 객체 2개 이상

class Phone:
    def __init__(self, name, prod, ai):
        self.name = name
        self.prod = prod
        self.ai = ai

    def info(self):
        print(f"저는 {self.name}이고, {self.prod}에 의해 제조되었으며, {self.ai} AI 비서를 제공해드리고 있습니다.")

    def call_ai(self):
        ai_name = input("AI 비서 이름을 불러주세요 : ")
        if ai_name == self.ai:
            print("네, 부르셨나요?")

# 객체 2개 이상
galaxy_s26 = Phone("갤럭시S26", "삼성", "빅스비")
iphone_18pro = Phone("아이폰18프로", "애플", "시리")

# 메서드 2개 호출
galaxy_s26.info()
galaxy_s26.call_ai()

iphone_18pro.info()
iphone_18pro.call_ai()
