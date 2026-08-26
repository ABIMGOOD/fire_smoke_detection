from ultralytics import YOLO
import torch

if __name__ == "__main__":
    # ----------------------------
    # 1. Basic Environment Check
    # ----------------------------
    print("CUDA available:", torch.cuda.is_available())
    print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")

    # ----------------------------
    # 2. Load Model
    # ----------------------------
    model = YOLO("yolov8m.pt")

    # ----------------------------
    # 3. Train
    # ----------------------------
    model.train(
        data="data.yaml",          # path to your data.yaml
        epochs=75,
        imgsz=640,
        batch=16,
        device=0,
        workers=8,                 # multiprocessing workers

        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        degrees=5,
        scale=0.5,
        fliplr=0.5,
        mosaic=1.0,

        optimizer="AdamW",
        lr0=0.001,
        weight_decay=0.0005,

        project="fire_detection",
        name="yolov8m_exp1",
    )

    # ----------------------------
    # 4. Validate Best Model
    # ----------------------------
    model.val()