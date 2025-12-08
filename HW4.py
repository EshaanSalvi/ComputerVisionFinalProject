import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# --- Load your image ---
billboard_path = "billboard.jpg"  # make sure billboard.jpg is in your working directory
img = mpimg.imread(billboard_path)

# --- Display the image ---
plt.figure(figsize=(10, 6))
plt.imshow(img)
plt.title("Click 4 billboard corners in order:\nTop-Left → Top-Right → Bottom-Right → Bottom-Left")
plt.axis("on")

# --- Wait for 4 clicks ---
clicked_points = plt.ginput(4, timeout=0)  # waits indefinitely for 4 clicks
plt.close()

# --- Convert clicks to numpy array ---
dst_pts = np.array(clicked_points, dtype=np.float32)

# --- Print results ---
print("\n✅ Billboard corner coordinates (x, y):")
print(dst_pts)

# --- Copy-paste format ---
print("\nPaste this into your code:")
print(f"dst_pts = np.array({dst_pts.tolist()}, dtype=np.float32)")
