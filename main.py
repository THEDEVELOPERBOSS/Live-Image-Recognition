import tensorflow as tf    

import os
from pathlib import Path
# This gets stuff from camera.py
import keyboard
import time
import camera_handler

# Set up a non-blocking hook so things can keep running.
# Space is the trigger key and it starts the function in background without freezing main.py
keyboard.add_hotkey('space', camera_handler.trigger_capture) # see if pyautogui can trigger the keyboard

print("Press space to take a picture")

try: 
    while True:
        # Main program goes here complelty unaffected 
        # Tensorflow just has to get IMAGES_FROM_CAMERA/current.jpg when it needs
script_dir = Path(__file__).resolve().parent

file_name = (
    script_dir
    / "TRAIN_VAL"
)

training_dir = (
    script_dir
    / "TRAIN_VAL"
    / "TRAINING"
)


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation='relu' ,
                input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(learning_rate=0.001),
              metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs=1 # change this for train epochs number
)