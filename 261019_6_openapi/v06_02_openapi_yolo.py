import urllib.request   # 인터넷 주소로 자료 요청하는 도구
import json             # 글자로 된 자료를 사전(dict) 모야으로 바꾸는 도구
import pandas as pd     # 자료를 엑셀 같은 표로 다루는 도구
from ultralytics import YOLO
import cv2


# 1. 인증 키
key = "db5c00dc1fce45c49049bff225a0fea6"
# 과금 우려가 있는 API KEY는 코드 노출 그리고 깃허브에 업로드 하지 않음
# .env 환경변수로 관리

# 2. 도로 유형(its=일반도로, ex=고속도로) -> 어느 도로 CCTV 가져올지 선택
road_type = "its"

# 3. 관심 영역(경도, 위도 범위)
minX, maxX = 120.95, 127.02
minY, maxY = 30.55, 37.69
getType = "json"    # 응답 형식 : JSON(글자로 정리된 자료)

# 4. API URL 조립
url_cctv = (
    f"https://openapi.its.go.kr:9443/cctvInfo"
    f"?apiKey={key}&type={road_type}&cctvType=1"
    f"&minX={minX}&maxX={maxX}"
    f"&minY={minY}&maxY={maxY}&getType={getType}"
)

# 5. 요청(만든 주소로 "자료 주세요!")
response = urllib.request.urlopen(url_cctv)
# print(response)
# <http.client.HTTPResponse object at 0x000001DFB9B8C0D0>

