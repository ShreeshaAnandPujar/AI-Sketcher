# AI Gesture-Controlled Sketch Booth ✨
# Author: Shreesha Pujar

import cv2
import mediapipe as mp
import time
import numpy as np

# Initialize Mediapipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Helper: Convert image to pencil sketch
def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

# Helper: Animate sketch line by line
def animate_sketch(sketch):
    h, w = sketch.shape
    canvas = np.ones((h, w), dtype=np.uint8) * 255
    for y in range(0, h, 2):
        canvas[y:y+2, :] = sketch[y:y+2, :]
        display = cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)
        cv2.imshow("Sketching...", display)
        if cv2.waitKey(10) == ord('q'):
            break
    return canvas

# Helper: Detect open palm gesture
def detect_palm(lm_list):
    if len(lm_list) >= 21:
        fingers = []
        fingers.append(lm_list[4][0] < lm_list[3][0])  # Thumb
        for tip in [8, 12, 16, 20]:
            fingers.append(lm_list[tip][1] < lm_list[tip - 2][1])
        return all(fingers)
    return False

# Video Capture
cap = cv2.VideoCapture(0)
captured = False
countdown = 0
start_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    lm_list = []
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

        if detect_palm(lm_list) and not captured:
            if countdown == 0:
                start_time = time.time()
                countdown = 5

    # Countdown display
    if countdown > 0:
        elapsed = int(time.time() - start_time)
        remaining = countdown - elapsed
        if remaining > 0:
            cv2.putText(frame, f"Stay Still! Capturing in {remaining}", (300, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "Captured! Generating Sketch...", (200, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            sketch_img = pencil_sketch(frame)
            final = animate_sketch(sketch_img)
            cv2.imwrite("client_sketch.png", final)
            cv2.imshow("Final Sketch", final)
            cv2.waitKey(0)
            captured = True
            countdown = 0

    cv2.imshow("AI Sketch Booth", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
