from ultralytics import YOLO
import pathlib
import os

def train():
    current_path = pathlib.Path().resolve()
    model = YOLO(os.path.join(current_path, 'weights/yolov8n.pt'))
    results = model.train(
        data=os.path.join(current_path, 'dataset_yolo/data.yaml'),
        imgsz=320,
        epochs=10,
        batch=4,
        patience=30,
        name='yolov8n_320',
        device=0,
        augment=True)


if __name__ == '__main__':
    train()