# 6. bytes -> str
json_str = response.read().decode("utf-8") # bytes -> str (사람 글자)
# print(json_str)
json_dict = json.loads(json_str)    # str -> dict (사전 모양)
# print(json_dict)
# {'response': {'coordtype': 1, 'data': [{'roadsectionid': '', 'coordx': 126.2619601, 'coordy': 36.75105767, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도38] 태안 두야교회교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4027/GS9cuqRaCq9cmhurLqU/q/tmpzaPlF57N7gi/wOVZjgQFruIygDd/loR38/6Is3xdvfmWmDxgSSa93CCrXpFZMg57rBqX76Wbs0niTh01ig='}, {'roadsectionid': '', 'coordx': 126.61283, 'coordy': 36.36643, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 21호선] 보령 봉황터널시점', 'cctvurl': 'http://cctvsec.ktict.co.kr/4107/YVJDetuWhH2gGuhzsUBWwJke83GSfQnSZrSa+3kEJS1xmMFFwFW5ohwHwyezBDSnYnpq2HO1jqgtY66Iu6sel5O+4myD62mcqbTR9rqIKTQ='}, {'roadsectionid': '', 'coordx': 126.59544, 'coordy': 36.37853, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 21호선] 보령 봉황터널종점', 'cctvurl': 'http://cctvsec.ktict.co.kr/4108/uEw2V7VUiudn1PsEoqH2s6DPNMx0CC1Hcz8nG8xHkDCJtZLWOiA4CZsmLDQeRbsG3ol/mTvwVwMpFB10QV6QWsvy4d3VuUWZk4k1sRN/epA='}, {'roadsectionid': '', 'coordx': 126.617068, 'coordy': 36.506767, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 21호선] 홍성 단아래사거리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4109/XIgVIAd5Mc+EOXn7+RNsFgyiUJSAA609pgX3G4KT80Um0XiI+KRzZVVPLLnr3eWHH9uNYD7uFp+Qscn5FB9LAuCJp1J8c3OTPrNHixR4PhE='}, {'roadsectionid': '', 'coordx': 126.46391, 'coordy': 36.77537, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 29호선] 서산 석림사거리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4120/bUjLufPLscQPC/m5ncdHsZYrmBQ6Jo82qltJi1bP1hmmFxTm9wS9EwgNZ+2B7+PIZkc1DdDhvtIc6HYRqZJU+UAoz1CWjUB6sK6X1v9COIU='}, {'roadsectionid': '', 'coordx': 126.56381, 'coordy': 36.60075, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 29호선] 홍성 갈산교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4122/WBJX/BxcJa+D8xev6cl9BKZuDkSktqgHtDkkVWWr0vUAy+KU4DNYS7SRVhatzLcKq/PyJcaCMhiXFBNzZnQ3x2pK23bGuKAJSYgL+Ai7KSs='}, {'roadsectionid': '', 'coordx': 126.54518, 'coordy': 36.70661, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 29호선] 서산 해미교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4123/mRjzuG2QEXNol3zpf+raX4p56Gt1VB18r9zbMgfqRup/B1/VtjthJ7t7P9MhCCikRRF1phR3liC1xroJuBASmu2TXOSrQ745BUTPullLRCM='}, {'roadsectionid': '', 'coordx': 126.668438, 'coordy': 36.902131, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 32호선] 당진 감골교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4131/XC9kX72oYhNJsOqOiUb9WIYDsBPaEwrOpF2k1fDpdSluZ4ZX0f7QgNxpvkfJ+sGKE04ehxPtT3DDrPxEy/ttgMYy+zVFVXSBgpdT2uUb6X4='}, {'roadsectionid': '', 'coordx': 126.56319, 'coordy': 36.81245, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 32호선] 서산 운산교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4136/96D1cbn0OLdYhjMM/jsSYNde5hOP8cpZog77Slb99mit7NwNTNQTHNhIz45S5RUn4bJRmIz7jJJ+jweluyu1gnnMhX8MCOMUFG96kLNqsNs='}, {'roadsectionid': '', 'coordx': 126.88307, 'coordy': 36.87125, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 34호선] 아산 인주공단교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4137/1LNLW9ct7cTQQ0vLxyJZaqf2kZpWx+UL6Hf2S/VpG7tNar44Aks/cJASVXsE+CaZUHSHj54l8GFvSceTh3FXKd4U+m2hrKehVUmrzOeEpUU='}, {'roadsectionid': '', 'coordx': 126.86466, 'coordy': 36.87883, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 34호선] 아산 검문소', 'cctvurl': 'http://cctvsec.ktict.co.kr/4138/zn057mNCZlH8LoAhdHJb9PM6zRdGgz1Dc5BvFZDmbXD3cFKK1FjazGFLRb0G0uERqjLGmgKjU1WskNVrevCULXNVRU4Z9TQ9EIDqtbKbcrQ='}, {'roadsectionid': '', 'coordx': 126.81398, 'coordy': 36.88138, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 34호선] 당진 운정교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4139/7bsjaSfLxfMYEkxVUK/hkkd50hTpFb0U8VUCbzSH+1EroD0U1qLHIKw+HXeEmnRJfWHOeAu3xmzegB2FkIcaRkIdVrLcQsvKcxi/j7YI29E='}, {'roadsectionid': '', 'coordx': 126.9328519, 'coordy': 36.9894698, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 38호선] 평택 안중오거리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4150/RlYcecPYSyv6jn9kkZSnKh6Wk6TyeFkNaO3esF4HLHW8yRGpw+Y66kM4pzYzgm0vqPXTvmoNlcxJn2mOlHGw1L2VGE1qr0GQQWhO3OsrkM0='}, {'roadsectionid': '', 'coordx': 126.938666, 'coordy': 36.990555, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 38호선] 평택 안중사거리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4156/+JHJwp8qDAIj8OoTz17+PVNutE++oTmAUlzCjLO3S3Rw5g/T+u/9CFXSByooJdQPx0+KRwFKZI1Jru2zoM+UkEnxAkxz4nugFMKREKdwIOs='}, {'roadsectionid': '', 'coordx': 126.8633157, 'coordy': 36.98916281, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도77호선] 평택 서평택IC사거리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4157/Br8R2ORaH4C73bOyxrKA5/Qv9seCCO26xOmuqaQEvmxqMB+1H2ZGLEwOMN2DQudTl7pn88YiUII0ULnCXAmchwelX58LMhfihLHeWTyVTHo='}, {'roadsectionid': '', 'coordx': 126.8807961, 'coordy': 36.98232068, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 38호선] 평택 내기삼거리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4158/jpbTUWG+siurUICMxgZFn+E0Eaw1PYfLDz7ccQDxcsNnwDbCvA3jneHM/Mv+CdA/AeMbvQVYOvK4r70FkAYGrapeZX7D5zln60JiKcxkI1E='}, {'roadsectionid': '', 'coordx': 126.9124283, 'coordy': 36.99097298, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 38호선] 평택 현화교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4159/uH/Stf2EDIujvV0CgeperlovUgOUW9vzSriljd9HPli8+r4QWoV6c/y7nwtX4yK3I0nBdoSJxAJf2K8hzm2TPPWek3GZ6r8R+7WKEGPxpPk='}, {'roadsectionid': '', 'coordx': 126.79376, 'coordy': 36.93342, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 38호선] 당진 송악읍', 'cctvurl': 'http://cctvsec.ktict.co.kr/4163/t3poJ7/EQCmf7RS7yCfpSvBNDZTZi2ogGuU6muK6CS2ula9P8uJnmzFGDTwZz+Hz3OpBkwKdkg+y4JQyK9yaHe33mPR52lB0vl9GzbxiOYs='}, {'roadsectionid': '', 'coordx': 126.9086813, 'coordy': 37.28304572, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도39호선] 화성 송라저수지', 'cctvurl': 'http://cctvsec.ktict.co.kr/4164/Witls7tf0l6a5Fe2+1uby2d+q4FtqnheAfx3ueQ7W/TUNDIggCyZOs/LjxRZJLBSSIPjuPq+zWCYyq3uRzcnElaaI9kEybYt6OxDj1IETLc='}, {'roadsectionid': '', 'coordx': 126.8964504, 'coordy': 37.25223203, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 화성 숙곡교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4165/I9nIOc5jyTLzc1I+EEHYFnlEcZdhGU2oc8jVAz4PNUnxbYEBtjMIFNvxyzOTwbFUFtwjLNgpwDhth5DUM0hUJgmp+/PB3OLQ7nE5mwAUX4U='}, {'roadsectionid': '', 'coordx': 126.8910689, 'coordy': 37.24504833, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 화성 쌍학교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4166/vWX1MaLwuDAoxyyLbOVVnxoBT0t86cLy+A8g40yMA9P2UQYinSlt25wxIhGSJBig8DNIzJbqULl/GWQCEvV1VCcuwABXaXqqguYL1HP+DDo='}, {'roadsectionid': '', 'coordx': 126.8795083, 'coordy': 37.19392277, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 화성 자안교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4167/Uvyh304EKfrXooQ2KeQUJNmCMFIQ7O4w2Y8egZiMkO2wO6k5wy6VqGzkF1S+mbtrLIVAXjAHAtVktSKaSE8x4bAbpvFI7orG9RSj6ufzRsc='}, {'roadsectionid': '', 'coordx': 126.8927875, 'coordy': 37.14302588, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 화성 지월교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4168/U0h4Bj3gmgKYaEEB7ulDeHRqVEHhat3kiL+Prwh1HTCN3Gal1wUHfTJVrYMD278/1IVlvyzgYUE+TGfTDiSswVyfNwbclYousilaxATEXAg='}, {'roadsectionid': '', 'coordx': 126.9003591, 'coordy': 37.11802091, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도39호선] 화성 제암육교', 'cctvurl': 'http://cctvsec.ktict.co.kr/4169/AWdxsXuJnQl0bJdcCKTYX9Xss+75302Us55XMq+QBeskGMgSgsik9VHnFCB4Cd6oxx6qPL6gbQsmg+9s+JnCMe/vy38xVhhoM4dE8wiO2Yg='}, {'roadsectionid': '', 'coordx': 126.8752729, 'coordy': 37.22220092, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 화성 양노교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4170/otmQhGTUEiuKOXxeG0/mk0CfyyXafxW2z+qDAdNdfXqnJtL+xYMnlZqi/kqjZl176/q3U3UHeMQkF5zIiWhCVtMcrhW2P1GpWvfdSGIR1rg='}, {'roadsectionid': '', 'coordx': 126.91384, 'coordy': 37.071883, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도39호선] 화성 요당2리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4171/OjPKU0B/Ehk06bsC+yIwqYZ4+12wMLTMBa0/ddTSNBoGD4TanddDccY/seOC7wbm6haYoevoN4kEPIvv7pTWp/BkVfV4MPEvNNosgBkpgX4='}, {'roadsectionid': '', 'coordx': 126.9019836, 'coordy': 37.09961835, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 화성 상신지하차도교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4172/x7za+VJY7nLmIyHSlh+kZaJYtX90do62KhF8MMszcO3+ozAqy2HN435+hhBhX4GPx6YN6esvm80Y3bkZZg+mdA/9RQ1/I2t1fZUn4QzwqYA='}, {'roadsectionid': '', 'coordx': 126.9310671, 'coordy': 37.04909753, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 평택 청북교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4173/RqMTbeMaTdIXNkv2YvO7v/nqfrqwwZ6S0Ese2ggAc2JPuqIiv6elsLCK7daDNrfaGTuEIjMt8LA0x3bUjelbT8CI0FWH+DmVxoK1/f2ecm4='}, {'roadsectionid': '', 'coordx': 126.9461948, 'coordy': 37.01442294, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 평택 용성3리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4174/0LR87ydDb2I77b7+Xny9FWY2dmoRIaAKF2BjVqp27GKzrU7mCVNkq6OYZTMxPZNLzRbxzxg7R5iD+gOJJLGmBwTbo2nV0SurWlk6W+K0UqA='}, {'roadsectionid': '', 'coordx': 126.9387053, 'coordy': 36.99656097, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 평택 금곡삼거리', 'cctvurl': 'http://cctvsec.ktict.co.kr/4175/cTlzSqi/j2uA3eZfBPZ2ig9HS6YbFVXZYZq2OoPI1GbSTs/i6ezBQimN5Kgp5rnXhwBHnvRldpY2g6XKplbZoRoAGBrwGq+KIVyWLFM7sTA='}, {'roadsectionid': '', 'coordx': 126.9249815, 'coordy': 36.9606678, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 평택 인광육교', 'cctvurl': 'http://cctvsec.ktict.co.kr/4176/z9aXa5wIqDygvoXWx89lW+e3j+O9zUAAOsAvGz1XnUt1f5gKo3mlbX/RepOB8h6nCV09Hmmjs0v6ScGe9zKhN0qqYPmL0sZpaFQH/lUwBGs='}, {'roadsectionid': '', 'coordx': 126.9124794, 'coordy': 36.95030894, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 평택 기산교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4177/tE0ov4FGcVAWuOEMZ+HqzarSeyJrNe6QRTkCI7aY0lRd0OA8wWzwr6SC7o9gnzuK+GEt5n8EXVeF/gnIwu4rVphn10jdGC4Mbh5vnXXs1FY='}, {'roadsectionid': '', 'coordx': 126.9108423, 'coordy': 36.91790302, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 평택 현덕교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4178/QNG4M94tKMxj12tAu8gL+M2h0IAthm5uau1uUwVEN6u9HLE1wD4CS/mm9uRCO4tJPMBhRCClyWDIde9ppcU5xbIqvVPmke7cYFvOtznH2hA='}, {'roadsectionid': '', 'coordx': 126.989589, 'coordy': 36.80039, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 아산 옥정교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4182/WVAXQOaxRWYYpMmnQTumP5mSabVLMVR4et25y5LWsMraovwKUSbOF+W8YCTW3KyxED34BZf/7RPo3GNHxWwcyGpo+wD2eki+nff8Z5Asmo8='}, {'roadsectionid': '', 'coordx': 126.976723, 'coordy': 36.811052, 'cctvresolution': '', 'filecreatetime': '', 'cctvtype': 1, 'cctvformat': 'HLS', 'cctvname': '[국도 39호선] 아산 곡교교차로', 'cctvurl': 'http://cctvsec.ktict.co.kr/4183/7/iHyNIC1UzhXRELnvzcgNSAdfPgOpvaz5A8h+4JS

