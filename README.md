# ✨ AI Gesture-Controlled Sketch Booth
### Built with ❤️ by Shreesha Pujar

A smart, camera-based booth that detects an open-palm gesture, waits for the subject to stay still, captures their image, and creates a cinematic pencil sketch — line by line.

---

## 📸 What It Does
- 🖐️ Detects **open palm gesture** using MediaPipe
- ⏱️ Starts a **5-second countdown** for the person to stay still
- 📷 Captures an image frame automatically
- ✏️ Applies a **pencil sketch effect**
- 🌀 Animates the sketch **line-by-line**
- 💾 Saves final result as `client_sketch.png`

---

## 🔧 How to Run

### 1. Setup Python Environment (Optional but clean)
```bash
python3 -m venv painter_env
source painter_env/bin/activate  # macOS/Linux
painter_env\Scripts\activate   # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Sketch Booth
```bash
python painter.py
```

---

## 🧠 Libraries Used
- [OpenCV](https://opencv.org/) – image processing & webcam
- [MediaPipe](https://google.github.io/mediapipe/) – hand gesture detection
- [NumPy](https://numpy.org/) – array & matrix operations

---

## ✅ Output Sample
A pencil-sketched portrait is saved like this:
```
client_sketch.png
```

---

## 📜 License & Credits
This project is free to use for personal or educational purposes.  
Author: **Shreesha Pujar**  
Feel free to connect or share feedback 💙

---

> 🚀 If you use this in your portfolio, events, or booth — tag `@Shreesha Pujar` and spread the innovation!
