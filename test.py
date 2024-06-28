import os
from keras.models import load_model
import h5py

file_path = "/Users/arun/Documents/srm_4th_sem_project/GUI/baseline_mariya.keras"

print("Current working directory:", os.getcwd())

if os.path.exists(file_path):
    print("File found at:", file_path)
    
    # Attempt to load as .h5 file
    try:
        model = load_model(file_path)
        print("Model loaded successfully.")
    except OSError as e:
        print("Failed to load as HDF5 file:", e)
    except ValueError as e:
        print("Failed to load model, possibly due to incompatible file format:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

    # Inspect the HDF5 file using h5py
    try:
        with h5py.File(file_path, 'r') as f:
            print("HDF5 file contents:")
            f.visit(print)
    except Exception as e:
        print("An error occurred while reading the HDF5 file:", e)
else:
    print(f"File not found: {file_path}. Please ensure the file path is correct.")

# List directory contents to verify
print("Files in directory:", os.listdir("/Users/arun/Documents/srm_4th_sem_project/GUI/"))
