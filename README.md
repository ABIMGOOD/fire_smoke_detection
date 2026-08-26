#  Fire & Smoke Detection using YOLO

A computer vision project for detecting **fire and smoke in video streams** using a custom-trained YOLO object detection model.

The project contains a trained model, inference script, sample test video, and example detection results. The goal is to provide a simple and reproducible starting point for real-time fire and smoke detection using Python and OpenCV.

---

## 🚀 Features

- Fire and smoke detection using YOLO
- Video-based inference using OpenCV
- Custom-trained detection model
- Bounding-box visualization with confidence scores
- Simple Python inference pipeline
- Sample test video included
- Trained model included for immediate testing

---

## 📁 Project Structure

```text
fire_smoke_detection/
│
├── best.pt                  # Trained YOLO model
├── README.md
├── requirements.txt
├── .gitignore
├── .gitattributes
│
├── scripts/
│   └── trial1.py            # Detection/inference script
│
├── videos/
│   └── vid3.mp4             # Sample test video
│
└── samples/                 # Example detection results
    ├── detection_01.jpg
    ├── detection_02.jpg
    └── detection_03.jpg
