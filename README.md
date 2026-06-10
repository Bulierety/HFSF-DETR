# HFSF-DETR

Official resources for the paper:
**Spatio-Frequency Feature Preservation and Purification for Real-Time Tiny Object Detection in Aerial Imagery**

---

## Overview
This repository provides the resources associated with the submitted manuscript:
> Spatio-Frequency Feature Preservation and Purification for Real-Time Tiny Object Detection in Aerial Imagery

HFSF-DETR is a lightweight RT-DETR-based framework designed for tiny object detection in aerial imagery. 
The proposed method follows a **Preservation–Purification–Localization** paradigm to improve tiny-object representation while maintaining real-time inference capability.
---

## Experimental Environment

The software environment is summarized as follows:

| Component | Version                 |
| --------- | ----------------------- |
| CUDA      | 11.8                    |
| Python    | 3.10                    |
| PyTorch   | 2.1.0                   |


## Available Resources
To facilitate reproducibility during the review process, the following materials are publicly available:

- Network configuration file (`rdetr-HFSFDETR.yaml`)
- Pretrained model weights
- Evaluation script (`val.py`)
- Heatmap visualization script (`heatmap.py`)
- Experimental protocols and training settings

> **Note:** The implementation of the proposed HFSF-DETR modules will be released after the paper is formally accepted for publication.
---

## Model Configuration

```text
ultralytics/
└── cfg/
    └── models/
        └── rt-detr/
            └── rdetr-HFSFDETR.yaml
```

This configuration file contains the complete network architecture definition used in our experiments.

---

## Pretrained Models

The pretrained weights for HFSF-DETR are publicly available for download:
- [Download pretrained models (Google Drive)](https://drive.google.com/drive/folders/1UY5owUTxbDOGp0nFlMWULYh7YeMfCoof?usp=sharing)

These models include:
- `hfsfdetr_visdrone_best.pt`
- `tinyperson_best.pt`
- `aitodv2i_best.pt`
- `rtdetr_visdrone_best.pt`

| Weight File | Dataset |
|-------------|----------|
| hfsfdetr_visdrone_best.pt | VisDrone2019 |
| tinyperson_best.pt | TinyPerson |
| aitodv2i_best.pt | AI-TODV2i |
| rtdetr_visdrone_best.pt | RT-DETR-R18 Baseline |

The provided checkpoints correspond to the models reported in the experimental section of the paper.

## Data Availability

The datasets used in this study are publicly available from the following sources:

* **VisDrone2019**
  https://github.com/VisDrone/VisDrone-Dataset
* **TinyPerson**
  https://universe.roboflow.com/chris-d-dbyby/tinyperson
* **AI-TODV2i**
  https://universe.roboflow.com/voc-em4sj/ai-tod-mknt4

Please refer to the official dataset websites for download instructions, licensing information, and usage restrictions.

### Evaluation Script
```text
val.py
```

### Visualization Script
```text
heatmap.py
```
Used to generate Grad-CAM++ visualizations presented in the manuscript.


## Experimental Protocol
The training and evaluation settings used in this work are summarized below.

### VisDrone2019

| Setting | Value |
|----------|----------|
| Input Size | 640×640 |
| Epochs | 300 |
| Batch Size | 8 |
| Optimizer | AdamW |
| Initial LR | 1e-4 |

### TinyPerson

| Setting | Value |
|----------|----------|
| Input Size | 768×768 |
| Epochs | 300 |
| Batch Size | 4 |
| Optimizer | AdamW |
| Initial LR | 1e-4 |

### AI-TODV2i

| Setting | Value |
|----------|----------|
| Input Size | 768×768 |
| Epochs | 300 |
| Batch Size | 4 |
| Optimizer | AdamW |
| Initial LR | 1e-4 |


## Code Availability

To facilitate reproducibility during the review process, this repository currently provides:

* Configuration files (`rdetr-HFSFDETR.yaml`)
* Evaluation scripts (`val.py`)
* Visualization scripts (`heatmap.py`)
* Pretrained model weights
* Experimental protocols and benchmark settings

The core implementation of the proposed HFSF-DETR modules is temporarily withheld during the peer-review process.

Upon formal acceptance of the manuscript, the complete source code, including all custom modules, training scripts, and implementation details, will be fully released in this repository.

## Citation

If you find this repository useful, please cite:

```bibtex
@article{hfsfdetr2026,
  title={Spatio-Frequency Feature Preservation and Purification for Real-Time Tiny Object Detection in Aerial Imagery},
  author={Haibo Wang and others},
  journal={The Visual Computer},
  year={2026}
}
```
