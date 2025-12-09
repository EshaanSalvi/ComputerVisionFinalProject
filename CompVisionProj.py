#This Python script extracts the total number of frames from the video to help us determine the number of fraames needed for the YOLO model training

import cv2
import os

video_path = "FreeThrows.mov"   #Our free throw shooting video
output_folder = "my_frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
i = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imwrite(os.path.join(output_folder, f"frame_{i}.jpg"), frame)
    i += 1

print("Done extracting frames! Total frames:", i)
