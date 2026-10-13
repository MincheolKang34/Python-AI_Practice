# 람다 함수 => 일회용 함수
# 함수명 = lambda 매개변수 : 반환값

# 기본 함수
# def add(a, b):
#     return a + b
# print((add(7, 10)))

# 람다 함수
# add = lambda a, b : a + b
# print(add(10, 10))

import pyfiglet

# pyfiglet 기본 함수
def decorate_text(text):
    return pyfiglet.figlet_format(text)

# pyfiglet 람다 함수
decorate_text_lambda = lambda text : pyfiglet.figlet_format(text)
py_text = decorate_text_lambda("lambda")
print(py_text)