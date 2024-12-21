from ultralytics import YOLO
import pathlib
import os


def test_predict():
    img = ''
    weights = ''
    model = YOLO(weights)
    presults = model.predict(
        source=img,
        save=True,
        conf=0.0,
    )
    result = {}
    #clases = ["star", "bomb", "diamond", "dog"]
    clases = ["star", "bomb", "diamond"]
    for presult in presults:
        for idx, cls in enumerate(presult.boxes.cls):
            result.setdefault(clases[int(cls)], [])
            result[clases[int(cls)]].append({
                "cls": int(cls),
                "xyxy": presult.boxes[idx].xyxy.cpu().numpy()[0].tolist()
            })
    print(result)


class ObjectDetector:
    def __init__(self):
        current_path = pathlib.Path().resolve()
        weights = os.path.join(current_path, 'weights/last.pt')
        self.model = YOLO(weights)

    def find_object(self, img):
        presults = self.model.predict(
            source=img,
            save=False,
            conf=0.8,
            device=0,
            half=True,
            max_det=10,
        )

        # Обработка результатов предсказания
        result = {
            "star": [],
            "bomb": [],
            "diamond": [],
            "dog": []
        }
        clases = ["star", "bomb", "diamond", "dog"]  # Определяем классы объектов
        for presult in presults:
            for idx, cls in enumerate(presult.boxes.cls):
                result[clases[int(cls)]].append({
                    "xyxy": presult.boxes[idx].xyxy.cpu().numpy()[0].tolist()  # Конвертация координат в список
                })
        return result


if __name__ == '__main__':
    test_predict()
