from ultralytics import YOLO
import cv2, time

# caminho do seu modelo treinado
MODEL_PATH = "runs/detect/train/weights/best.pt"
model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(0)  # 0 = webcam
if not cap.isOpened():
    raise RuntimeError("Não abriu a webcam")

while True:
    ok, frame = cap.read()
    if not ok:
        break

    t0 = time.time()
    results = model.predict(frame, imgsz=640, conf=0.35, verbose=False)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().int().tolist()
            cls = int(box.cls[0].item())
            conf = float(box.conf[0].item())
            name = model.names[cls]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{name} {conf:.2f}", (x1, y1-8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    fps = 1.0 / (time.time() - t0 + 1e-6)
    cv2.putText(frame, f"FPS: {fps:.1f}", (10,25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow("Pokémon Detector", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC pra sair
        break

cap.release()
cv2.destroyAllWindows()
