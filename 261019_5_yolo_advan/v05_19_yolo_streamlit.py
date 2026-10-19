from ultralytics import solutions

# 1. inference 객체 생성
inf = solutions.Inference(
    model="yolo11n.pt"
)

# 2. 추론 실행
inf.inference()

# 터미널에서 'streamlit run v05_19_yolo_search.py'로 실행