# Should be able to set it up to so a different program can listen in for the hotkey and start this up
import cv2 
import os 
from datetime import datetime
from pathlib import Path

# Path.cwd().parent means go up one folder
OUTPUT_FOLDER = Path.cwd().parent / 'IMAGES FROM CAMERA'
ACTIVE_NAME = 'current.jpg'

# Combine folder and filename
full_path = OUTPUT_FOLDER / ACTIVE_NAME
print(full_path.resolve())

def trigger_capture():
    # Archives old photo and captures a fresh one silently
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    if os.path.exists(active_path):
        timestamp = datetime.now().strftime(r'%Y%m%d_%H%M%S')
        os.rename(active_path, os.path.join(OUTPUT_FOLDER, f'archive_{timestamp}.jpg'))
        
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return False
    
    for _ in range(5): # Warm up sensor
        cap.read()
        
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(active_path, frame)
        
    cap.release()
    return ret