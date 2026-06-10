import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('/weights/best.pt') # select your model.pt path
    model.predict(source='VisDrone/images/test/9999938_00000_d_0000015.jpg',
                  conf=0.25,
                  project='images',
                  name='HFSF-DETR',
                  save=True,
                  # visualize=True # visualize model features maps
                  line_width=1, # line width of the bounding boxes
                  show_conf=True, # do not show prediction confidence
                  show_labels=True, # do not show prediction labels
                  )

