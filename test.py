#This Python script extracts frames from a video and saves them as images for us to use in training a YOLO model.
#These frames were then used to create the bounding boxes for the hoop and ball in the video using the YOLO annotation tool.

import cv2
import os
import numpy as np


VIDEO_PATH = "FreeThrows.mov"      
OUTPUT_FOLDER = "selected_frames"   #Folder to save selected frames
MAX_FRAMES = 80                     #We only need a few frames since YOLO is good at picking up patterns
STEP_SIZE = 5                       #Process every 5th frame to reduce redundancy
DIFF_THRESHOLD = 25_000             #Threshold for frame difference


# Create output directory if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)
prev_frame = None
saved = 0
frame_idx = 0

def frame_diff(f1, f2):
    
    diff = cv2.absdiff(f1, f2)
    return np.sum(diff)

print("Starting frame selection...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Skip frames based on step size
    if frame_idx % STEP_SIZE != 0:
        frame_idx += 1
        continue

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #If its first frame then save it
    if prev_frame is None:
        cv2.imwrite(f"{OUTPUT_FOLDER}/frame_{saved}.jpg", frame)
        prev_frame = frame_gray
        saved += 1
    else:
        #Compute difference with previous saved frame
        diff_value = frame_diff(frame_gray, prev_frame)

        if diff_value > DIFF_THRESHOLD:
            #Save this frame
            cv2.imwrite(f"{OUTPUT_FOLDER}/frame_{saved}.jpg", frame)
            prev_frame = frame_gray
            saved += 1

    frame_idx += 1

    #Stop when max frames has been reached
    if saved >= MAX_FRAMES:
        break

cap.release()
print(f"Saved {saved} diverse frames to '{OUTPUT_FOLDER}'")
