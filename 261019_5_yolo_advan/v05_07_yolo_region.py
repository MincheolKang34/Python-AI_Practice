from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv013.stream/playlist.m3u8")

# 2. 영역 좌표 설정 (dict 형식 - 키로 영역 구분)
region_points = {
    "region1" : [(126, 126), (166, 423), (509, 390), (480, 140)],
    "region2" : [(494, 441), (639, 421), (531, 321), (424, 331), (439, 389)]
}

# 3. 모델 로드
yolo_region = solutions.RegionCounter(
    model="yolo11n.pt",
    show=False,
    region=region_points
)

# 4. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인")
        break
    # 4-1. 프레임 크기 조정(좌표계 통일)
    re_frame = cv2.resize(frame, (640, 480))

    # 4-2. 구역 내 객체 수 계산
    results = yolo_region(re_frame)

    # 4-3. 처리된 프레임 표시(show=False => 우리가 직접 창을 띄움)
    cv2.imshow("REGION", results.plot_im)

    # 4-4. q키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break

# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()