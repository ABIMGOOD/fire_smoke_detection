from ultralytics import YOLO
import cv2
import torch

if __name__ == "__main__":

    print("CUDA available:", torch.cuda.is_available())

    # Load trained model
    model = YOLO(r"best.pt")

    # Open video
    cap = cv2.VideoCapture("videos/vid3.mp4")

    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            break

        # Run detection
        results = model(frame, conf=0.5, device=0)

        # Draw predictions on frame
        annotated_frame = results[0].plot()

        # Show frame
        cv2.imshow("Fire & Smoke Detection", annotated_frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()