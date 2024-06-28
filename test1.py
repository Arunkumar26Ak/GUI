import os
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

file_path = "/Users/arun/Documents/srm_4th_sem_project/GUI/baseline_mariya.keras"
print("Current working directory:", os.getcwd())

if os.path.exists(file_path):
    print("File found at:", file_path)
    
    # Recreate the model architecture
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')
    ])
    
    # Load the weights from the HDF5 file
    try:
        model.load_weights(file_path)
        print("Model weights loaded successfully.")
    except Exception as e:
        print("An error occurred while loading model weights:", e)
else:
    print(f"File not found: {file_path}. Please ensure the file path is correct.")

# List directory contents to verify
print("Files in directory:", os.listdir("/Users/arun/Documents/srm_4th_sem_project/GUI/"))
