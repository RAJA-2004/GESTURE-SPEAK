# ✋ Gesture Speak ✋

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/RAJA-2004/gesture-speak?logo=github&style=for-the-badge)](https://github.com/RAJA-2004/gesture-speak/)
[![GitHub last commit](https://img.shields.io/github/last-commit/RAJA-2004/gesture-speak?style=for-the-badge&logo=git)](https://github.com/RAJA-2004/gesture-speak/)
[![GitHub stars](https://img.shields.io/github/stars/RAJA-2004/gesture-speak?style=for-the-badge)](https://github.com/RAJA-2004/gesture-speak/stargazers)
[![My stars](https://img.shields.io/github/stars/RAJA-2004?affiliations=OWNER%2CCOLLABORATOR&style=for-the-badge&label=My%20stars)](https://github.com/RAJA-2004/gesture-speak/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/RAJA-2004/gesture-speak?style=for-the-badge&logo=git)](https://github.com/RAJA-2004/gesture-speak/network)
[![Code size](https://img.shields.io/github/languages/code-size/RAJA-2004/gesture-speak?style=for-the-badge)](https://github.com/RAJA-2004/gesture-speak)
[![Languages](https://img.shields.io/github/languages/count/RAJA-2004/gesture-speak?style=for-the-badge)](https://github.com/RAJA-2004/gesture-speak)
[![Top](https://img.shields.io/github/languages/top/RAJA-2004/gesture-speak?style=for-the-badge&label=Top%20Languages)](https://github.com/RAJA-2004/gesture-speak)
[![Issues](https://img.shields.io/github/issues/RAJA-2004/gesture-speak?style=for-the-badge&label=Issues)](https://github.com/RAJA-2004/gesture-speak)
[![Watchers](https://img.shields.io/github/watchers/RAJA-2004/gesture-speak?label=Watch&style=for-the-badge)](https://github.com/RAJA-2004/gesture-speak/)

Real-time hand gesture recognition using OpenCV and a pre-trained Keras model. The system detects hand gestures captured through a webcam and classifies them into predefined labels.

## 📖 Project Overview

The project uses the following components:

- [cv2](https://github.com/opencv/opencv): OpenCV library for computer vision.
- [cvzone](https://github.com/cvzone/cvzone): A library providing tools for computer vision applications.
- [Keras](https://github.com/keras-team/keras): A high-level neural networks API.

## ✨ Features

- **🔍 Hand Gesture Detection**: Recognizes hand gestures in real-time using a webcam.
- **📊 Pre-trained Model**: Utilizes a pre-trained Keras model for gesture classification.
- **📦 Easy Setup**: Simple installation and execution process.

## ⚙️ Installation

1. Install the required libraries:

   ```bash
   pip install opencv-python
   pip install numpy
   pip install keras
   pip install mediapipe
   ```

2. Download the pre-trained Keras model ```(keras_model.h5)``` and labels ```(labels.txt)``` from the Model directory.
3. Run the main script:
   ```bash
   python dataCollection.py
   python test.py
   ```

## ✨ Usage

- Execute the script, and it will open a window displaying the webcam feed.
- Make hand gestures within the camera frame, and the system will classify them based on the trained model.
- The recognized gestures and their corresponding labels will be displayed on the screen

## 🔧 Customization

- **Adding New Gestures**: You can expand the dataset and train the model to recognize additional gestures. Update the labels list with the new gesture labels.
- **Adjusting Parameters**: Fine-tune parameters like imgSize, offset, and others in the script to optimize the performance based on your requirements.

## 📸 Examples

Here are some example gestures that the system can recognize:

### Gesture A

![Gesture A](https://github.com/RAJA-2004/GESTURE-SPEAK/raw/main/data/A/Image_1699424096.032801.jpg)

### Gesture C

![Gesture C](https://github.com/RAJA-2004/GESTURE-SPEAK/raw/main/data/C/Image_1699425008.203967.jpg)

### Gesture F

![Gesture F](https://github.com/RAJA-2004/GESTURE-SPEAK/raw/main/data/F/Image_1699452637.640337.jpg)


## Need help?

Feel free to contact me on [LinkedIn](https://www.linkedin.com/in/rajadigvijaysingh/) 

---------

```python
if youEnjoyed:
    starThisRepository()
```

