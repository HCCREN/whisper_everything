import os
from pydub import AudioSegment
import torch
import whisper

# def m4a_to_wav(input_path, output_path):
    # audio = AudioSegment.from_file(input_path, "m4a")
    # audio.export(output_path, format="wav")

def transcribe_audio_files(folder_path, model, output_folder):
    # List all the files in the folder
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file_name in file_names:
        if not file_name.endswith('.wav'):
            continue  # Skip non-WAV files

        # Load audio
        audio_path = os.path.join(folder_path, file_name)
        audio = whisper.load_audio(audio_path)

        # Transcribe audio
        text = model.transcribe(audio)

        # Create and save text file
        output_text_path = os.path.join(output_folder, f"{file_name.split('.')[0]}_transcription.txt")
        with open(output_text_path, 'w', encoding='utf-8') as f:
            f.write(text['text'])

# Check if CUDA is available and set the device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the whisper model
# My GPU is RTX3050 with 4GB VRAM, so the model can only use the "small" variant.
model_size = "small"  # or "small", "medium", "large" depending on the model size you want to load 
model = whisper.load_model(model_size).to(device)

# Folder containing the audio segments
input_folder = 'sound_data'

# Output folder for the transcriptions
output_folder = 'transcriptions'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Transcribe and save text
transcribe_audio_files(input_folder, model, output_folder)