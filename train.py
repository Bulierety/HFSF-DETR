import warnings, os

warnings.filterwarnings('ignore')
from ultralytics import RTDETR


if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/rt-detr/rdetr-HFSFDETR.yaml')
    model.train(data='/VisDrone/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=8,
                workers=4,
                project='train',
                name='HFSF-DETR',
                )