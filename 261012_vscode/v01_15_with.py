# 새롭게 생성, 기존 내용이 있다면 덮어씀
# with open("memo.txt", "w", encoding="utf-8") as f:
#     f.write("새로운 한 줄 추가")

# 파일 읽기
# with open("memo.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# print(text) # 새로운 한 줄 추가

# 파일 이어 쓰기
# with open("memo.txt", "a", encoding="utf-8") as f:
#     f.write("\n줄바꿈 가능합니까?")

# x 모드(새 파일 만들기)
# try:
#     fname = input("텍스트 파일명을 입력하세요 : ") + ".txt"
#     with open(fname, "x", encoding="utf-8") as f:
#         f.write("새로 추가하나요? 막나요?")
# except FileExistsError:
#     print("이미 존재하는 파일입니다.")

# rb 모드(이미지 읽기)
with open("images.jpg", "rb") as img:
    r_img = img.read()
# print(r_img)

# wb 모드(이미지 쓰기)
# with open("wb_img.jpg", "wb") as m_img:
#     m_img.write(r_img)

# r+ 모드(읽기와 쓰기 둘 다)
with open("memo.txt", "r+", encoding="utf-8") as f:
    text = f.read() # 먼저 읽기
    f.seek(0)       # 맨 앞부터 수정
    f.write("새롭게 시작")  # 새로 쓰기
    # f.write(text.replace("새로운", "낡은")) # 문자 변경
    f.truncate()    # 나머지 내용 제거

print("완료")