# 7. 데이터 프레임 변환
cctv_play = pd.json_normalize(
    json_dict["response"]["data"], sep=''
)
# print(cctv_play)
#      roadsectionid  ...                                            cctvurl
# 0                   ...  http://cctvsec.ktict.co.kr/4027/GS9cuqRaCq9cmh...
# 1                   ...  http://cctvsec.ktict.co.kr/4107/YVJDetuWhH2gGu...
# 2                   ...  http://cctvsec.ktict.co.kr/4108/uEw2V7VUiudn1P...
# 3                   ...  http://cctvsec.ktict.co.kr/4109/XIgVIAd5Mc+EOX...
# 4                   ...  http://cctvsec.ktict.co.kr/4120/bUjLufPLscQPC/...

# 8. CCTV URL 출력
test_url = cctv_play["cctvurl"][1000]
print(f"선택된 CCTV URL : {test_url}")

# 9. 프레임 설정
cap = cv2.VideoCapture(test_url)

# 10. 모델 로드
model = YOLO("yolo11n.pt")

# 11. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인")
        break
    results = model(frame)
    annotated_frame = results[0].plot()

    # 11-1. 윈도우 창 설정 및 띄우기
    cv2.namedWindow("OPENAPI", cv2.WINDOW_NORMAL)   # 창 크기 조절
    cv2.imshow("OPENAPI", annotated_frame)

    # 11-2. q키 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키 눌러서 종료")
        break

# 12. 자원 해제
cap.release()
cv2.destroyAllWindows()