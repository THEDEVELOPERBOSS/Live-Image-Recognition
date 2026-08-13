import tensorflow as tf 
from pathlib import Path 
import cv2 
import time
from tensorflow.keras.optimizers import RMSprop

script_dir = Path(__file__).resolve().parent

# Trains CNN
# This should help make it so I can specify I am taking pictures for training
def dataset_image(): 
    while True:
        print('\nWhat type of image are you taking?')
        print('\n[1] Training')
        print('\n[2] Validation')
        
        dataset_choice = input("\nSelect datset: ").strip()
        
        if dataset_choice == '1':
            dataset_type = 'TRAINING'
            break
        
        elif dataset_choice == '2':
            dataset_type = 'VALIDATION'
            break
        
        print('Please enter 1 or 2')
    while True:
        print('\nWhat is this image of')
        print('[1] Person')
        print('[2] Over Ear Headphones')
        print('[3] Book')
        
        class_choice = input("Select what it is: ").strip()
        
        if class_choice == '1':
            image_class = 'Person'
            break
        elif class_choice == '2':
            image_class = 'Over_Ear_Headphones'
            break
        elif class_choice == '3':
            image_class = 'Book'
            break
        
        print("Please enter a valid number")
    image_class = input(
        "What is this image of? "
    ).strip().lower()
    # Makes it so the folders get made automatically
    save_folder = (
        script_dir
        / 'TRAIN_VAL'
        / dataset_type
        / image_class
    )
    save_folder.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return False
    
    for _ in range(5): # Warm up sensor
        cap.read()
    
    for number in range(3, 0, -1):
        print(number)
        time.sleep(1)
    # Takes picture
    ret, frame = cap.read()
    
    if not ret:
        print('Failed to take picture.')
        cap.release()
        return False

    print("Picture taken")
    # Displays image 
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(2)
    while True:
        choice = input("Save this image? (y/n): ").strip().lower()
        
        if choice in ('y', 'n'):
            break 
        
        print("Please enter y or n")
        
    if choice == 'n':
        cv2.destroyAllWindows()
        print("Retaking...")
    image_name = input("What should I call this image? ").strip()
    # Adds .jpg at the end to give it a file extension if not already done
    if not image_name.lower().endswith('.jpg'): 
        image_name += ".jpg" 
    save_path = save_folder / image_name
    cv2.imwrite(str(save_path), frame)
# Should make this: 
# dataset_type = training
# image_class = horse
# image_name = horse_001.jpg
# into this: 
# TRAIN_VAL/
#└── TRAINING/
#     └── horse/
#        └── horse_001.jpg
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