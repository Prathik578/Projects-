# Person Recognition with Fine-Tuned MobileNetV2

A person-recognition object detection model developed as part of the **Qualcomm Academy AI Upskilling / Edge AI coursework** using **Edge Impulse**.

The project fine-tunes a **MobileNetV2** model for person detection and evaluates both the original INT32 model and an **INT8 quantised** version for edge deployment.

## Overview

The goal of this project was to explore a practical Edge AI workflow:

**Dataset → Model Training → Transfer Learning/Fine-Tuning → Quantisation → Evaluation → On-Device Performance**

The model was trained to detect people and then converted to an INT8 representation to evaluate its suitability for resource-constrained edge devices.

## Model

* **Task:** Person detection
* **Architecture:** MobileNetV2
* **Training:** Fine-tuned pretrained model
* **Quantisation:** INT8
* **Framework/Platform:** Edge Impulse
* **Course:** Qualcomm Academy – AI Upskilling / Edge AI

## Results

### INT32 Model

| Metric          | Result |
| --------------- | -----: |
| mAP@[IoU=50:95] |   0.66 |
| mAP@50          |   1.00 |
| mAP@75          |   0.76 |
| Recall          |   0.70 |
| Precision       |  87.7% |

### INT8 Quantised Model

| Metric               |     Result |
| -------------------- | ---------: |
| mAP@[IoU=50:95]      |   **0.70** |
| mAP@50               |   **1.00** |
| mAP@75               |   **1.00** |
| Recall               |   **0.73** |
| Precision            |  **88.0%** |
| Inference Time       | **560 ms** |
| Flash Usage          | **3.3 MB** |
| Estimated Arena Size |  **>6 MB** |

The INT8 model maintained strong detection performance while reducing the model representation for edge inference.

## Edge Deployment

The INT8 model was evaluated using Edge Impulse's on-device performance estimation.

The estimated inference time was approximately **560 ms per inference**.

Edge Impulse reported an estimated arena requirement of more than **6 MB**, meaning the model does not fit within the available memory constraints of supported MCUs for this configuration.

## What I Learned

This project provided hands-on experience with:

* Transfer learning and model fine-tuning
* MobileNetV2 for efficient computer vision
* Object detection metrics such as mAP, IoU, precision, and recall
* INT8 quantisation
* Edge inference benchmarking
* Flash and RAM constraints in embedded AI
* The trade-offs between model accuracy and hardware resources

## Technology Stack

* **Python**
* **MobileNetV2**
* **Edge Impulse**
* **Qualcomm Academy**
* **INT8 Quantisation**
* **Computer Vision / Object Detection**

## Acknowledgement

This project was completed as part of the **Qualcomm Academy AI Upskilling coursework** and uses **Edge Impulse** for model development and evaluation.

## License

This repository is intended primarily for educational and portfolio purposes.

