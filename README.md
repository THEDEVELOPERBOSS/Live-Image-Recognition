This is my attempt at making a live image recognition software. I will use tensorflow and keras imports to achieve this. 

Install: 
pip insall tensorflow
pip install opencv-python
pip install opencv-python keyboard


Things I need to do listed in no particular order
- [ ] Pulls live camera feed
- [ ] Training Data Made
- [ ] Validation Data Made
- [ ] Gets files from camera
- [ ] 90 % accuracy 


Rough draft for eventual layout 
PROJECT/
│
├── main.py                 # Runs the actual assistant
│
├── vision/
│   ├── train.py            # Trains the image recognition model
│   ├── camera.py           # Gets frames from the camera
│   ├── predict.py          # Uses the trained model on camera frames
│   └── model.keras         # Saved trained model
│
├── voice/
│   ├── listen.py           # Speech recognition
│   └── speak.py            # Text-to-speech
│
├── agent/
│   └── agent.py            # AI-agent logic
│
├── TRAIN_VAL/
│   ├── TRAINING/
│   └── VALIDATION/
│
└── requirements.txt