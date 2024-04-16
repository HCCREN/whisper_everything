import os
from pydub import AudioSegment
def m4a_to_wav(input_path, output_path):
    audio = AudioSegment.from_file(input_path, "m4a")
    audio.export(output_path, format="wav")
file_name = '操作模態.m4a'
input_file_path = '/content/drive/MyDrive/Colab Notebooks/sound_data/'+file_name  # 替換為您的M4A文件路徑
output_file_path = '/content/drive/MyDrive/Colab Notebooks/sound_data/'+file_name.split('.')[0] + '.wav'        # 輸出WAV文件的路徑

m4a_to_wav(input_file_path, output_file_path)