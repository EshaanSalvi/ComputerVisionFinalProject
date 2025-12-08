import cv2
import os
import numpy as np

# -------------------------------
# CONFIGURATION
# -------------------------------
VIDEO_PATH = "FreeThrows.mov"      # change this to your video name
OUTPUT_FOLDER = "selected_frames"  # folder where chosen frames will be saved
MAX_FRAMES = 80                    # how many frames you want to pick (50–120 recommended)
STEP_SIZE = 5                      # read every Nth frame for speed
DIFF_THRESHOLD = 25_000            # how much difference needed to save a frame


# -------------------------------
# SETUP
# -------------------------------
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)
prev_frame = None
saved = 0
frame_idx = 0

def frame_diff(f1, f2):
    """Compute simple absolute difference between two frames."""
    diff = cv2.absdiff(f1, f2)
    return np.sum(diff)

print("[INFO] Starting automatic frame selection...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Skip frames based on step size
    if frame_idx % STEP_SIZE != 0:
        frame_idx += 1
        continue

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # If first frame — automatically save
    if prev_frame is None:
        cv2.imwrite(f"{OUTPUT_FOLDER}/frame_{saved}.jpg", frame)
        prev_frame = frame_gray
        saved += 1
    else:
        # Compute difference with previous saved frame
        diff_value = frame_diff(frame_gray, prev_frame)

        if diff_value > DIFF_THRESHOLD:
            # Save this frame
            cv2.imwrite(f"{OUTPUT_FOLDER}/frame_{saved}.jpg", frame)
            prev_frame = frame_gray
            saved += 1

    frame_idx += 1

    # Stop if enough frames collected
    if saved >= MAX_FRAMES:
        break

cap.release()
print(f"[INFO] Done! Saved {saved} diverse frames to '{OUTPUT_FOLDER}'")
