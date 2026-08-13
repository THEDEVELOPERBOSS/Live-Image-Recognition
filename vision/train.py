import tensorflow as tf 
import os 
from pathlib import Path 
import cv2 
import time
# Trains CNN
# This should help make it so I can specify I am taking pictures for training
def dataset_image(dataset_type, image_class):
        while True:
            dataset_type = input(
                        "Is this for training or validation? "
                ).strip().lower()
            
            if dataset_type in('training', 'validation'):
                break
            
            print("Please enter 'training' or 'validation'")
    
    image_class = input(
        "What is this image of? "
    ).strip().lower()
    # Makes it so the folders get made automatically
    save_folder = (
        script_dir
        / 'TRAIN_VAL'
        / dataset_type.upper()
        
    )
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
    
    for number in range(3, 0, -1):
        print(number)
        time.sleep(1)
        
    ret, frame = cap.read()
    print("Picture taken")
    ret, frame = cap.read()
    
    # show the picture
    ret, frame = cap.read()
    cv2.imshow("Captured Image", frame)
    if ret:
        cv2.imwrite(active_path, frame)
        
    cap.release()
    return ret


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