import os
import torch
import whisper
from tqdm import tqdm  # Import the tqdm library

def transcribe_audio_files(folder_path, model, output_folder):
    # List all the files in the folder that are WAV files
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.wav')]

    # Initialize the progress bar
    pbar = tqdm(total=len(file_names), desc="Transcribing audio files")

    for file_name in file_names:
        # Load audio
        audio_path = os.path.join(folder_path, file_name)
        audio = whisper.load_audio(audio_path)

        # Transcribe audio
        text = model.transcribe(audio)

        # Create and save text file
        output_text_path = os.path.join(output_folder, f"{file_name.split('.')[0]}_transcription.txt")
        with open(output_text_path, 'w', encoding='utf-8') as f:
            f.write(text['text'])
        
        # Update the progress bar after each file is processed
        pbar.update(1)

    # Close the progress bar
    pbar.close()

# Check if CUDA is available and set the device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the whisper model
model_size = "small"  # Chosen for compatibility with the available GPU VRAM
model = whisper.load_model(model_size).to(device)

# Folder paths
input_folder = 'sound_data'
output_folder = 'transcriptions'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Transcribe and save text
transcribe_audio_files(input_folder, model, output_folder)
