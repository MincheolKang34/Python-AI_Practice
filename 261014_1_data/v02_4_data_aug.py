import cv2
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = cv2.imread("images.jpg")

# 2. 이미지 증강
# 밝기
img_bright = cv2.convertScaleAbs(img, alpha=1, beta=50)
# alpha : 픽셀에 곱하는 값
# beta : 더할 밝기 (+50 = 밝게, -50 = 어둡게)

# 채도
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
h = (h + 30) % 180
# 채도 범위 변경
img_hue = cv2.cvtColor(cv2.merge([h, s, v]), cv2.COLOR_HSV2BGR)

# 반전(뒤집기)
img_flip = cv2.flip(img, 1)
# 1 : 좌우 반전, 0 : 상하 반전, -1 : 둘 다

# 회전
h, w = img.shape[:2]
M = cv2.getRotationMatrix2D((w/2, h/2), 15, 1.0)
img_rot = cv2.warpAffine(img, M, (w, h), borderMode=cv2.BORDER_REFLECT)
# getRotationMatrix2D(중심, 각도, 배율) : 각도가 양수면 반시계 방향
# BORDER_REFLECT : 회전으로 생긴 빈 공간을 반사된 픽셀로 채움

# 3. 이미지 시각화
fig, ax = plt.subplots(3, 2, figsize=(10, 5))

# 3-1. 원본 이미지
ax[0,0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0,0].axis('off')
ax[0,0].set_title("Original")

# 3-2. 밝기 이미지
ax[0,1].imshow(cv2.cvtColor(img_bright, cv2.COLOR_BGR2RGB))
ax[0,1].axis('off')
ax[0,1].set_title("Bright Image")

# 3-3. 채도 이미지
ax[1,0].imshow(cv2.cvtColor(img_hue, cv2.COLOR_BGR2RGB))
ax[1,0].axis('off')
ax[1,0].set_title("HSV Image")

# 3-4. 좌우 반전 이미지
ax[1,1].imshow(cv2.cvtColor(img_flip, cv2.COLOR_BGR2RGB))
ax[1,1].axis('off')
ax[1,1].set_title("Flip Image")

# 3-5. 회전 이미지
ax[2,1].imshow(cv2.cvtColor(img_rot, cv2.COLOR_BGR2RGB))
ax[2,1].axis('off')
ax[2,1].set_title("Rotate Image")

# 4. 그림창 띄우기
plt.show()

# 5. 이미지 저장
cv2.imwrite("./bright_img.jpg", img_bright)
cv2.imwrite("./hsv_img.jpg", img_hue)
cv2.imwrite("./flip_img.jpg", img_flip)
cv2.imwrite("./rotate_img.jpg", img_rot)
print("이미지 저장 완료")