import tensorflow as tf    

import os
from pathlib import Path
# This gets stuff from camera.py
import keyboard
import time

# Set up a non-blocking hook so things can keep running.
# Space is the trigger key and it starts the function in background without freezing main.py
keyboard.add_hotkey('space', camera_handler.trigger_capture) # see if pyautogui can trigger the keyboard

print("Press space to take a picture")

try: 
    while True:
        # Main program goes here complelty unaffected 
        # Tensorflow just has to get IMAGES_FROM_CAMERA/current.jpg when it needs
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping camera feed")

script_dir = Path(__file__).resolve().parent

