from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 추론
results = model("input_video.mp4")

# 3. 결과 시각화
results_image = results[0].plot()

# 4. 결과 이미지 저장
cv2.imwrite("./output_det.jpg", results_image)

print("결과 이미지 저장 완료!!")