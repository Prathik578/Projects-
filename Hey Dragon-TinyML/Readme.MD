# Hey Dragon — TinyML Wake Word Detector

A lightweight keyword-spotting model designed to detect the wake word **"hey_dragon"** against background noise.

The model was trained and deployed using **Edge Impulse** and exported as a C++ inference library for resource-constrained embedded devices.

## 🎯 Objective

Build a small, low-latency wake-word classifier capable of running directly on an edge device without requiring an internet connection.

## 🧠 Model

### Classes

- `hey_dragon`
- `Noise`

The classifier processes short audio samples and predicts whether the wake word is present.

## 📊 Results

### Validation Set

| Metric | Result |
|---|---:|
| Accuracy | **88.5%** |
| Weighted Precision | **0.90** |
| Weighted Recall | **0.88** |
| Weighted F1 | **0.88** |
| ROC-AUC | **0.85** |

### Independent Test Set

| Metric | Result |
|---|---:|
| Accuracy | **75.86%** |
| Weighted Precision | **0.76** |
| Weighted Recall | **0.76** |
| Weighted F1 | **0.75** |
| ROC-AUC | **0.72** |

## ⚡ On-Device Performance

| Resource | Result |
|---|---:|
| Inference time | **~1 ms** |
| Peak RAM | **12.5 KB** |
| Flash usage | **45.6 KB** |

The model is therefore small enough for highly resource-constrained embedded systems.

## 🔍 Evaluation

The independent test set revealed a significant difference between validation and test performance.

The primary limitation is **false positive detection of noise as `hey_dragon`**.

Test-set confusion matrix:

| Actual → Predicted | Noise | hey_dragon | Uncertain |
|---|---:|---:|---:|
| **Noise** | 54.5% | 36.4% | 9.1% |
| **hey_dragon** | 11.1% | 88.9% | 0% |

This indicates that the model recognizes the wake word relatively well but requires better noise generalization for reliable real-world deployment.

## 🛠️ Technology

- Edge Impulse
- TinyML
- C++
- TensorFlow Lite Micro / embedded inference
- TensorBoard

## 📁 Repository Structure

```text
hey-dragon-tinyml/
├── edge-impulse-sdk/
├── model-parameters/
├── tflite-model/
├── CMakeLists.txt
├── README.md
└── README.txt
