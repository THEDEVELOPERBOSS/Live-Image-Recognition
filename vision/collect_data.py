import tensorflow as tf 
from pathlib import Path 
import cv2 
import time


script_dir = Path(__file__).resolve().parent

# Collects images for the training and validation datasets
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
            image_class = 'person'
            break
        elif class_choice == '2':
            image_class = 'over_ear_headphones'
            break
        elif class_choice == '3':
            image_class = 'book'
            break
        
        print("Please enter a valid number")
    # Makes it so the folders get made automatically
    save_folder = (
        script_dir
        / 'TRAIN_VAL'
        / dataset_type
        / image_class
    )
    save_folder.mkdir(parents=True, exist_ok=True)
    while True: # keeps looping until one gets chosen to be saved
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return False
        
        for _ in range(5): # Warm up sensor
            cap.read()
        # Countdown
        for number in range(3, 0, -1):
            print(number)
            time.sleep(1)
        # Takes picture
        ret, frame = cap.read()
        
        cap.release()
        
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
            continue
        # Saves image
        image_name = input("What should I call this image? ").strip()
        # Adds .jpg at the end to give it a file extension if not already done
        if not image_name.lower().endswith('.jpg'): 
            image_name += ".jpg" 
        save_path = save_folder / image_name
        cv2.imwrite(str(save_path), frame)
        cv2.destroyAllWindows
        print('Saved image to: ')
        print(save_path)
        
        break
    
    return True
# Should make this: 
# dataset_type = training
# image_class = horse
# image_name = horse_001.jpg
# into this: 
# TRAIN_VAL/
#└── TRAINING/
#     └── horse/
#        └── horse_001.jpg

dataset_image()