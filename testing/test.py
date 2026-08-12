from pathlib import Path

#Path.cwd().parent means go up one folder
OUTPUT_FOLDER = Path.cwd().parent / 'IMAGES FROM CAMERA'
ACTIVE_NAME = 'current.jpg'

# Combine folder and filename
full_path = OUTPUT_FOLDER / ACTIVE_NAME
print(full_path.resolve())